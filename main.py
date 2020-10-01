import pyttsx3
from tkinter import *
import time
import wikipedia
import os
import winsound
import os.path
import webbrowser

# Root Configuration
root = Tk()
root.resizable(0,0)
root.geometry('500x600')
root.title('Wiki Bot')
color_background='#1F1B24'
root.configure(bg=color_background)


def change_look():
    """
        checks what color the root is already in and changes it!
        Activates When Theme in Menubar is clicked
    """
    global color_background
    if color_background == '#1F1B24':
        color_background='#121212'
        root.configure(bg=color_background)
        button2.configure(bg='#121212',fg='white',padx=10)
        button3.configure(bg='#121212',fg='white',padx=10)
        button.configure(bg='#121212',fg='white',padx=10)
        t.configure(bg='#121212',fg='white')
    elif color_background == '#121212':
        color_background='#1F1B24'
        root.configure(bg=color_background)
        button2.configure(bg='#1F1B24',fg='white',padx=10)
        button3.configure(bg='#1F1B24',fg='white',padx=10)
        button.configure(bg='#1F1B24',fg='white',padx=10)
        t.configure(bg='#1F1B24',fg='white',padx=5)
    
# Making a Menu Bar and assigning it to Root
menubar = Menu(root) 
menubar.add_command(label="Theme", command=change_look)  
root.config(menu=menubar)  
# Creting a text widget to hold the text from wikipedia
t = Text(root, height=20, width=40)
# Creating a scroll bar for the t text widget
scrollb = Scrollbar(root, command=t.yview)
scrollb.place()
t['yscrollcommand'] = scrollb.set


def open_browser():
    """
        Opens the browser with the link of the wikipedia page
        Activates when Read More On Wikipedia Button is Clicked
    """
    engine = pyttsx3.init()
    idd ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', idd)
    engine.save_to_file(' Opening browser', 'browser.mp3')
    
    engine.runAndWait()
    
    winsound.PlaySound('browser.mp3', winsound.SND_PURGE)
    ny2 = wikipedia.page(entry.get())
    webbrowser.open(ny2.url)
   
def speak():
    """
        starts engine and turns the text from wikipedia to speech
    """
    global engine
    global t
    try:
        ny2 = wikipedia.summary(entry.get(), sentences=5)
        t.delete(1.0, END)
        t.insert(INSERT,ny2,'a')
        t['font'] = ('Gill Sans', '12')
        t.pack()
        scrollb.place(relx=0.9, rely=0.5,anchor='c')

        engine = pyttsx3.init()
        ny = wikipedia.summary(entry.get(), sentences=5)
        engine.save_to_file(ny, 'test.mp3')
        
        engine.runAndWait()
        winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)
    except wikipedia.exceptions.DisambiguationError:
        
        ny2 = 'Please Enter A More Specefic Text'
        t.delete(1.0, END)
        t.insert(INSERT,ny2,'a')
        t['font'] = ('Gill Sans', '12')
        t.pack()
        engine = pyttsx3.init()
        
        engine.save_to_file(ny2, 'test.mp3')
        
        engine.runAndWait()
        winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)
    except wikipedia.exceptions.PageError:
        ny2 = 'There is no Article about the text You Entered'
        t.delete(1.0, END)
        t.insert(INSERT,ny2,'a')
        t['font'] = ('Gill Sans', '12')
        t.pack()
        engine = pyttsx3.init()
        
        engine.save_to_file(ny2, 'test.mp3')
        
        engine.runAndWait()
        winsound.PlaySound('test.mp3', winsound.SND_FILENAME | winsound.SND_ASYNC)

    button3['state']=ACTIVE
    button2['state']=ACTIVE
    
    
        

def stop():
    """
        Stops the voice of winsound
    """
    idd ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    if os.path.isfile('stop.mp3') :
        winsound.PlaySound('stop.mp3', winsound.SND_PURGE)
    else:
        engine = pyttsx3.init()
        engine.setProperty('voice', idd)
        engine.save_to_file(' Audio Stopped', 'stop.mp3')
        
        engine.runAndWait()
        
        winsound.PlaySound('stop.mp3', winsound.SND_PURGE)
    button2.configure(bg='#1F1B24',fg='white',padx=10,state=DISABLED)
        



# Widgets
entry = Entry(root)
entry.pack(pady=10)

button = Button(root,text='Click',command=speak)
button.pack(pady=10)
button2 = Button(root,text='stop',command=stop)
button2.pack(pady=10)
button3 = Button(root, text='Read More On WikiPedia', command=open_browser)
button3.place(relx=0.5,rely=0.95, anchor='c')
button2.configure(bg='#1F1B24',fg='white',padx=10,state=DISABLED)
button3.configure(bg='#1F1B24',fg='white',padx=10,state=DISABLED)
button.configure(bg='#1F1B24',fg='white',padx=10)
t.configure(bg='#1F1B24',fg='white',padx=5)   

# Making the Main Loop in order to start the program
root.mainloop()


