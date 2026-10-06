import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. Create Sample Dataset
# ==========================================

data = {
    "study_hours": [
        1, 2, 2.5, 3, 3.5,
        4, 4.5, 5, 5.5, 6,
        6.5, 7, 7.5, 8, 8.5,
        9, 9.5, 10
    ],

    "attendance": [
        50, 55, 58, 60, 62,
        65, 68, 70, 72, 75,
        78, 80, 82, 85, 87,
        90, 93, 95
    ],

    "previous_marks": [
        35, 40, 42, 45, 48,
        50, 53, 55, 58, 60,
        63, 65, 68, 70, 73,
        76, 80, 85
    ],

    "final_marks": [
        40, 43, 46, 49, 52,
        55, 58, 61, 64, 67,
        70, 73, 76, 79, 82,
        85, 88, 92
    ]
}

df = pd.DataFrame(data)


# ==========================================
# 2. Display Dataset
# ==========================================

print("\n========== STUDENT DATA ==========\n")
print(df)


# ==========================================
# 3. Separate Features and Target
# ==========================================

X = df[[
    "study_hours",
    "attendance",
    "previous_marks"
]]

y = df["final_marks"]


# ==========================================
# 4. Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 5. Create Linear Regression Model
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)


# ==========================================
# 6. Test Model
# ==========================================

predictions = model.predict(X_test)


print("\n========== MODEL EVALUATION ==========\n")

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")


# ==========================================
# 7. Compare Actual vs Predicted
# ==========================================

results = pd.DataFrame({
    "Actual Marks": y_test.values,
    "Predicted Marks": predictions.round(2)
})

print("\n========== ACTUAL vs PREDICTED ==========\n")
print(results)


# ==========================================
# 8. Take User Input
# ==========================================

print("\n========== STUDENT MARKS PREDICTOR ==========\n")

study_hours = float(
    input("Enter study hours per day: ")
)

attendance = float(
    input("Enter attendance percentage: ")
)

previous_marks = float(
    input("Enter previous marks: ")
)


# ==========================================
# 9. Predict Final Marks
# ==========================================

student_data = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_marks": [previous_marks]
})

predicted_marks = model.predict(student_data)[0]


# Keep marks between 0 and 100
predicted_marks = max(0, min(100, predicted_marks))


# ==========================================
# 10. Display Result
# ==========================================

print("\n==========================================")
print(f"Predicted Final Marks: {predicted_marks:.2f}/100")
print("==========================================")

if predicted_marks >= 80:
    print("Performance: Excellent 🎉")
elif predicted_marks >= 70:
    print("Performance: Very Good 👍")
elif predicted_marks >= 60:
    print("Performance: Good")
elif predicted_marks >= 50:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")