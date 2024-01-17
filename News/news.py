import requests
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import scrolledtext

def haber_basliklarini_getir():
    try:
        # Otomatik olarak RSS feed URL'sini oluştur
        rss_url = "https://www.haberturk.com/rss/manset.xml"
        haber_url="https://www.haberturk.com/rss"

        # RSS feed'ini al
        response = requests.get(rss_url)
        response.raise_for_status()

        # XML içeriğini parse et
        root = ET.fromstring(response.content)

        # Haber başlıklarını ekrana yazdır
        for item in root.iter('item'):
            haber_baslik = item.find('title').text.strip()
            scrolled_text.insert(tk.END, haber_baslik + "\n\n")

    except Exception as err:
        scrolled_text.insert(tk.END, f"Hata: {err}\n\n")
def haberler():
    try:
        haber_url="https://www.haberturk.com/rss"
        response = requests.get(haber_url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        for item in root.iter('item'):
            haber_baslik = item.find('title').text.strip()
            scrolled_text.insert(tk.END, haber_baslik + "\n\n")
    except Exception as err:
        scrolled_text.insert(tk.END, f"Hata: {err}\n\n")    
def ekonomi():
    try:
        ekonomi_url="https://www.haberturk.com/rss/ekonomi.xml"
        response = requests.get(ekonomi_url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        for item in root.iter('item'):
            haber_baslik = item.find('title').text.strip()
            scrolled_text.insert(tk.END, haber_baslik + "\n\n")
    except Exception as err:
        scrolled_text.insert(tk.END, f"Hata: {err}\n\n")    
def spor():
    try:
        spor_url="https://www.haberturk.com/rss/spor.xml"
        response = requests.get(spor_url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        for item in root.iter('item'):
            haber_baslik = item.find('title').text.strip()
            scrolled_text.insert(tk.END, haber_baslik + "\n\n")
    except Exception as err:
        scrolled_text.insert(tk.END, f"Hata: {err}\n\n")    

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Haberler Made.by Cangozler")
root.configure(bg="#a9d6e5")
root.geometry("420x250")
# Haber başlıklarını göstermek için kaydırılabilir metin alanı
scrolled_text = scrolledtext.ScrolledText(root, width=50, height=10, bg="#001524", fg="#ffffff")
scrolled_text.pack()

# Haber başlıklarını getir butonu
button_haber = tk.Button(root, text="Haberler",command=haberler, bg="#fffcf2",fg="#61a5c2")
button_haber.pack(side=tk.LEFT, padx=10)

button_ekonomi = tk.Button(root, text="Ekonomi Haberleri",command=ekonomi, bg="#fffcf2",fg="#61a5c2")
button_ekonomi.pack(side=tk.LEFT, padx=18)

button_getir = tk.Button(root, text="Manşetler", command=haber_basliklarini_getir, bg="#fffcf2",fg="#61a5c2")
button_getir.pack(side=tk.RIGHT,padx=15)

button_spor = tk.Button(root, text="Spor haberleri", command=spor, bg="#fffcf2",fg="#61a5c2")
button_spor.pack(side=tk.RIGHT,padx=10)

# Tkinter döngüsünü başlat
root.mainloop()
