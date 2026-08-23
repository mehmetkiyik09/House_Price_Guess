from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LinearRegression
import uvicorn

# 1. API Uygulamasını Başlat
app = FastAPI(title="Yapay Zeka Ev Tahmin Servisi")

# 2. Modeli Eğit (Sunucu açılırken bir kere yapılır)
veri = {
    'Metrekare': [50, 80, 100, 120, 150],
    'Fiyat_TL': [1500000, 2200000, 2800000, 3100000, 3900000]
}
df = pd.DataFrame(veri)
X = df[['Metrekare']]
y = df['Fiyat_TL']

model = LinearRegression()
model.fit(X, y)

# 3. İnternetten Gelen İstekleri Karşılayacak Kapıyı (Endpoint) Aç
@app.get("/tahmin")
def fiyat_tahmin_et(metrekare: float):
    # İnternetten gelen metrekareyi DataFrame'e çevirip modele sor
    istek_df = pd.DataFrame({'Metrekare': [metrekare]})
    tahmin_sonucu = model.predict(istek_df)[0]
    
    # Sonucu JSON formatında geri döndür
    return {
        "girilen_metrekare": metrekare,
        "tahmini_fiyat_tl": round(tahmin_sonucu, 2)
    }

# 4. Sunucuyu Çalıştır
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)