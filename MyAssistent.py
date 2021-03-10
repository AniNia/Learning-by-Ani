import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
Myname="Ani...."

def mail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.startls()
    server.login('mailid','pwd')
    server.sendmail('mail',pwd)
    server.close()
def speek(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speek("Good Morning "+Myname)
    elif hour>=12 and hour<18:
        speek("Good Afternoon"+Myname)
    else:
        speek("Good Evening"+Myname)
    speek("I am your Nia")
    speek("How may I help you?")
def listenInstruction():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try :
        print("Recognizing....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query
def main():
    speek("Welcome.....")
    wish()
    while True:
                query = listenInstruction()
                if query:
                    if 'wikipedia' in query.lower():
                        speek('Searching wikipedia...')
                        query = query.replace("wikipedia","")
                        result= wikipedia.summary(query, sentences = 3)
                        speek(result)
                        print(result)
                        
                    if 'open youtube' in query.lower():
                        url="youtube.com"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)

                    if 'open google' in query.lower():
                        url="google.com"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)

                    if 'open geeks for geek' in query.lower():
                        url="https://www.geeksforgeeks.org/"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)

                    if 'open mail' in query.lower():
                        url="https://mail.google.com/mail/u/0/#inbox"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)

                    if 'mail' in query.lower():
                        url="https://mail.google.com/mail/u/0/#inbox"
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open(url)

                    if 'music' in query.lower():
                        song_dir = "C:\\Users\\Anjali\\Music\\audio"
                        song=os.listdir(song_dir)
                        os.startfile(os.path.join(song_dir,song[11]))

                    if 'time' in query.lower():
                        t= datetime.datetime.now().strftime("%H:%M:%S")
                        speek(f"{Myname} the time is {t}")

                    if 'you doing' in query.lower():
                        speek("Nothing "+Myname)
                        speek("Just listening to you")

                    if 'you doing' in query.lower():
                        speek("Nothing "+Myname)
                        speek("Just listening to you")

                    if 'how are you' in query.lower():
                        speek("I am fine")
                        speek("How are you"+Myname)
                    if 'stop' in query.lower():
                        speek("As your wish")
                        break
main()