# model_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Veri yükleme
df = pd.read_csv("data/students_with_teachers.csv")

# Özellikler ve hedef
features = ["Teacher_ExperienceYears", "Teacher_Degree", "Teacher_Style", "Age", "StudyTimeWeekly"]
target = "GPA"

# Kategorik sütunları one-hot encoding
df = pd.get_dummies(df, columns=["Teacher_Degree", "Teacher_Style"], drop_first=True)

# X ve y ayırma
X = df.drop(columns=[target, "StudentID", "GradeClass", "TeacherID"])  # hedef + ID'leri at
y = df[target]

# Train-Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Modeli kaydet
joblib.dump(model, "gpa_predictor.pkl")

print("✅ Model başarıyla eğitildi ve kaydedildi.")
