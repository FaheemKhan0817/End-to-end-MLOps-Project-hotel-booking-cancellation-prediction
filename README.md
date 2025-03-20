# Hotel Reservation Prediction 🏨✨

## MLOps Project

### Python Flask | Docker | Google Cloud

Welcome to **Hotel Reservation Prediction**, an **MLOps-driven machine learning project** designed to predict hotel booking cancellations with precision and style! 🚀  
This end-to-end solution integrates **data science, web development, and DevOps**, offering a **scalable, user-friendly application**.

---

## 🎯 Project Overview

This project predicts whether a **hotel reservation will be canceled** based on booking details like **lead time, average room price, and special requests**.  
Ideal for **hotel managers**, helping them **optimize operations** and **reduce revenue loss** from cancellations.

- **Input**: Booking features (e.g., lead time, arrival date, meal plan).
- **Output**: Prediction (0 = Canceled, 1 = Not Canceled).
- **Tech Stack**: Python, Flask, LightGBM, Docker, Jenkins, Google Cloud Run, MLflow.

---

## 🌟 Features

✅ **Sleek Web UI** - A modern, grid-based interface for easy input and predictions.  
✅ **Automated Workflow** - CI/CD pipeline with **Jenkins** for training and deployment.  
✅ **Scalable Deployment** - Hosted on **Google Cloud Run** via **Docker containers**.  
✅ **Experiment Tracking** - MLflow logs **model parameters, metrics, and artifacts**.  
✅ **Robust Preprocessing** - Handles **skewness, encodes categories, and balances data** with SMOTE.  

---

## 🛠️ Project Structure

```
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
├── pipeline/
    └──training_pipeline.py   # Orchestrates the ML pipeline
├── custom_jenkins/
│   ├── docker/               # Jenkins pipeline configuration
├── Dockerfile                # Docker configuration
└── README.md                 # This file! 👋
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python **3.9+**
- Docker
- Jenkins (with Docker support)
- Google Cloud SDK
- MySQL database
- MLflow server (`http://localhost:5000`)

### Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/FaheemKhan0817 End-to-end-MLOps-Project-hotel-booking-cancellation-prediction.git
cd End-to-end-MLOps-Project-hotel-booking-cancellation-prediction
```

#### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
pip install -r requirements.txt
```

#### 3️⃣ Configure Environment

- Update **config/paths_config.py** with correct file paths (e.g., `TRAIN_FILE_PATH`, `MODEL_OUTPUT_PATH`).
- Set MySQL credentials in `config.yaml`.
- Add **Google Cloud credentials** to Jenkins as `gcp-key`.

#### 4️⃣ Run Locally

```bash
python app.py
```

Visit [http://localhost:8080](http://localhost:8080) to test the app.

---

## 🏃‍♂️ How It Works

1. **Data Ingestion**: Pulls data from MySQL, splits it into train/test sets.
2. **Preprocessing**: Drops duplicates, encodes categories, handles skewness, balances data with **SMOTE**, and selects top features.
3. **Training**: Trains a **LightGBM** model with **hyperparameter tuning**, tracked via MLflow.
4. **Deployment**: Jenkins **builds a Docker image**, pushes it to GCR, and deploys to **Cloud Run**.
5. **Prediction**: Users enter **booking details via the web UI** to get real-time predictions.

---

## 🎨 Web Interface

✨ **Sleek & User-Friendly UI** ✨

- **Compact Grid**: 3-column layout for a smooth user experience.  
- **Stylish Design**: Gradient backgrounds, borders, and hover effects.  
- **Error Feedback**: Clear messages for invalid inputs.  

🖼 **UI Screenshot** 
![Hotel Reservation Prediction UI](static/main.jpg)

---

## ⚙️ CI/CD Pipeline

The **Jenkins pipeline** automates the workflow:

1️⃣ **Clone**: Fetches code from GitHub.  
2️⃣ **Setup**: Installs dependencies in a virtual environment.  
3️⃣ **Build**: Creates and pushes a Docker image to **Google Container Registry**.  
4️⃣ **Deploy**: Deploys to **Google Cloud Run** (`us-central1`).  

Run it in **Jenkins** to see the magic happen! ✨

---

## 📊 Model Performance

- **Algorithm**: LightGBM with **RandomizedSearchCV** for tuning.  
- **Metrics**: Accuracy, Precision, Recall, F1-Score (**logged in MLflow**).  
- **Features**: **Top 10 selected** via RandomForest importance.  

View results in **MLflow** at [`http://localhost:5000`](http://localhost:5000).

---

## 🌐 Deployment

Deployed on **Google Cloud Run**:

## Live Demo
Check out the live demo of the Hotel Reservation Prediction project here: [Hotel Reservation Prediction](https://end-to-end-mlops-project-hotel-booking.onrender.com/)

---

## 🤝 Contributing

We’d love your help!

1. **Fork** the repo.  
2. **Create a branch**: `git checkout -b feature/cool-idea`.  
3. **Commit changes**: `git commit -m "Add cool idea"`.  
4. **Push**: `git push origin feature/cool-idea`.  
5. **Open a Pull Request**.  

---

## 📧 Contact

📌 **Author**: [Faheem Khan]  
📌 **GitHub**: [FaheemKhan0817](https://github.com/FaheemKhan0817)  
📌 **Email**: `faheemthakur23@gmail.com`  

---

## ✨ Acknowledgments
 
🔹 **LightGBM** for fast, accurate predictions.  
🔹 **Flask** for a lightweight web framework.  
🔹 **Google Cloud** for scalable hosting.  

⭐ **Star this repo if you like it!** ⭐  

Happy predicting! 🏨💡  
