import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from scapy.all import sniff
import threading
import time  # Zaman gecikmesi için

class TrafficAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Analyzer")

        # Ağ trafiğini izleme butonu
        self.btn_traffic = tk.Button(root, text="Ağ Trafigini İzle", command=self.start_traffic_analysis)
        self.btn_traffic.pack(pady=10)

        # VPN bağlantısını değiştirme butonu
        self.btn_change_vpn = tk.Button(root, text="VPN Değiştir", command=self.toggle_vpn_connection)
        self.btn_change_vpn.pack(pady=10)

        # VPN durumu
        self.vpn_connected = False

        # Listbox ve Scrollbar oluştur
        self.listbox = Listbox(root, height=15, width=110, selectbackground='gray', selectmode='extended', bg='black', fg='green')
        self.scrollbar = Scrollbar(root, orient='vertical', command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.scrollbar.pack(side=tk.LEFT, fill='y')

        # Ağ trafiğini yavaşlatmak için kullanılacak gecikme süresi (saniye cinsinden)
        self.delay_time = 0.1

    def start_traffic_analysis(self):
        messagebox.showinfo("Ağ Trafik İzleme", "Ağ trafiği izleniyor. Kapatmak için pencereyi kapatın.")
        
        # Arka plan iş parçacığında trafik izleme işlemi başlatılır
        threading.Thread(target=self.capture_traffic).start()

    def capture_traffic(self):
        sniff(prn=self.packet_callback, store=0)

    def packet_callback(self, packet):
        if packet.haslayer('IP'):
            ip_src = packet['IP'].src
            ip_dst = packet['IP'].dst
            protocol = packet['IP'].proto

            packet_info = f"IP Packet: {ip_src} -> {ip_dst}, Protocol: {protocol}"

            if protocol == 6 and packet.haslayer('TCP'):
                # TCP paketi ise
                src_port = packet['TCP'].sport
                dst_port = packet['TCP'].dport
                packet_info += f", TCP Packet: {ip_src}:{src_port} -> {ip_dst}:{dst_port}"

            elif protocol == 17 and packet.haslayer('UDP'):
                # UDP paketi ise
                src_port = packet['UDP'].sport
                dst_port = packet['UDP'].dport
                packet_info += f", UDP Packet: {ip_src}:{src_port} -> {ip_dst}:{dst_port}"

            # Listbox'a ekleyin
            self.listbox.insert(tk.END, packet_info)
            # Listbox'u en son eklenen pakete odaklayın
            self.listbox.see(tk.END)

            # İşlemi yavaşlatmak için zaman gecikmesi ekle
            time.sleep(self.delay_time)

    def toggle_vpn_connection(self):
        if self.vpn_connected:
            self.disconnect_vpn()
        else:
            self.connect_vpn()

    def connect_vpn(self):
        try:
            # VPN bağlantısını burada kurabilirsiniz
            self.vpn_connected = True
            messagebox.showinfo("VPN Bağlantısı", "VPN bağlantısı başarıyla kuruldu.")
        except Exception as e:
            messagebox.showerror("Hata", f"VPN bağlantısı kurulurken bir hata oluştu: {str(e)}")

    def disconnect_vpn(self):
        try:
            # VPN bağlantısını burada sonlandırabilirsiniz
            self.vpn_connected = False
            messagebox.showinfo("VPN Bağlantısı", "VPN bağlantısı sonlandırıldı.")
        except Exception as e:
            messagebox.showerror("Hata", f"VPN bağlantısı sonlandırılırken bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#000000")
    app = TrafficAnalyzerApp(root)
    root.mainloop()
