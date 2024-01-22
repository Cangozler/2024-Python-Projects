import tkinter as tk
import random

class CodePuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Puzzle Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#F0F0F0")  # Pencere arka plan rengi

        # Oyun verileri
        self.code_snippets = [
            # Soru 1: Merhaba Dünya (Doğru Cevap: print('Merhaba, Dünya!'))
            "print('Merhaba, Dünya!')",
            
            # Soru 2: 0'dan 2'ye kadar olan sayıları yazdır (Doğru Cevap: for i in range(3):\n    print(i))
            "for i in range(3):\n    print(i)",
            
            # Soru 3: Kare hesaplama fonksiyonu (Doğru Cevap: def kare_hesapla(n):\n    return n ** 2)
            "def kare_hesapla(n):\n    return n ** 2",
            
            # Soru 4: Pozitif veya negatif kontrolü (Doğru Cevap: if sayi > 0:\n    print('Pozitif')\nelse:\n    print('Pozitif değil'))
            "if sayi > 0:\n    print('Pozitif')\nelse:\n    print('Pozitif değil')",
            
            # Soru 5: Renkler listesini yazdırma (Doğru Cevap: renkler = ['kırmızı', 'yeşil', 'mavi']\nfor renk in renkler:\n    print(renk))
            "renkler = ['kırmızı', 'yeşil', 'mavi']\nfor renk in renkler:\n    print(renk)"
        ]
        self.current_code = ""
        self.correct_answer = ""
        self.feedback_list = []

        # Puan etiketi
        self.score = 0
        self.score_label = tk.Label(root, text=f"Puan: {self.score}", font=("Helvetica", 12), bg="#F0F0F0")
        self.score_label.pack(pady=10)

        # Soru etiketi
        self.question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, bg="#F0F0F0")
        self.question_label.pack(pady=10)

        # Cevap giriş kutusu
        self.answer_entry = tk.Entry(root, font=("Helvetica", 14), bg="#FFFFFF")
        self.answer_entry.pack(pady=10)

        # Cevap kontrol düğmesi
        self.check_button = tk.Button(root, text="Cevap Kontrol Et", command=self.check_answer, bg="#4CAF50", fg="white")
        self.check_button.pack(pady=10)

        # Geri Bildirim ekleme
        self.feedback_label = tk.Label(root, text="Geri Bildirim:", font=("Helvetica", 12), bg="#F0F0F0")
        self.feedback_label.pack(pady=10)

        # Geri Bildirim giriş kutusu
        self.feedback_entry = tk.Entry(root, font=("Helvetica", 12), bg="#FFFFFF")
        self.feedback_entry.pack(pady=10)

        # Geri Bildirim ekleme düğmesi
        self.add_feedback_button = tk.Button(root, text="Geri Bildirim Ekle", command=self.add_feedback, bg="#2196F3", fg="white")
        self.add_feedback_button.pack(pady=10)

        # Oyunu başlatma düğmesi
        self.start_button = tk.Button(root, text="Oyunu Başlat", command=self.start_game, bg="#FFC107", fg="black")
        self.start_button.pack(pady=10)

        # Oyunu başlat
        self.start_game()

    def start_game(self):
        # Yeni bir soru oluştur
        self.current_code = random.choice(self.code_snippets)
        self.correct_answer = self.generate_correct_answer(self.current_code)

        # Soru etiketini güncelle
        self.question_label.config(text=self.current_code)

        # Cevap giriş kutusunu temizle
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
    # Kullanıcının cevabını al
        user_answer = self.answer_entry.get()

    # Doğru ve kullanıcı cevaplarını ekrana yazdır
        print("Kullanıcı Cevabı:", user_answer)
        print("Doğru Cevap:", self.correct_answer)

    # Cevabı kontrol et
        if user_answer.strip() == self.correct_answer.strip():
            result_text = f"Tebrikler! Doğru Cevap: ({self.correct_answer})"
            self.score += 1
        else:
            result_text = f"Üzgünüm, Yanlış Cevap. Doğru Cevap: ({self.correct_answer})"

    # Sonuç mesajını göster
        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 12), wraplength=400, bg="#F0F0F0")
        result_label.pack(pady=10)

    # Puanı güncelle ve ekrana yazdır
        self.score_label.config(text=f"Puan: {self.score}")

    def generate_correct_answer(self, code):
    # Kod içerisinden rastgele bir kelimeyi eksik bırakarak seç
     lines = code.split('\n')
     random_line = random.choice(lines)
     words = random_line.split()
     missing_word = random.choice(words)
 
    # Eksik kelimenin yerine boşluk bırak
     missing_word_index = words.index(missing_word)
     words[missing_word_index] = '______'
 
    # Doğru cevabı oluştur
     correct_answer = ' '.join(words).strip('.,;:!?\'"()[]{}<>')  # Noktalama işaretlerini temizle
     return correct_answer


    def add_feedback(self):
        # Kullanıcının girdiği geri bildirimi al
        feedback_text = self.feedback_entry.get()

        # Geri bildirimi listeye ekle
        self.feedback_list.append(feedback_text)

        # Geri bildirimleri ekrana yazdır
        self.update_feedback_display()

        # Geri bildirim giriş kutusunu temizle
        self.feedback_entry.delete(0, tk.END)

    def update_feedback_display(self):
        # Geri bildirim etiketini güncelle
        feedback_text = "\n".join(self.feedback_list)
        self.feedback_label.config(text=f"Geri Bildirim:\n{feedback_text}")

# Tkinter penceresini oluştur
root = tk.Tk()

# Oyunu başlat
game = CodePuzzleGame(root)

# Tkinter penceresini çalıştır
root.mainloop()
