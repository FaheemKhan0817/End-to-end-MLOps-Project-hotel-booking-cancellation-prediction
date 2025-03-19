import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        # Extract the data ingestion configuration
        self.config = config["data_ingestion"]
        
        # Set database connection parameters from config
        self.db_host = self.config["db_host"]
        self.db_port = self.config["db_port"]
        self.db_name = self.config["db_name"]
        self.db_user = self.config["db_user"]
        self.db_password = self.config["db_password"]
        self.table_name = self.config["table_name"]
        self.train_test_ratio = self.config["train_ratio"]

        # Log the start of data ingestion with database details
        logger.info(f"Data Ingestion started with database {self.db_name} and table {self.table_name}")

    def fetch_data_from_db(self):
        """Fetch data from the MySQL database into a pandas DataFrame."""
        try:
            logger.info("Connecting to the database")
            
            # Create a connection string for SQLAlchemy
            connection_string = f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            engine = create_engine(connection_string)
            
            # Query to fetch all data from the specified table
            query = f"SELECT * FROM {self.table_name}"
            data = pd.read_sql(query, engine)
            
            logger.info("Data fetched successfully from the database")
            return data
        
        except Exception as e:
            logger.error("Error while fetching data from the database")
            raise CustomException("Failed to fetch data from the database", e)

    def split_data(self, data):
        """Split the DataFrame into training and test sets and save them to CSV files."""
        try:
            logger.info("Starting the splitting process")
            
            # Split the data based on the train-test ratio
            train_data, test_data = train_test_split(data, test_size=1-self.train_test_ratio, random_state=42)
            
            # Ensure the directories for train and test files exist
            os.makedirs(os.path.dirname(TRAIN_FILE_PATH), exist_ok=True)
            os.makedirs(os.path.dirname(TEST_FILE_PATH), exist_ok=True)
            
            # Save the split data to CSV files without the index column
            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)
            
            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into training and test sets", e)

    def run(self):
        """Execute the data ingestion process."""
        try:
            logger.info("Starting data ingestion process")
            
            # Fetch data from the database and split it
            data = self.fetch_data_from_db()
            self.split_data(data)
            
            logger.info("Data ingestion completed successfully")
        
        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
        
        finally:
            logger.info("Data ingestion completed")

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()