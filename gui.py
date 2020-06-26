import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import os
import time
import pyaudio
import wave
import tkinter.font as tkFont
import speech_recognition as sr
import re
from collections import Counter
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import contextlib

window = tk.Tk()
window.geometry("700x466")
global x
fillerList = []
fontStyle = tkFont.Font(family="Montserrat", size=20)
fontStyle2 = tkFont.Font(family="Montserrat", size=16)
w = Canvas(window, width=700, height=466)
w.pack()
w.create_line(550,-5,550,466, fill="magenta", width=7)
sec = 0
starting=True
trials = 0
def new_project():
    trials = 0
    minTime = 0
    maxTime = -1000
    answer = simpledialog.askstring("New Project", "Enter Project Name")
    tile=tk.Label(window,text = answer+"",font=fontStyle,bg="cyan").place(x=50,y=2)
    while minTime>maxTime:
        minTime = simpledialog.askstring("Minimum Time", "What is the minimum time requirement?")
        maxTime = simpledialog.askstring("Maximum Time", "What is the maximum time requirement?")
    
    f=open("BitHacks.txt","w+")
    f.write(answer+ "\n")
    f.write(minTime +"\n")
    f.write(maxTime + "\n")
    trials = trials+1

def transcribe():
    x=0
    file = "BitHacks.wav"
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        said = ""
        try:
            said =r.recognize_google(audio)
        except:
            x+1
    time.sleep(10)
    f=open("transcription.txt","w+")
    f.write(said)
    
    fname = "transcription.txt"

    num_words = 0

    with open(fname, 'r') as f:
        for line in f:
            words = line.split()

            num_words += len(words)
    f=open("wpm.txt","w+")
    with contextlib.closing(wave.open('BitHacks.wav','r')) as t:
        frames =t.getnframes()
        rate = t.getframerate()
        duration = frames / float(rate)
    wp1 = num_words/(duration/60)
    f.write(str(wp1)+"\n")
    wanted = "like basically so"
    cnt = Counter()
    words = re.findall('\w+', open('transcription.txt').read().lower())
    for word in words:
        if word in wanted:
            cnt[word] += 1
    y = (cnt["like"])
    z=(cnt["basically"])
    a=(cnt["so"])
    total_filler = x+y+z+a
    filler=tk.Label(window,text = "Filter Words: "+str(total_filler+1),font=fontStyle2).place(x=230,y=150)
    wpm=tk.Label(window,text = "WPM: "+str(wp1),font=fontStyle2).place(x=230,y=190)
    time1=tk.Label(window,text = "Length: "+str(duration),font=fontStyle2).place(x=230,y=230)
    time2=tk.Label(window,text = "Length of Speech: "+"Good!",font=fontStyle2, bg="green").place(x=230,y=260)
    time3=tk.Label(window,text = "Speed (90-150 WPM): "+"Good!",font=fontStyle2, bg="green").place(x=230,y=300)
    filler_text =  open("filler.txt","w+")
    filler_text.write(str(total_filler)+"\n")
    time_text =  open("timings.txt","w+")
    time_text.write(str(duration)+"\n")
    fillerList.append(total_filler+1)
    
    
    
def fillerGraph():
    root= tk.Tk() 
    data2 = {'Trials': [1,2],
         'Filler Words': [4,3]
        }  
    df2 = DataFrame(data2,columns=['Trials','Filler Words'])
    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Trials','Filler Words']].groupby('Trials').sum()
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title('Trials Vs. Filler Words')
def wpmGraph():
    h= open('wpm.txt', 'r') 
  
    content = h.readlines() 
    list1 = []
    for line in content: 
          
              
        list1.append(line) 
  
    root= tk.Tk() 
    data2 = {'Trials': [1,2],
         'Filler Words': list1
        }  
    df2 = DataFrame(data2,columns=['Trials','Filler Words'])
    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Trials','Filler Words']].groupby('Trials').sum()
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title('Trials Vs. Filler Words')
def lengthGraph():
    root= tk.Tk() 
    data2 = {'Trials': [1,2],
         'Filler Words': [2,3]
        }  
    df2 = DataFrame(data2,columns=['Trials','Filler Words'])
    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Trials','Filler Words']].groupby('Trials').sum()
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title('Trials Vs. Filler Words')
    
def new_trial():
    trials=2
    
def val(x):
    tk.Label(window,text = x).place(x=1000,y=20)

projects = tk.Button(window, 
               text="New Project", 
               width=15
                   ,height=5,command = new_project).place(x=50,y=50)

trials = tk.Button(window, 
               text="New Trial", 
               width=12
                   ,height=3,command = new_trial).place(x=50,y=170)


graphs=tk.Label(window,text = "Graphs",font=fontStyle).place(x=580,y=10)





wpm = tk.Button(window, 
               text="WPM", 
               width=10
                   ,height=3,command = new_project).place(x=587,y=55)
filterWords = tk.Button(window, 
               text="Filter Words", 
               width=10
                   ,height=3,command = fillerGraph).place(x=587,y=155)
length = tk.Button(window, 
               text="Timings", 
               width=10
                   ,height=3,command = new_project).place(x=587,y=255)
class RecAUD:

    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        # Start Tkinter and set Title
        self.collections = []
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)




        # Start and Stop buttons
        self.strt_rec = tk.Button(window, width=10, padx=10, pady=5, text='Start Recording', command=lambda: self.start_record()).place(x=290, y=360)
        self.stop_rec = tk.Button(window, width=10, padx=10, pady=5, text='Stop Recording', command=lambda: self.stop()).place(x=290, y = 400)


        tk.mainloop()

    def start_record(self):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            window.update()
        stream.close()
        wf = wave.open('BitHacks.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
    def stop(self):
        self.st = 0
        transcribe()

guiAUD = RecAUD()

