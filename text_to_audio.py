from gtts import gTTS
import os
import tkinter as tk
from playsound import playsound
from tkinter import filedialog

win = tk.Tk()

def choosefile():
    global content
    file = filedialog.askopenfile(filetypes = [('Text files' , '*.txt ')])
    sFile = tk.Label(win,text = f'selected file : {file.name}')
    sFile.grid(row=1,column=0,columnspan=2)
    if file is not None:
        content = file.read()
    return content

def convert():
    text = content
    speech = gTTS(text=content,lang='en')
    speech.save(r'D:\VSgarage\text to speech.mp3')
    playsound(r'D:\VSgarage\text to speech.mp3')

label = tk.Label(win,text = 'select file')
label.grid(row=0,column=0,padx=8,pady=8)

button = tk.Button(win,text='Choose!!',command = choosefile)
button.grid(row=0,column=1,padx=8,pady=8)

button2 = tk.Button(win,text = 'Convert',command = convert)
button2.grid(row=2,column=0,padx=8,pady=8)

win.mainloop()
