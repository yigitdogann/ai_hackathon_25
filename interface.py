# app.py
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import joblib
import pandas as pd
import sys, os

def resource_path(relative_path):
    """PyInstaller ile çalışırken dosya yolunu çözer"""
    try:
        base_path = sys._MEIPASS  # PyInstaller geçici klasörü
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Modeli yükle
model = joblib.load(resource_path("gpa_predictor.joblib"))

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

        messagebox.showinfo("Tahmin", f"Tahmini OBP: {gpa:.2f}")
        progress.set(gpa / 100.0)
        gpa_label.configure(text=f"Tahmini OBP: {gpa:.2f}")

    except Exception as e:
        messagebox.showerror("Hata", str(e))


# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("🎓 OBP Tahmin Uygulaması")

# Tam ekran
root.state("zoomed")

# ---------------- Arkaplan resmi ----------------
bg_image = ctk.CTkImage(
    light_image=Image.open(resource_path("assets/Arkaplan.jpg")),
    dark_image=Image.open(resource_path("assets/Arkaplan.jpg")),
    size=(1920, 1080)
)
bg_label = ctk.CTkLabel(root, image=bg_image, text="")
bg_label.place(relx=0.5, rely=0.5, anchor="center")
# ------------------------------------------------

# Grid yapılandırması → ortalama için
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Ana çerçeve
main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.grid(row=1, column=1, padx=50, pady=50)

# ----------- EKRAN ORANLI FONTLAR -------------
screen_height = root.winfo_screenheight()
title_font_size = int(screen_height * 0.05)   # başlık için %5
label_font_size = int(screen_height * 0.03)   # label için %3
# ----------------------------------------------

# Başlık
title = ctk.CTkLabel(main_frame,
                     text="Öğrenci OBP Tahmini",
                     font=ctk.CTkFont(size=title_font_size, weight="bold"))
title.pack(pady=50)

# Yaş
frame_age = ctk.CTkFrame(main_frame)
frame_age.pack(pady=10, fill="x")
ctk.CTkLabel(frame_age, text="Öğrenci Yaşı:", font=ctk.CTkFont(size=label_font_size)).pack(side="left", padx=50)
entry_age = ctk.CTkEntry(frame_age)
entry_age.pack(side="right", padx=30)

# Haftalık çalışma saati
frame_study = ctk.CTkFrame(main_frame)
frame_study.pack(pady=10, fill="x")
ctk.CTkLabel(frame_study, text="Haftalık Çalışma Saati:", font=ctk.CTkFont(size=label_font_size)).pack(side="left", padx=50)
entry_study = ctk.CTkEntry(frame_study)
entry_study.pack(side="right", padx=30)

# Öğretmen deneyimi
frame_exp = ctk.CTkFrame(main_frame)
frame_exp.pack(pady=10, fill="x")
ctk.CTkLabel(frame_exp, text="Öğretmen Deneyimi (yıl):", font=ctk.CTkFont(size=label_font_size)).pack(side="left", padx=50)
entry_exp = ctk.CTkEntry(frame_exp)
entry_exp.pack(side="right", padx=30)

# Eğitim düzeyi
frame_edu = ctk.CTkFrame(main_frame)
frame_edu.pack(pady=10, fill="x")
ctk.CTkLabel(frame_edu, text="Öğretmen Eğitim Düzeyi:", font=ctk.CTkFont(size=label_font_size)).pack(side="left", padx=50)
education_var = ctk.StringVar(value="Bachelor")
education_menu = ctk.CTkOptionMenu(frame_edu, variable=education_var,
                                   values=["Bachelor", "Master", "PhD"])
education_menu.pack(side="right", padx=30)

# Öğretim stili
frame_style = ctk.CTkFrame(main_frame)
frame_style.pack(pady=10, fill="x")
ctk.CTkLabel(frame_style, text="Öğretim Stili:", font=ctk.CTkFont(size=label_font_size)).pack(side="left", padx=50)
style_var = ctk.StringVar(value="Lecture")
style_menu = ctk.CTkOptionMenu(frame_style, variable=style_var,
                               values=["Lecture", "Project-Based", "Interactive"])
style_menu.pack(side="right", padx=30)

# Tahmin butonu
predict_btn = ctk.CTkButton(main_frame, text="Tahmin Et", command=predict_gpa, width=200)
predict_btn.pack(pady=30)

# GPA Progress Bar
progress = ctk.DoubleVar(value=0.0)
progressbar = ctk.CTkProgressBar(main_frame, variable=progress, width=300)
progressbar.pack(pady=30)
gpa_label = ctk.CTkLabel(main_frame, text="Tahmini OBP: -", font=ctk.CTkFont(size=label_font_size))
gpa_label.pack(pady=40)

root.mainloop()
