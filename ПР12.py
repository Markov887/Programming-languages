import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_info():
    name = entry.get()
    if not name:
        return
    
    try:
        r = requests.get(f"https://api.github.com/repos/{name}")
        r.raise_for_status()
        data = r.json()
        owner = data['owner']
        result = {
            'company': owner.get('company'),
            'created_at': owner.get('created_at'),
            'email': owner.get('email'),
            'id': owner.get('id'),
            'name': owner.get('login'),
            'url': owner.get('url')
        }      
        with open('repo_data.json', 'w') as f:
            json.dump(result, f, indent=4)
            
        tk.messagebox.showinfo("Готово", "Данные сохранены в repo_data.json")
    except:
        tk.messagebox.showerror("Ошибка", "Репозиторий не найден")

root = tk.Tk()
root.title("GitHub Info")
root.geometry("300x150")

tk.Label(root, text="Имя репозитория:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Получить данные", command=get_info).pack(pady=20)

root.mainloop()

