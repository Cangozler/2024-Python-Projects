import praw
import io
from PIL import Image, ImageTk
import tkinter as tk
import requests

# Reddit API kimlik bilgilerini gir
reddit = praw.Reddit(
    client_id="n0BUs1H053B_cmZTATATvg",
    client_secret="JCYq3Zr_4QcVHJsrxVYhgHW-_Bv-0A",
    user_agent="MyRedditApp/1.0 (by Prestigious_Leg5895 )"
)

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Reddit Popüler Gönderiler")

# Başlık ve resim gösterme fonksiyonu
def show_post(post):
    title_label.config(text=post.title)

    # Gönderiye resim ekli mi kontrol et
    if post.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
        image_url = post.url
        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail((300, 300))  # Resmi küçült

        # Resmi Tkinter için uygun formata dönüştür
        photo = ImageTk.PhotoImage(image)

        # Resmi göster
        image_label.config(image=photo)
        image_label.image = photo
    else:
        image_label.config(image=None)

# Reddit'den popüler gönderileri çek
subreddit_name = "popular"
post_count = 5
subreddit = reddit.subreddit(subreddit_name)
hot_posts = subreddit.hot(limit=post_count)

# Başlık ve resim gösterme bileşenleri
title_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=400)
title_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

# İlk popüler gönderiyi göster
initial_post = next(hot_posts, None)
if initial_post:
    show_post(initial_post)

# Sonraki popüler gönderi butonu
def show_next_post():
    next_post = next(hot_posts, None)
    if next_post:
        show_post(next_post)

next_button = tk.Button(root, text="Next Post", command=show_next_post)
next_button.pack(pady=10)

# Tkinter penceresini çalıştır
root.mainloop()
