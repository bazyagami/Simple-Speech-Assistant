import pyttsx3
import speech_recognition as sr
import webbrowser as wb


def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def fn_speech_recognition():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        SpeakText('Please say something:')

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)
        try:
            phrase = r.recognize_google(audio)
            SpeakText(f"you have said: {phrase} ")
            url = "https://www.google.com/search?q="
            search_url = url+phrase
            wb.open(search_url)

        except LookupError:
            print("repeat your request")
        else:
            SpeakText("Check your browser")


fn_speech_recognition()
