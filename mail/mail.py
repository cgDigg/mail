from .web import *
import tkinter as tk
from tkinter import scrolledtext
import os
def push_mail(to_ip,message):
    push_tcp(to_ip,20263,message)
def ide_mail(test):
    root = tk.Tk()
    root.title("IDE")
    text_area = scrolledtext.ScrolledText(root, width=800, height=1000)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.INSERT, test)
    root.mainloop()
    return text_area.get("1.0", tk.END)
def ide_rewrite(name):
    if not os.path.exists(name):
        return "error:1"
    with open(name) as f:
        data = f.read()
    rewite=ide_mail(data)
    os.remove(name)
    with open(name,"w") as f:
        f.write(rewite)
    return "success"
def change_mail(name,to_ip,to_out_number,from_ip,from_out_number):
    if os.path.exists(name):
        return "error:1"
    ip=local_ip()
    with open(name) as f:
        data = f.read()
    message=f"{ip}{from_ip}{to_out_number}{from_out_number}{data}"
    if not os.path.exists(f"{name}.mail"):
        with open(f"{name}.mail","w") as f:
            f.write(message)
    else:
        os.remove(f"{name}.mail")
        with open(f"{name}.mail","w") as f:
            f.write(message)
