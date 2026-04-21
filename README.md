# SubtiQ-AI 🚀

### A Predictive Model for Substance-Use among Students

---

## 📌 Overview

SubtiQ-AI is a machine learning-based predictive system designed to identify the risk of substance addiction among students. The system integrates clinical, behavioral, and academic data to enable early detection and intervention.

Substance addiction is a growing concern affecting students due to factors such as peer pressure, academic stress, and emotional instability. This project aims to provide a data-driven solution for early risk prediction and prevention. 

---

## 🎯 Objectives

* Develop a machine learning model to predict addiction risk
* Analyze clinical biomarkers and behavioral indicators
* Enable early intervention and preventive care
* Provide a user-friendly web-based prediction system
* Support educators and healthcare professionals in decision-making 

---

## 🧠 Key Features

* 🔍 Multi-domain data analysis (medical + academic + behavioral)
* 🤖 Machine Learning prediction system
* 📊 Exploratory Data Analysis (EDA)
* 🌐 Web-based interface using Flask
* 🔐 Secure login system (Admin & User)
* 📈 Real-time prediction results

---

## 🗂️ Dataset Details

* 📊 ~75,000 student records

* 📌 20 features across multiple domains:

  * Medical: ALT, GGT, Glucose, Creatinine, THC, Cocaine, Opioid
  * Academic: Attendance, marks drop, assignments
  * Behavioral: Mood swings, peer influence, social media usage

* 🏷️ Labeled as:

  * Addicted
  * Not Addicted 

---

## 📊 Dataset Sample (Preview)

The following table shows a sample of the dataset used for training the model:

| StudentID | ALT | GGT | Glucose | Creatine | THC | Cocaine | Opioid | pH  | Attendance | Marks Drop | Assign Delay | Leave | Mood | Peer Issues | Discipline | Counseling | Social Media | Gaming | Label        |
| --------- | --- | --- | ------- | -------- | --- | ------- | ------ | --- | ---------- | ---------- | ------------ | ----- | ---- | ----------- | ---------- | ---------- | ------------ | ------ | ------------ |
| S03902    | 64  | 10  | 125     | 1.28     | Yes | No      | Yes    | 6.0 | 1          | 0          | 1            | 0     | 0    | 0           | 0          | 1          | 1            | 1      | Addicted     |
| S04901    | 13  | 53  | 144     | 1.25     | No  | No      | No     | 6.2 | 0          | 0          | 0            | 0     | 0    | 1           | 1          | 0          | 1            | 0      | Not Addicted |
| S03946    | 119 | 51  | 113     | 1.49     | Yes | No      | No     | 5.4 | 0          | 0          | 1            | 0     | 0    | 1           | 0          | 1          | 0            | 1      | Addicted     |
| S04397    | 30  | 100 | 84      | 1.03     | No  | No      | No     | 6.4 | 0          | 0          | 0            | 0     | 1    | 1           | 0          | 0          | 1            | 0      | Not Addicted |
| S01164    | 61  | 179 | 121     | 1.10     | No  | No      | Yes    | 6.0 | 0          | 0          | 0            | 0     | 0    | 0           | 1          | 0          | 0            | 1      | Not Addicted |
| S01784    | 71  | 10  | 70      | 1.54     | No  | No      | No     | 6.4 | 1          | 0          | 0            | 0     | 1    | 1           | 1          | 1          | 0            | 1      | Addicted     |
| S02085    | 84  | 29  | 144     | 1.44     | No  | No      | No     | 5.8 | 0          | 0          | 1            | 1     | 0    | 0           | 1          | 0          | 0            | 0      | Not Addicted |
| S05058    | 51  | 59  | 86      | 1.14     | Yes | No      | No     | 5.6 | 1          | 0          | 0            | 0     | 1    | 0           | 1          | 1          | 0            | 0      | Not Addicted |
| S01864    | 62  | 120 | 96      | 1.28     | Yes | No      | No     | 6.1 | 0          | 0          | 1            | 0     | 0    | 1           | 0          | 1          | 0            | 0      | Not Addicted |

---

## 📌 Data Privacy & Access

The dataset preview shown above contains a limited number of entries and has been **partially masked and anonymized** to protect sensitive information.

The complete dataset consists of a significantly larger number of records and features, which are not publicly available due to **privacy policies, ethical considerations, and institutional restrictions**.

For further information or collaboration requests, please contact the author.


## 🛠️ Tech Stack

### 🔹 Backend

* Python
* Flask

### 🔹 Machine Learning

* Logistic Regression
* Random Forest
* CatBoost (Final Model)

### 🔹 Data Processing

* Pandas
* PySpark
* Scikit-learn

### 🔹 Frontend

* HTML, CSS, JavaScript

---

## ⚙️ System Architecture

The system follows a **3-tier architecture**:

1. **User Interface Layer** – Data input & result display
2. **Logic Layer** – ML model processing & prediction
3. **Data Layer** – Data handling and transformation 

---

## 🔄 Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Prediction & Evaluation
7. Web Application Integration

---

## 📊 Model Performance

* Evaluated using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * AUC

* **CatBoost** achieved the best performance for prediction. 

---

## 🌍 Real-World Impact

* Helps in early detection of addiction risk
* Supports schools and counselors
* Enables preventive healthcare strategies
* Aligns with SDGs:

  * Good Health & Well-being
  * Quality Education
  * Innovation & Infrastructure 

---

## 🚀 Future Scope

* Deployment as a cloud-based system
* Mobile application integration
* Real-time monitoring
* Explainable AI integration
* Improved dataset scalability

---

## 👩‍💻 Team

* Athira Raj
* Alan D Sam
* Antony Thomas
* Fathima N

---

## 🏫 Institution

Carmel College of Engineering & Technology
APJ Abdul Kalam Technological University

---

## 📌 Note

This project is developed for academic and research purposes and aims to contribute to early intervention in substance addiction among students.

The dataset preview shown above includes a limited sample (10 entries) for demonstration purposes.
Sensitive information has been masked and anonymized to ensure privacy and ethical compliance.
The complete dataset consists of a significantly larger number of records and features, which are not publicly shared due to data confidentiality, security, and institutional restrictions.
For further details, access requests, or collaboration inquiries, please feel free to contact the author.
