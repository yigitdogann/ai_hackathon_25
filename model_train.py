# model_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1️⃣ Veri yükleme
df = pd.read_csv("data/students_with_teachers.csv")

# 2️⃣ Kategorik sütunları one-hot encoding
# drop_first=False kullanıyoruz çünkü Bachelor, Master, PhD hepsi kalsın ki degree_score hesaplayabilelim
df = pd.get_dummies(df, columns=["Teacher_Degree", "Teacher_Style"], drop_first=False)

# 3️⃣ Öğretmen eğitim düzeyi puanını hesapla
degree_score_map = {
    "Teacher_Degree_Bachelor": 1,
    "Teacher_Degree_Master": 2,
    "Teacher_Degree_PhD": 3
}

df["Teacher_Degree_Score"] = (
    df["Teacher_Degree_Bachelor"] * degree_score_map["Teacher_Degree_Bachelor"]
    + df["Teacher_Degree_Master"] * degree_score_map["Teacher_Degree_Master"]
    + df["Teacher_Degree_PhD"] * degree_score_map["Teacher_Degree_PhD"]
)

# 4️⃣ GPA'ya simülasyon etkisi ekle (daha görünür fark yaratır)
df["GPA"] = df["GPA"] + 0.1 * df["Teacher_Degree_Score"]

# 5️⃣ Özellikler ve hedef değişken ayırma
X = df.drop(columns=["GPA", "StudentID", "GradeClass", "TeacherID"])  # GPA'yı hedef olarak tutma
y = df["GPA"]

# 6️⃣ Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7️⃣ Model oluşturma ve eğitme
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 8️⃣ Eğitilen modeli kaydetme
joblib.dump(model, "gpa_predictor.pkl")

print("✅ Model başarıyla eğitildi ve kaydedildi. (Simülasyon eklendi!)")
