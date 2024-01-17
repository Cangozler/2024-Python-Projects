import requests
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import scrolledtext

def haber_basliklarini_getir():
    try:
        # Otomatik olarak RSS feed URL'sini oluştur
        rss_url = "https://www.haberturk.com/rss/manset.xml"

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

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Habertürk Haber Başlıkları")

# Haber başlıklarını göstermek için kaydırılabilir metin alanı
scrolled_text = scrolledtext.ScrolledText(root, width=50, height=10)
scrolled_text.pack()

# Haber başlıklarını getir butonu
button_getir = tk.Button(root, text="Haber Başlıklarını Getir", command=haber_basliklarini_getir)
button_getir.pack()

# Tkinter döngüsünü başlat
root.mainloop()
