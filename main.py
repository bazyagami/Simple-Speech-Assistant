import speech_recognition as sr
import pyttsx3
import string

r=sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)
    print("please say something")

    audio2=r.listen(source2)
    print("recognizing...")

    MyText=r.recognize_google(audio2,language='ta',show_all=True)


    SpeakText(MyText)
    print("did you say",MyText)

