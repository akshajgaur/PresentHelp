import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import os
import time
import pyaudio
import wave
import tkinter.font as tkFont
import speech_recognition as sr

window = tk.Tk()
window.geometry("700x466")
fontStyle = tkFont.Font(family="Montserrat", size=20)
w = Canvas(window, width=700, height=466)
w.pack()
w.create_line(550,-5,550,466, fill="magenta", width=7)
sec = 0
starting=True
trials = 0
answer = ""
f=open(""+answer+".txt","w+")
def new_project():
    minTime = 0
    maxTime = -1000
    answer = simpledialog.askstring("New Project", "Enter Project Name")
    while minTime>maxTime:
        minTime = simpledialog.askstring("Minimum Time", "What is the minimum time requirement?")
        maxTime = simpledialog.askstring("Maximum Time", "What is the maximum time requirement?")
    f.write("Name: "+answer + "\n")
    f.write(minTime +"\n")
    f.write(maxTime + "\n")
    trials = trials+1
def wpm():
    file = open("C:\Users\User\Documents\GitHub\PresentHelp\transcription.txt", "rt")
    data = file.read()
    words = data.split()
    return words

print('Number of words in text file :', len(words))
def transcribe():
    file = "test_recording.wav"
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)  # read the entire audio file                  
        f=open("transcription.txt","w+")
        f.write(r.recognize_google(audio))
    
    f.write(words + "\n")

    
def val(x):
    tk.Label(window,text = x).place(x=1000,y=20)

projects = tk.Button(window, 
               text="New Project", 
               width=15
                   ,height=5,command = new_project).place(x=50,y=50)

trials = tk.Button(window, 
               text="New Trial", 
               width=12
                   ,height=3,command = new_project).place(x=50,y=170)


graphs=tk.Label(window,text = "Graphs",font=fontStyle).place(x=580,y=10)





wpm = tk.Button(window, 
               text="WPM", 
               width=10
                   ,height=3,command = new_project).place(x=587,y=55)
filterWords = tk.Button(window, 
               text="Filter Words", 
               width=10
                   ,height=3,command = new_project).place(x=587,y=155)
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
        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
    def stop(self):
        self.st = 0
        transcribe()

guiAUD = RecAUD()

