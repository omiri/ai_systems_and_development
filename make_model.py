import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Provide baseline training data for the Titanic model
X_train = pd.DataFrame([
[1, 0, 29, 0, 0, 211.3],
[3, 1, 22, 1, 0, 7.25],
[1, 1, 30, 0, 0, 26.55],
[3, 0, 26, 0, 2, 16.44]
], columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])

y_train = [1, 0, 0, 1] 

# 2. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Serialize and save the file
joblib.dump(model, 'titanic_model.joblib')
print("Task 1 Complete: 'titanic_model.joblib' file created successfully!")