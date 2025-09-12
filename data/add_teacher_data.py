import pandas as pd
import numpy as np

#öğrenci CSV dosyasını aç
df = pd.read_csv("students_performance.csv")

#oluşturulacak örnek 10 öğretmen için ID'ler
teacher_ids = [f"T{i}" for i in range(1, 11)]

#her öğrenciye rastgele öğretmen atamak için
np.random.seed(42)
df["TeacherID"] = np.random.choice(teacher_ids, size=len(df))

#öğretmen özelliklerini oluşturma kısmı (tecrübe-eğitim-stil)
teacher_info = {
    "T1":  {"ExperienceYears": 1,  "Degree": "Bachelor", "Style": "Lecture"},
    "T2":  {"ExperienceYears": 3,  "Degree": "Bachelor", "Style": "Interactive"},
    "T3":  {"ExperienceYears": 5,  "Degree": "Master",   "Style": "Project-Based"},
    "T4":  {"ExperienceYears": 7,  "Degree": "Master",   "Style": "Lecture"},
    "T5":  {"ExperienceYears": 10, "Degree": "Master",   "Style": "Interactive"},
    "T6":  {"ExperienceYears": 15, "Degree": "PhD",      "Style": "Lecture"},
    "T7":  {"ExperienceYears": 25, "Degree": "PhD",      "Style": "Project-Based"},
    # 3 öğretmen 12 yıllık ama farklı derece ve stile sahip
    "T8":  {"ExperienceYears": 12, "Degree": "Bachelor", "Style": "Interactive"},
    "T9":  {"ExperienceYears": 12, "Degree": "Master",   "Style": "Lecture"},
    "T10": {"ExperienceYears": 12, "Degree": "PhD",      "Style": "Project-Based"}
}

#öğrenci satırlarına yeni sütunda öğretmen özelliklerini ekle
df["Teacher_ExperienceYears"] = df["TeacherID"].apply(lambda x: teacher_info[x]["ExperienceYears"])
df["Teacher_Degree"] = df["TeacherID"].apply(lambda x: teacher_info[x]["Degree"])
df["Teacher_Style"] = df["TeacherID"].apply(lambda x: teacher_info[x]["Style"])

#yeni CSV'ye kaydet
df.to_csv("students_with_teachers.csv", index=False)
print("10 öğretmen verisi başarıyla eklendi ve CSV kaydedildi")