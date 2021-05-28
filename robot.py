from tkinter import *
from tkinter import ttk
import playsound
import speech_recognition as sr
from gtts import gTTS
from PIL import ImageTk,Image

def listen_user():
	##capture audio
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('Mr ROBOT IS LISTENING...') 
        audio = rec.listen(source ,phrase_time_limit=5)
    try:
        text=rec.recognize_google(audio,language='en-US')        
        return text
    except:
        print("Sorry,I had a problem")
        return 0
def talk(text,file):
    tts=gTTS(text=text,lang="en")
    filename ="%s.mp3"%file
    tts.save(filename)
    playsound.playsound(filename)
            
def contact():
    text_return  =listen_user()
    if text_return =="hello":
        talk("welcome to master robot what's your name",'p')
        phrase=listen_user()
        name=phrase.split()[-1]
        talk("welcome %s"%name,"f")
        talk("how old","r")
        phrase1=listen_user()
        old=phrase1.split()[-1]
        talk("ohh %s%name it's teen ","g")
root =Tk()

root.title("Mr Robots")
##root.
##("720x640")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack() 
##rbt = PhotoImage(file ="robot.png") 
rbt=ImageTk.PhotoImage(Image.open("robot.png")) 
##label(root ,image =rbt).place(x=0,y=0)
canvas.create_image(20, 20, anchor=NW, image=rbt)
b= Button(root,text ="Start",bd =5,comman =lambda:contact())
b.pack(side = 'top') 
root.mainloop()