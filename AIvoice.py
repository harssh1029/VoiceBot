import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import requests
import wolframalpha
import json
from urllib.request import urlopen
import time
from PyQt5 import QtCore, QtGui, QtWidgets



engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Harsh")
    #time_()
    #date_()

    #greeting
    hour = datetime.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("good morning sir")
    elif(hour>=12 and hour<18):
        speak("good afternoon sir")
    elif(hour>=18 and hour<24):
        speak("good evening sir")
    else:
        speak("Good night sir")


    speak("How can I help you, today!")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()

    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        #all commands will be stored in lowercase letter

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching..")
            query = query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()

                speak("who is reciver")
                reciever = input("Enter receiver email:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has sent.')
            
            except Exception as e:
                print(e)
                speak("Unable to send email.")

        elif 'chrome' in query:
            speak("What do you want to search in chrome?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'youtube' in query:
            speak('What do you want to search in youtube')
            speack_Term = TakeCommand().lower()
            speak('Opening youtube')
            wb.open('https://www.youtube.com/results?search_query='+speack_Term)

        elif 'google' in query:
            speak("what do you want to search in google")
            search_Term = TakeCommand().lower()
            speak("Searching")
            wb.open('https://www.google.com/search?q='+search_Term)    

        elif 'go offline' in query:
            speak('Going offine sir')
            quit()

        elif 'write a note' in query:
            speak("What to write")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Should i incude date and time")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done . Note added")
            else:
                file.write(notes)
                speak("Done . Note added")

        elif 'show notes' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ec8b71f8c43b44ca89f5822027aacc93')
                data = json.load(jsonObj)
                i= 1

                speak("Here are some top headlines")
                for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1

            except Exception as e:
                print(str(e))


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")


        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'stop listening' in query:
            speak("for how many sec i should stop listening")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)


        




        


        

