import tkinter as tk
from tkinter import messagebox, simpledialog
import random


class MatkolikApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matkolik - Eğlenceli Matematik Dünyası 🚀")
        # Pencere boyutunu biraz daha genişletelim
        self.root.geometry("500x650")
        self.root.configure(bg="#E3F2FD")  # Açık mavi arka plan

        # Başlık
        self.title_label = tk.Label(root, text="MATKOLİK 🌈", font=("Comic Sans MS", 30, "bold"),
                                    bg="#E3F2FD", fg="#1565C0")  # Koyu Mavi Başlık
        self.title_label.pack(pady=30)

        # Buton İsimleri ve Fonksiyonları
        menu_items = [
            ("🔢 Süper Hesap Makinesi", self.hesap_makinesi),
            ("⚖️ Tek mi? Çift mi?", self.tek_cift_kontrolu),
            ("💎 Gizemli Asal Sayılar", self.asal_sayi_kontrolu),
            ("📝 Harf Saymaca", self.harf_sayisi),
            ("🎯 Sayı Tahmin Oyunu", self.sayi_tahmin),
            ("🏆 Matematik Yarışması", self.basit_matematik)
        ]

        # --- DÜZELTME BURADA ---
        for text, command in menu_items:
            # Mac'te butonların içinin boyanması zordur.
            # Bu yüzden highlightbackground kullanarak kenarları boyuyoruz
            # ve fg (yazı rengini) KOYU MAVİ yapıyoruz ki okunsun.
            btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), width=25,
                            bg="white",  # Arka plan
                            fg="#0D47A1",  # YAZI RENGİ: Koyu Lacivert (Okunması için)
                            highlightbackground="#E3F2FD",  # Mac için kenar rengi uyumu
                            activebackground="#BBDEFB",  # Tıklanınca alacağı renk
                            cursor="hand2", command=command)
            btn.pack(pady=8)

        # Çıkış Butonu
        # Mac'te kırmızı butonu göstermek için yazı rengini kırmızı yapıyoruz
        exit_btn = tk.Button(root, text="❌ Oyunu Kapat", font=("Arial", 12, "bold"),
                             fg="#D32F2F", bg="#FFCDD2",  # Kırmızı yazı
                             highlightbackground="#E3F2FD",
                             command=root.quit)
        exit_btn.pack(pady=40)

    # --- Fonksiyonlar (Aynı kalıyor) ---

    def hesap_makinesi(self):
        try:
            n1 = simpledialog.askfloat("Sayı 1", "İlk sayıyı gir bakalım:")
            if n1 is None: return
            op = simpledialog.askstring("Operatör", "Ne yapalım? (+, -, *, /)")
            if op is None: return
            n2 = simpledialog.askfloat("Sayı 2", "İkinci sayıyı gir:")
            if n2 is None: return

            res = 0
            if op == '+':
                res = n1 + n2
            elif op == '-':
                res = n1 - n2
            elif op == '*':
                res = n1 * n2
            elif op == '/':
                res = n1 / n2 if n2 != 0 else "Tanımsız!"
            else:
                res = "Geçersiz işlem!"

            messagebox.showinfo("Sonuç", f"Bulduğum sonuç: {res} ✨")
        except:
            pass

    def tek_cift_kontrolu(self):
        try:
            sayi = simpledialog.askinteger("Sayı Gir", "Sayıyı yaz, sihrimi göstereyim:")
            if sayi is None: return
            durum = "Çift 🍎" if sayi % 2 == 0 else "Tek 🍏"
            messagebox.showinfo("Sonuç", f"{sayi} sayısı {durum} bir sayıdır!")
        except:
            pass

    def asal_sayi_kontrolu(self):
        try:
            sayi = simpledialog.askinteger("Asal mı?", "Sayıyı gir:")
            if sayi is None: return
            if sayi < 2:
                messagebox.showwarning("Hoppala", "En küçük asal sayı 2'dir! 🧐")
                return
            is_prime = all(sayi % i != 0 for i in range(2, int(sayi ** 0.5) + 1))
            msg = "Yaşasın, bu bir ASAL sayı! 🌟" if is_prime else "Bu bir asal sayı değil. 😅"
            messagebox.showinfo("Asal Kontrolü", msg)
        except:
            pass

    def harf_sayisi(self):
        metin = simpledialog.askstring("Metin Gir", "Bir cümle yaz:")
        if metin is None: return
        harfler = sum(1 for c in metin if c.isalpha())
        messagebox.showinfo("Harf Sayacı", f"Vay canına! Yazında tam {harfler} tane harf var! ✍️")

    def sayi_tahmin(self):
        hedef = random.randint(1, 100)
        tahmin = -1
        while tahmin != hedef:
            tahmin = simpledialog.askinteger("Tahmin Et", "1-100 arası bir sayı tuttum:")
            if tahmin is None: break
            if tahmin == 0: break
            if tahmin < hedef:
                messagebox.showinfo("İpucu", "Daha BÜYÜK bir sayı! ⬆️")
            elif tahmin > hedef:
                messagebox.showinfo("İpucu", "Daha KÜÇÜK bir sayı! ⬇️")

        if tahmin == hedef:
            messagebox.showinfo("Tebrikler!", "Bildin! Harikasın! 🎉")

    def basit_matematik(self):
        skor = 0
        for i in range(3):
            n1, n2 = random.randint(1, 10), random.randint(1, 10)
            cevap = simpledialog.askinteger("Yarışma", f"{n1} + {n2} kaç eder?")
            if cevap is None: return
            if cevap == n1 + n2:
                skor += 1
                messagebox.showinfo("Doğru", "Süpersin! ✅")
            else:
                messagebox.showerror("Yanlış", f"Üzgünüm, cevap {n1 + n2} olmalıydı. ❌")
        messagebox.showinfo("Oyun Bitti", f"Yarışmayı {skor} puanla bitirdin! 🏆")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatkolikApp(root)
    root.mainloop()