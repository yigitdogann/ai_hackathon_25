# app.py
import customtkinter as ctk
from tkinter import messagebox
import joblib
import pandas as pd

# Modeli yükle
model = joblib.load("gpa_predictor.pkl")

# Tahmin fonksiyonu
def predict_gpa():
    try:
        age = int(entry_age.get())
        study_time = float(entry_study.get())
        experience = int(entry_exp.get())
        education = education_var.get()
        style = style_var.get()

        data = {
            "Age": [age],
            "StudyTimeWeekly": [study_time],
            "Teacher_ExperienceYears": [experience],
            "Teacher_Degree": [education],
            "Teacher_Style": [style]
        }
        df = pd.DataFrame(data)
        df = pd.get_dummies(df)

        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0
        df = df[model.feature_names_in_]

        gpa = model.predict(df)[0]

        messagebox.showinfo("Tahmin", f"Tahmini GPA: {gpa:.2f}")
        progress.set(gpa / 4.0)
        gpa_label.configure(text=f"Tahmini GPA: {gpa:.2f}")

    except Exception as e:
        messagebox.showerror("Hata", str(e))


# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("🎓 GPA Tahmin Uygulaması")

# Tam ekran
root.state("zoomed")

# Grid yapılandırması → ortalama için
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Ana çerçeve (ortalanacak)
main_frame = ctk.CTkFrame(root)
main_frame.grid(row=1, column=1, padx=20, pady=20)

# Başlık
title = ctk.CTkLabel(main_frame, text="Öğrenci GPA Tahmini", font=ctk.CTkFont(size=22, weight="bold"))
title.pack(pady=15)

# Yaş
frame_age = ctk.CTkFrame(main_frame)
frame_age.pack(pady=5, fill="x")
ctk.CTkLabel(frame_age, text="Öğrenci Yaşı:").pack(side="left", padx=10)
entry_age = ctk.CTkEntry(frame_age)
entry_age.pack(side="right", padx=10)

# Haftalık çalışma saati
frame_study = ctk.CTkFrame(main_frame)
frame_study.pack(pady=5, fill="x")
ctk.CTkLabel(frame_study, text="Haftalık Çalışma Saati:").pack(side="left", padx=10)
entry_study = ctk.CTkEntry(frame_study)
entry_study.pack(side="right", padx=10)

# Öğretmen deneyimi
frame_exp = ctk.CTkFrame(main_frame)
frame_exp.pack(pady=5, fill="x")
ctk.CTkLabel(frame_exp, text="Öğretmen Deneyimi (yıl):").pack(side="left", padx=10)
entry_exp = ctk.CTkEntry(frame_exp)
entry_exp.pack(side="right", padx=10)

# Eğitim düzeyi
frame_edu = ctk.CTkFrame(main_frame)
frame_edu.pack(pady=5, fill="x")
ctk.CTkLabel(frame_edu, text="Öğretmen Eğitim Düzeyi:").pack(side="left", padx=10)
education_var = ctk.StringVar(value="Bachelor")
education_menu = ctk.CTkOptionMenu(frame_edu, variable=education_var,
                                   values=["Bachelor", "Master", "PhD"])
education_menu.pack(side="right", padx=10)

# Öğretim stili
frame_style = ctk.CTkFrame(main_frame)
frame_style.pack(pady=5, fill="x")
ctk.CTkLabel(frame_style, text="Öğretim Stili:").pack(side="left", padx=10)
style_var = ctk.StringVar(value="Lecture")
style_menu = ctk.CTkOptionMenu(frame_style, variable=style_var,
                               values=["Lecture", "Interactive", "Project-Based"])
style_menu.pack(side="right", padx=10)

# Tahmin butonu
predict_btn = ctk.CTkButton(main_frame, text="📊 Tahmin Et", command=predict_gpa, width=200)
predict_btn.pack(pady=20)

# GPA Progress Bar
progress = ctk.DoubleVar(value=0.0)
progressbar = ctk.CTkProgressBar(main_frame, variable=progress, width=300)
progressbar.pack(pady=10)
gpa_label = ctk.CTkLabel(main_frame, text="Tahmini GPA: -", font=ctk.CTkFont(size=16))
gpa_label.pack(pady=5)

root.mainloop()
