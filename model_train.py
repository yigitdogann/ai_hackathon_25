# model_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1️⃣ Veri yükleme
df = pd.read_csv("data/students_with_teachers.csv")

# 2️⃣ Kategorik sütunları one-hot encoding
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

# 4️⃣ GPA değerini 100’lük sisteme dönüştür (eğer veriler 4’lük ise)
df["GPA"] = df["GPA"] * 25

# 5️⃣ Öğretmen eğitim derecesinin etkisi (yüksek derece → daha yüksek GPA)
df["GPA"] += df["Teacher_Degree_Score"] * 5   # Lisans +5, Master +10, PhD +15

# 6️⃣ Tecrübe etkisi (1–25 yıl arası, ~13 yıl en yüksek etki)
df["Experience_Effect"] = -0.15 * (df["Teacher_ExperienceYears"] - 13)**2 + 15
df["Experience_Effect"] = df["Experience_Effect"].clip(lower=0)  # negatif çıkarsa sıfırla
df["GPA"] += df["Experience_Effect"]

# 7️⃣ Öğretim stili etkisi
style_effects = {
    "Project-Based": 3,   # istediğin katkıyı verecek
    "Lecture": 0,         # geleneksel ders, etki yok
    "Interactive": 2      # interaktif ders, biraz katkı
}

for style, effect in style_effects.items():
    if style in df.columns:
        df["GPA"] += df[style] * effect

# 8️⃣ Özellikler ve hedef değişken kısmı
X = df.drop(columns=["GPA", "StudentID", "GradeClass", "TeacherID"])
y = df["GPA"]

# 9️⃣ Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔟 Model oluşturma ve eğitme
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 1️⃣1️⃣ Eğitilen modeli kaydetme
joblib.dump(model, "gpa_predictor.pkl")

print("✅ Model başarıyla eğitildi ve kaydedildi. (100’lük sistem + dereceler + tecrübe + stil etkileri eklendi!)")

#test push for wrong pull