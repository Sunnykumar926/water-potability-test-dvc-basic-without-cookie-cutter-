# Water Potability Prediction with DVC and FastAPI
This project demonstrates how to build a machine learning pipeline using Data Version Control (DVC), 
along with the basics of creating an API using FastAPI. The primary goal of this project is to understand 
the workflow of DVC and integrate it with a simple FastAPI application. Note that model accuracy is not the focus; 
the emphasis is on learning and implementing DVC in a machine learning project.

Prediction/
│
├── data/
│   ├── processed_test.csv
│   ├── processed_train.csv
│   └── raw/
│       └── water_potability.csv
│
├── my_env/  # Python virtual environment
│
├── src/
│   ├── data/
│   │   ├── data_collection.py
│   │   ├── data_pred_model.py
│   │   └── data_prep.py
│   ├── model_building.py
│   ├── model_eval.py
│   └── main.py
│
├── test.py
├── .dvc/
├── .gitignore
├── dvc.yaml
├── dvc.lock
├── metrics.json
├── model.pkl
├── params.yaml
├── requirements.txt
└── water_potability.csv
