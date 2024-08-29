import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import requests
import datetime
import os
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        r.energy_threshold=350
        audio=r.listen(source,0,4)

    try:
        print("Understanding....")
        query=r.recognize_google(audio,language='en-in')
        print(f"you said : {query}")
    except  Exception as e :
        print("say that again")
        return 'None'
    return query

if __name__ == "__main__":
    while True :
        query= takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe 
            greetMe()

            while True : 
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir, you can call me anytime")
                    break 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "what is your name" in query:
                    speak("I am Jarvis")
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
    
                elif "temperature" in query:
                    search="temperature in chikkaballapur"
                    url=f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search="temperature in chikkaballapur"
                    url=f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "shutdown" in query:
                    speak("Good bye,sir")
                    exit()

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume downm sir")
                    volumedown()
                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    

                