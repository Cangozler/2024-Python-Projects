import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        # Turkish: Ana sınıfın kurucu metodu. Tkinter penceresini ve arayüzü başlatır.
        # English: Constructor of the main class. Initializes the Tkinter window and the interface.
        self.master = master
        master.title("Weather App")

        # Turkish: Arka plan rengini siyah yapar.
        # English: Sets the background color to black.
        master.configure(bg="#95adb6")

        # Turkish: Şehir girişi için etiket oluşturulur, metni ve ön plan rengini ayarlar.
        # English: Creates a label for the city entry, sets the text, and foreground color.
        self.label_city = tk.Label(master, text="City:", bg="#DBC7BE", fg="#ffffff")
        self.label_city.pack()

        # Turkish: Şehir girişi için metin kutusu oluşturulur, arka plan ve ön plan rengini ayarlar.
        # English: Creates an entry for the city, sets the background and foreground color.
        self.entry_city = tk.Entry(master, bg="#EF959C", fg="#ffffff")
        self.entry_city.pack()

        # Turkish: Hava durumu bilgisini almak için buton oluşturulur, arka plan rengini altın rengine, ön plan rengini siyaha ayarlar.
        # English: Creates a button to get the weather, sets the background color to gold, and foreground color to black.
        self.button_get_weather = tk.Button(master, text="Get Weather", command=self.get_weather, bg="#DBC7BE", fg="#000000")
        self.button_get_weather.pack()

        # Turkish: Hava durumu bilgilerini göstermek için etiket oluşturulur, arka plan rengini siyah, ön plan rengini beyaza ayarlar.
        # English: Creates a label to display weather information, sets the background color to black, and foreground color to white.
        self.label_info = tk.Label(master, text="", bg="#95ADB6", fg="#ffffff")
        self.label_info.pack()

    def get_weather(self):
        # Turkish: Kullanıcının girdiği şehir bilgisini alır.
        # English: Gets the city information entered by the user.
        city = self.entry_city.get().strip()
        if city:
            API_KEY = "faac498d6c8fa5ff2067ed034bb76bd4"
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            try:
                # Turkish: API'ye istek gönderir.
                # English: Sends a request to the API.
                response = requests.get(api_url)
                data = response.json()

                # Turkish: İstek başarılı ise hava durumu bilgilerini alır ve gösterir.
                # English: If the request is successful, retrieves and displays weather information.
                if response.status_code == 200:
                    weather_info = {
                        "City": data["name"],
                        "Condition": data["weather"][0]["description"],
                        "Temperature": data["main"]["temp"],
                        "Humidity": data["main"]["humidity"],
                        "Wind Speed": data["wind"]["speed"]
                    }
                    # Turkish: Hava durumu bilgilerini etikete yazar.
                    # English: Writes weather information to the label.
                    self.label_info.config(
                        text=f"{weather_info['City']} Weather:\n"
                             f"Condition: {weather_info['Condition']}\n"
                             f"Temperature: {weather_info['Temperature']}°C\n"
                             f"Humidity: {weather_info['Humidity']}%\n"
                             f"Wind Speed: {weather_info['Wind Speed']} m/s"
                    )
                else:
                    # Turkish: API hatası durumunda hata mesajını gösterir.
                    # English: Displays an error message in case of an API error.
                    messagebox.showerror("Error", f"Error: {data['message']}")

            except Exception as e:
                # Turkish: Genel bir hata durumunda hata mesajını gösterir.
                # English: Displays a general error message in case of an exception.
                messagebox.showerror("Error", f"Error: {e}")
        else:
            # Turkish: Kullanıcı bir şehir girmemişse uyarı mesajını gösterir.
            # English: Displays a warning if the user didn't enter a city.
            messagebox.showwarning("Warning", "Please enter a city.")

if __name__ == '__main__':
    root = tk.Tk()
    # Turkish: Arka plan rengini siyah yapar.
    # English: Sets the background color to black.
    root.configure(bg="#95adb6")
    app = WeatherApp(root)
    root.mainloop()
