# OBP Tahmin Edici

Uygulamamız, öğretmen özelliklerinin öğrenci lise ortalamasına (OBP) olan etkisini hesaplamayı amaçlamaktadır. 

## Uygulama Hakkında

Öğrenciler öğretmenlerinin,  
• Tecrübe yıllarını (1 - 25).  
• Aldıkları eğitim düzeylerini (Bachelor - Master - PhD).  
• Dersi öğretme stillerini (Lecture - Project Based - Interactive).  
Kendi haftalık ders çalışma saatiyle birlikte uygulamaya girdi olarak verdiğinde, liseyi bitirdiklerine elde edecekleri OBP’leri (Ortaöğretim Başarı Puanı) tahmin edilecektir.  

*Not: Lise öğrenci yaş aralığı 15’ten 18’e kadar, haftalık çalışma saati ise 1 ile 20 arası olarak hesaplanacaktır.*

## Uygulama Yapısı

**Dataset:**  
	•	Öğrenci özelliklerini (yaş, çalışma saati, GPA vb.) içeren bir dataset kullanılmıştır.    
	•	Ek olarak, sahte öğretmen bilgileri (tecrübe, eğitim seviyesi, öğretim stili) öğrencilere rastgele dağıtılarak veri setine eklenmiştir.    
	•	Gerçek öğretmen-öğrenci eşleşmeleri bulunmadığından, model deneysel amaçla geliştirilmiştir.  
**Model:**  
	•	Random Forest algoritması kullanılmıştır.  
	•	Öğrenci ve öğretmen özellikleri birlikte modele verilmiştir.  
**Arayüz:**  
	•	Kullanıcı dostu bir masaüstü arayüzü ile öğrenci/öğretmen bilgileri girilip tahmin alınabilir.  


## Geliştirilebilir yönleri:
• Toplanan gerçek datalar aracılığıyla model geliştirilebilir, doğruluğu yüksek tahminler yapacak duruma getirilebilir.  
• Farklı makine öğrenmesi algoritmaları denenebilir.  

