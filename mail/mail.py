from coverage import data
from .web import *
import tkinter as tk
from tkinter import scrolledtext
import os
import smtplib
import hashlib
import random
from email.mime.text import MIMEText
from email.header import Header
import time
import json
def hash(text):
    hashobj=hashlib.sha512()
    hashobj.update(text.encode("utf-8"))
    return hashobj.hexdigest()
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
def create(name,password,email,auth_code,server_email):
    check_number=[random.randint(100000,999999),time.time()]
    subject="IDE Login Auth Code"
    message = f"Your auth code is {check_number}"
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = Header("系统管理员", 'utf-8')
    msg['To'] = Header(email, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    server = smtplib.SMTP_SSL(email,465)
    server.login(server_email, auth_code)
    server.sendmail(server_email, [email], msg.as_string())
    server.quit()
    check=input("check number:")
    if time.time()-check_number[1]>300:
        return "error:1"
    if check==str(check_number[0]):
        if os.path.exists("user.json"):
            with open("user.json") as f:
                data = json.load(f)
                data[name]=hash(password))
                f.write(json.dumps(data))
        else:
            with open("user.json","w") as f:
                data={}
                data[name]=hash(password))
                f.write(json.dumps(data))
        return "success"
def login():
    name=input("name:")
    password=input("password:")
    if os.path.exists("user.json"):
        with open("user.json") as f:
            data = json.load(f)
            if name in data:
                if hash(password)==data[name]:
                    with open("login.txt",'w') as f:
                        f.write(name)
                    return True
                else:
                    return False
            else:
                return "error:2"
    else:
        return "error:1"