
import requests
import json
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",180)

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

def latestnews():
   

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    query= takeCommand().lower()

    if "business" in query:
        news("business")

    elif "entertainment" in query:
        news("entertainment")

    elif "health" in query:
        news("health")
    
    elif "technology" in query:
        news("technology")

    elif "sports" in query:
        news("sports")

    elif "entertainment" in query:
        news("entertainment")

    elif "science" in query:
        news("science")

def news(field):

    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d519081c328c4195abed7eea8a59e3e8",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d519081c328c4195abed7eea8a59e3e8",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=d519081c328c4195abed7eea8a59e3e8",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d519081c328c4195abed7eea8a59e3e8",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d519081c328c4195abed7eea8a59e3e8",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d519081c328c4195abed7eea8a59e3e8"
    }
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

