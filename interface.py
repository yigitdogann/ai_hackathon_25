# app.py
import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd

# Modeli yükle
model = joblib.load("gpa_predictor.pkl")


def predict_gpa():
    try:
        age = int(entry_age.get())
        study_time = float(entry_study.get())
        experience = int(entry_exp.get())
        education = education_var.get()
        style = style_var.get()

        # Dataframe oluştur
        data = {
            "Age": [age],
            "StudyTimeWeekly": [study_time],
            "TeacherExperience": [experience],
            "TeacherEducation": [education],
            "TeachingStyle": [style]
        }
        df = pd.DataFrame(data)

        # Kategorikleri dummy’ye çevir
        df = pd.get_dummies(df)

        # Modelin eğitiminde kullanılan kolonlarla eşleştir
        # Eksik kolon varsa ekle
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0
        df = df[model.feature_names_in_]

        gpa = model.predict(df)[0]
        messagebox.showinfo("Tahmin", f"Tahmini GPA: {gpa:.2f}")
    except Exception as e:
        messagebox.showerror("Hata", str(e))


# GUI
root = tk.Tk()
root.title("GPA Tahmin Uygulaması")

tk.Label(root, text="Öğrenci Yaşı:").grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

tk.Label(root, text="Haftalık Çalışma Saati:").grid(row=1, column=0)
entry_study = tk.Entry(root)
entry_study.grid(row=1, column=1)

tk.Label(root, text="Öğretmen Deneyimi (yıl):").grid(row=2, column=0)
entry_exp = tk.Entry(root)
entry_exp.grid(row=2, column=1)

tk.Label(root, text="Öğretmen Eğitim Düzeyi:").grid(row=3, column=0)
education_var = tk.StringVar()
education_menu = tk.OptionMenu(root, education_var, "Bachelor", "Master", "PhD")
education_menu.grid(row=3, column=1)

tk.Label(root, text="Öğretim Stili:").grid(row=4, column=0)
style_var = tk.StringVar()
style_menu = tk.OptionMenu(root, style_var, "Traditional", "Interactive", "Mixed")
style_menu.grid(row=4, column=1)

tk.Button(root, text="Tahmin Et", command=predict_gpa).grid(row=5, column=0, columnspan=2)

root.mainloop()
