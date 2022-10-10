import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import pywhatkit as kt

engine = pyttsx3.init('sapi5')
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                      #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)



voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)   # 0. male voice and 1. female voice
# print(voices[1].id)

# Varible data
Myname="Ani...."
anyWork="Do you have any other work ?  "
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
song_dir = "C:\\Users\\anjali.mishra\\Music\\audios"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning "+Myname)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+Myname)
    else:
        speak("Good Evening"+Myname)
    speak("I am Nia your assistant.")
    speak("How may I help you?")

def listenInstruction():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try :
        print("Recognizing....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

def main():
    speak("Welcome.....")
    wish()
    while True:
                query = listenInstruction()
                if query:
                    if 'what is' in query.lower():
                        speak('Searching ...')
                        result= wikipedia.summary(query, sentences = 3)
                        print(result)
                        speak("According to Wikipedia "+result)                       
                        speak(anyWork)

                    if 'wikipedia' in query.lower():
                        speak('Searching ...')
                        query = query.replace("wikipedia","")
                        result= wikipedia.summary(query, sentences = 3)
                        print(result)
                        speak("According to Wikipedia "+result)                       
                        speak(anyWork)

                    if 'search' in query.lower():
                        speak('Searching ...')
                        query = query.replace("search","")
                        result= kt.search(query)
                        
                    if 'open youtube' in query.lower():
                        url="youtube.com"
                        webbrowser.get(chrome_path).open(url)
                        # speak(anyWork)

                    if 'open google' in query.lower():
                        url="google.com"
                        webbrowser.get(chrome_path).open(url)
                        # speak(anyWork)

                    if 'open geeks for geek' in query.lower():
                        url="https://www.geeksforgeeks.org/"
                        webbrowser.get(chrome_path).open(url)
                        # speak(anyWork)

                    if 'mail' in query.lower():
                        url="https://mail.google.com/mail/u/0/#inbox"
                        webbrowser.get(chrome_path).open(url)
                        # speak(anyWork)

                    if 'music' in query.lower():
                        song=os.listdir(song_dir)
                        os.startfile(os.path.join(song_dir,song[0]))
                        # speak(anyWork)

                    if 'time' in query.lower():
                        t= datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"{Myname} the time is {t}")
                        # speak(anyWork)

                    if 'you doing' in query.lower():
                        speak("Nothing "+Myname)
                        speak("Just listening to you")
                        # speak(anyWork)

                    if 'your name' in query.lower():
                        speak("My name is Nia. I am your Assistant. ")
                        # speak(anyWork)

                    if 'how are you' in query.lower():
                        speak("I am fine")
                        speak("How are you "+Myname)
                        # speak(anyWork)

                    if 'stop' in query.lower():
                        speak("Ok Thank you. Have a good day")
                        break
main()

  
