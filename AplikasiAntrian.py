import tkinter as tk
from tkinter import messagebox

# List untuk menyimpan data antrian
antrian = []

# Fungsi tambah antrian
def tambah_antrian():
    nama = entry_nama.get()
    if nama == "":
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
    else:
        antrian.append(nama)
        entry_nama.delete(0, tk.END)
        update_listbox()

# Fungsi panggil antrian
def panggil_antrian():
    if len(antrian) == 0:
        messagebox.showinfo("Info", "Antrian kosong")
    else:
        dipanggil = antrian.pop(0)
        messagebox.showinfo("Dipanggil", f"Antrian dipanggil: {dipanggil}")
        update_listbox()

# Update listbox
def update_listbox():
    listbox_antrian.delete(0, tk.END)
    for i, nama in enumerate(antrian, start=1):
        listbox_antrian.insert(tk.END, f"{i}. {nama}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Data Antrian")
root.geometry("400x400")

# Judul
label_judul = tk.Label(root, text="Aplikasi Data Antrian", font=("Arial", 14, "bold"))
label_judul.pack(pady=10)

# Input nama
label_nama = tk.Label(root, text="Masukkan Nama:")
label_nama.pack()

entry_nama = tk.Entry(root, width=30)
entry_nama.pack(pady=5)

# Tombol
btn_tambah = tk.Button(root, text="Tambah Antrian", width=20, command=tambah_antrian)
btn_tambah.pack(pady=5)

btn_panggil = tk.Button(root, text="Panggil Antrian", width=20, command=panggil_antrian)
btn_panggil.pack(pady=5)

# Listbox antrian
label_list = tk.Label(root, text="Daftar Antrian:")
label_list.pack(pady=5)

listbox_antrian = tk.Listbox(root, width=40, height=10)
listbox_antrian.pack()

# Menjalankan aplikasi
root.mainloop()