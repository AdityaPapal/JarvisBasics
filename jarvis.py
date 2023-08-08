import pyttsx3 
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5') # sapi5 :  Speech API
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!") 
    
    else: 
        speak("Good Evening!")

    speak("I am Jarvis Sir, How can i help you ?")


if __name__ == "__main__":
    wishme()
    # speak("Heey Bae") 