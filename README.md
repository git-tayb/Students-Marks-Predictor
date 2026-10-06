# 🎓 Student Marks Predictor

A beginner-friendly **Machine Learning project** that predicts a student's final marks based on:

* 📚 Study Hours
* 📅 Attendance Percentage
* 📝 Previous Marks

The project uses **Linear Regression** from Scikit-learn and is designed as a simple **one-file Machine Learning project**.

---

## 🚀 Features

* Create a student dataset using Pandas
* Split data into training and testing sets
* Train a Linear Regression model
* Evaluate the model using:

  * Mean Absolute Error (MAE)
  * R² Score
* Compare actual and predicted marks
* Take custom student information from the user
* Predict final examination marks
* Display a performance category

---

## 🛠️ Technologies Used

| Technology        | Purpose              |
| ----------------- | -------------------- |
| Python            | Programming Language |
| Pandas            | Data manipulation    |
| Scikit-learn      | Machine Learning     |
| Linear Regression | Prediction Model     |

---

## 📁 Project Structure

```text
student-marks-predictor/
│
├── main.py
└── README.md
```

The complete Machine Learning project is contained inside **`main.py`**.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-marks-predictor.git
```

### 2. Open the project directory

```bash
cd student-marks-predictor
```

### 3. Install required libraries

```bash
pip install pandas scikit-learn
```

---

## ▶️ Run the Project

Run the following command:

```bash
python main.py
```

---

## 🧠 How It Works

The model uses three input features:

```text
Study Hours
     +
Attendance
     +
Previous Marks
     ↓
Linear Regression Model
     ↓
Predicted Final Marks
```

### Input Features

#### 1. Study Hours

Number of hours the student studies per day.

Example:

```text
7 hours
```

#### 2. Attendance

Student's attendance percentage.

Example:

```text
85%
```

#### 3. Previous Marks

Marks obtained in previous examinations.

Example:

```text
72
```

---

## 📊 Machine Learning Process

### Step 1 — Create Dataset

A sample student dataset is created using Pandas.

```python
df = pd.DataFrame(data)
```

### Step 2 — Select Features

```python
X = df[
    [
        "study_hours",
        "attendance",
        "previous_marks"
    ]
]
```

### Step 3 — Select Target

The target variable is the student's final marks.

```python
y = df["final_marks"]
```

### Step 4 — Split Dataset

The dataset is divided into training and testing data.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Step 5 — Train Model

A Linear Regression model is created and trained.

```python
model = LinearRegression()

model.fit(X_train, y_train)
```

### Step 6 — Make Predictions

```python
predictions = model.predict(X_test)
```

### Step 7 — Evaluate Model

The project calculates:

```text
Mean Absolute Error (MAE)
R² Score
```

---

## 📈 Model Evaluation

### Mean Absolute Error

MAE tells us the average difference between actual and predicted marks.

A lower MAE generally means better predictions.

```python
mae = mean_absolute_error(
    y_test,
    predictions
)
```

### R² Score

R² indicates how well the model explains the variation in the target values.

```python
r2 = r2_score(
    y_test,
    predictions
)
```

---

## 💻 Example

When you run the program, it asks:

```text
Enter study hours per day: 7
Enter attendance percentage: 85
Enter previous marks: 72
```

The model then predicts the student's final marks:

```text
==========================================
Predicted Final Marks: 78.XX/100
==========================================
Performance: Very Good
```

The exact prediction can vary depending on the trained model and dataset.

---

## 🎯 Performance Categories

The project categorizes the predicted marks as:

|    Marks | Performance       |
| -------: | ----------------- |
|   80–100 | Excellent         |
|    70–79 | Very Good         |
|    60–69 | Good              |
|    50–59 | Average           |
| Below 50 | Needs Improvement |

---

## 📚 What I Learned From This Project

This project demonstrates the basic Machine Learning workflow:

```text
Data Collection
      ↓
Data Preparation
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Prediction
      ↓
Model Evaluation
```

Through this project, you can practice:

* Python
* Pandas
* Data preprocessing
* Feature selection
* Train/test splitting
* Linear Regression
* Model training
* Model prediction
* MAE
* R² Score

---

## 🔮 Future Improvements

This project can be expanded by adding:

* [ ] Real student dataset from CSV
* [ ] Data visualization using Matplotlib
* [ ] More student features
* [ ] Multiple Machine Learning models
* [ ] Random Forest Regression
* [ ] Decision Tree Regression
* [ ] User-friendly GUI
* [ ] Web interface using Flask or FastAPI
* [ ] Model saving using Joblib
* [ ] Deployment to a cloud platform

---

## 👨‍💻 Author

**Tayyab**

Beginner Data Science & Machine Learning Project

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **educational and learning purposes**.
