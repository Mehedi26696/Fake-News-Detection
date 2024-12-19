# Fake News Detection

This project aims to detect fake news using machine learning algorithms. The goal is to classify news articles as either genuine or fake based on their content.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Algorithms](#algorithms)
- [Installation](#installation)
- [Usage](#usage)
- [Streamlit App](#streamlit-app)
- [License](#license)

## Introduction
Fake news detection is a critical task in today's digital age. This project leverages machine learning techniques to identify and classify fake news articles.

## Dataset
The dataset used for this project consists of labeled news articles. It includes features such as the article's text, title, and source.

## Algorithms
The following machine learning algorithms are used in this project:
- **Logistic Regression**: A simple and effective linear model for binary classification.
- **Random Forest**: An ensemble method that combines multiple decision trees to improve accuracy.
- **Decision Tree**: A non-linear model that splits the data into subsets based on feature values, creating a tree-like structure for decision making.

## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Usage
To train the model and make predictions, follow these steps:
1. Preprocess the dataset.
2. Train the model using one of the algorithms mentioned above.
3. Evaluate the model's performance.
4. Make predictions on new data.

## Streamlit App
A Streamlit app is included to interactively visualize and test the fake news detection model. To run the app, use the following command:
```bash
streamlit run app.py
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.