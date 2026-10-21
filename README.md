# Python Machine Learning Assignment

**Name:** Duncan Njoroge 

## Project Description

### Supervised Learning: Exam Score Prediction
This project uses Linear Regression to estimate a student's exam score from the number of hours studied.

### Unsupervised Learning: Customer Segmentation
This project uses K-Means to group supermarket customers based on their monthly spending and monthly visits.

## Setup and Running

Open a terminal in the project folder and run:
```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
```

```bash
python supervised_ml.py
python unsupervised_ml.py
```

## Part C: Theory Questions

### 1. What is supervised machine learning?
Supervised Machine Learning is a type of machine learning where a model is trained on a labeled dataset where every training data consists of an input feature paired with the correct, known output label. It learns a mapping function to predict the outputs of new, unseen data.

### 2. What is unsupervised machine learning?
Unsupervised machine learning is when a model looks for patterns or groups in data that does not have labeled answers. For example, K-Means can group customers by their shopping behavior.

### 3. What is the difference between supervised and unsupervised learning?
Supervised learning uses data that includes the correct answers, called labels. The model learns from these examples to predict answers for new data. Unsupervised learning uses data without labels and tries to find patterns or groups on its own.

### 4. Why is Linear Regression considered supervised learning?
Linear Regression is supervised learning because it is trained using examples that include both input values and known target values. In this project, the inputs are study hours and the targets are exam scores. The model learns their relationship so it can estimate a score for new study hours.

### 5. Why is K-Means considered unsupervised learning?
K-Means is considered unsupervised learning because it groups data without being given correct group labels. It uses similarities in the data to assign each customer to a cluster.

### 6. What is the difference between fit() and predict()?
fit() trains a model by having it learn from the training data. predict() uses what the model  learned to produce an output for new input data.

### 7. What are real-world applications of supervised learning and unsupervised learning?
Supervised learning is used for predicting house prices from features such as size and location, and for classifying emails as spam or not spam. Unsupervised learning is used for grouping customers by shopping behavior and for grouping news articles by topic.

