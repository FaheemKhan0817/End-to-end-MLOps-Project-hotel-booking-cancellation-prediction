Hotel Reservation Prediction 🏨✨

MLOps Project

Python Flask

Docker Google Cloud

Welcome to Hotel Reservation Prediction, an MLOps-driven machine learning project designed to predict hotel booking cancellations with precision and style! This end-to-end solution combines data science, web development, and DevOps to deliver a scalable, user-friendly application. 🚀
🎯 Project Overview

This project predicts whether a hotel reservation will be canceled based on booking details like lead time, average room price, and special requests. It’s perfect for hotel managers looking to optimize operations and reduce revenue loss from cancellations.

    Input: Booking features (e.g., lead time, arrival date, meal plan).
    Output: Prediction (0 = Cancel, 1 = Not Cancel).
    Tech Stack: Python, Flask, LightGBM, Docker, Jenkins, Google Cloud Run, MLflow.

🌟 Features

    Sleek Web UI: A modern, grid-based interface for easy input and predictions.
    Automated Workflow: CI/CD pipeline with Jenkins for training and deployment.
    Scalable Deployment: Hosted on Google Cloud Run via Docker containers.
    Experiment Tracking: MLflow logs model parameters, metrics, and artifacts.
    Robust Preprocessing: Handles skewness, encodes categories, and balances data with SMOTE.

🛠️ Project Structure
text
Hotel-Reservation-Prediction/
├── config/                   # Configuration files
│   ├── paths_config.py       # File paths
│   └── model_params.py       # Model hyperparameters
|
├── src/                      # Core source code
│   ├── data_ingestion.py     # Fetch and split data from MySQL
│   ├── data_preprocessing.py # Preprocess, balance, and select features
│   ├── model_training.py     # Train and evaluate LightGBM model
│   ├── logger.py             # Custom logging utility
│   └── custom_exception.py   # Custom exception handling
├── static/                   # Static assets
│   └── style.css             # Custom CSS for UI
├── templates/                # Flask templates
│   └── index.html            # Web UI template
├── app.py                    # Flask web application
├── training_pipeline.py      # Orchestrates the ML pipeline
├── custom_jenkins_docker     # Jenkins pipeline configuration
├── Dockerfile                # Docker configuration (assumed)
└── README.md                 # This file! 👋
🚀 Getting Started
Prerequisites

    Python 3.9+
    Docker
    Jenkins (with Docker support)
    Google Cloud SDK
    MySQL database
    MLflow server (http://localhost:5000)

Installation

    Clone the Repository
    bash

git clone https://github.com/data-guru0/MLOPS-COURSE-PROJECT-1.git
cd MLOPS-COURSE-PROJECT-1
Set Up Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
Configure Environment

    Update config/paths_config.py with your file paths (e.g., TRAIN_FILE_PATH, MODEL_OUTPUT_PATH).
    Set MySQL credentials in your config.yaml (assumed from data_ingestion.py).
    Add Google Cloud credentials to Jenkins as gcp-key.

Run Locally
bash

    python app.py
    Visit http://localhost:8080 to test the app.

🏃‍♂️ How It Works

    Data Ingestion: Pulls data from MySQL, splits it into train/test sets.
    Preprocessing: Drops duplicates, encodes categories, handles skewness, balances data with SMOTE, and selects top features.
    Training: Trains a LightGBM model with hyperparameter tuning, tracked via MLflow.
    Deployment: Jenkins builds a Docker image, pushes it to GCR, and deploys to Cloud Run.
    Prediction: Users enter booking details via the web UI to get real-time predictions.

🎨 Web Interface

The UI is designed for beauty and usability:

    Compact Grid: 3-column layout fits all inputs on one screen.
    Stylish Design: Gradient backgrounds, borders, and hover effects.
    Error Feedback: Clear messages for invalid inputs.

UI Screenshot

(Add your actual screenshot here, e.g., ./static/ui-screenshot.png)
⚙️ CI/CD Pipeline

The Jenkins pipeline automates everything:

    Clone: Fetches code from GitHub.
    Setup: Installs dependencies in a virtual environment.
    Build: Creates and pushes a Docker image to Google Container Registry.
    Deploy: Deploys to Google Cloud Run (us-central1).

Run it in Jenkins to see the magic happen! ✨
📊 Model Performance

    Algorithm: LightGBM with RandomizedSearchCV for tuning.
    Metrics: Accuracy, Precision, Recall, F1-Score (logged to MLflow).
    Features: Top 10 selected via RandomForest importance.

View results in MLflow at http://localhost:5000.
🌐 Deployment

Deployed on Google Cloud Run:

    URL: (Insert your Cloud Run URL here, e.g., https://ml-project-abc123-uc.a.run.app).
    Access: Public (--allow-unauthenticated).

🤝 Contributing

We’d love your help!

    Fork the repo.
    Create a branch: git checkout -b feature/cool-idea.
    Commit changes: git commit -m "Add cool idea".
    Push: git push origin feature/cool-idea.
    Open a Pull Request.

📧 Contact

Questions? Reach out!

    Author: [Your Name]
    GitHub: data-guru0
    Email: your.email@example.com

✨ Acknowledgments

    xAI for inspiring AI innovation.
    LightGBM for fast, accurate predictions.
    Flask for a lightweight web framework.
    Google Cloud for scalable hosting.

⭐ Star this repo if you like it! ⭐

Happy predicting! 🏨💡
