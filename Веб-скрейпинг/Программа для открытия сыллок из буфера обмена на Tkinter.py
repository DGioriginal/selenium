import tkinter as tk
import webbrowser, pyperclip
# Функции для обработки нажатий

def on_button1_click():
    address = pyperclip.paste()
    webbrowser.open('google.com/maps/place/' + address)

def on_button2_click():
    address = pyperclip.paste()
    webbrowser.open('https://leetcode.com/problems/' + address)

def on_button3_click():
    webbrowser.open('Telegram.web')

# Создаем главное окно
root = tk.Tk()
root.title("Простая программа")
root.geometry("300x200")

# Создаем кнопки
button1 = tk.Button(root, text="Google Maps", command=on_button1_click)
button1.pack(pady=10)

button2 = tk.Button(root, text="LeecCode", command=on_button2_click)
button2.pack(pady=10)

button3 = tk.Button(root, text="Telegram", command=on_button3_click)
button3.pack(pady=10)

# Запускаем цикл событий
root.mainloop()