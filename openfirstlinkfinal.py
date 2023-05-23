from bs4 import BeautifulSoup
import requests, json, lxml
import webbrowser as wb
import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)           #0-male 1-female


path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        SpeakText("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        SpeakText("Good Afternoon Sir !")

    else:
        SpeakText("Good Evening Sir !")

    asstname = ("mark")
    SpeakText("I am your Assistant")
    SpeakText(asstname)


def speechrec():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        SpeakText("what should i open")
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        try:
            phrase=r.recognize_google(audio)
            SpeakText(f"You have said {phrase}")
            params = {
                'q': phrase,  # search query
                'gl': 'in',  # country to search from
                'hl': 'en',  # language
            }

            html = requests.get('https://www.google.com/search', headers=headers, params=params).text
            soup = BeautifulSoup(html, 'lxml')

            data = []

            for result in soup.select('.tF2Cxc'):
                title = result.select_one('.DKV0Md').text
                link = result.select_one('.yuRUbf a')['href']
                SpeakText(f"opening {title}")


                try:
                    snippet = result.select_one('#rso .lyLwlc').text


                except:
                    snippet = None
                return wb.get(path).open(link)


                data.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet,
                })

                SpeakText("here's your request")

        except LookupError:
            SpeakText("please repeat your request")


wishMe()
speechrec()
