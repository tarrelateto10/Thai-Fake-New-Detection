# Thai Fake News Detection Web Application
This repository contains a Flask web application that serves a machine learning model to make predictions based on input data. The model was trained using the thai news dataset and a RandomForestClassifier from scikit-learn.

## Introduction
This project demonstrates how to train a machine learning model, save it, and use it in a Flask web application to provide predictions via an API endpoint. The model used in this project is a RandomForestClassifier trained on the Iris dataset.

## Features
Train and save a machine learning model
Load the model in a Flask app
Provide predictions via a RESTful API

## Compare Model

![screenshot](https://github.com/tarrelateto10/Thai-Fake-New-Detection/blob/main/documents/compare%20Model.png?raw=true)


## Installation
To run this project locally, follow these steps:

1. Clone the repository:
```
    git clone https://github.com/tarrelateto10/Thai-Fake-New-Detection.git
    cd Thai-Fake-New-Detection
```
2. Create a virtual environment and activate it:
```
    python3 -m venv venv
    source venv/bin/activate
```
3. Install the required packages:
```
    pip install -r requirements.txt
```
4. Run the Flask app:
```
    python app.py
```

# Usage
After running the Flask app, you can access the App endpoint at http://127.0.0.1:5000/.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or enhancements.

# Contact
For any questions or inquiries, please contact tar.relate@gmail.com.

