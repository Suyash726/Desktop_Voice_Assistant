import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0])



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 5 and hour <12):
        speak("Good Morning")
    elif(hour>= 12 and hour < 18 ):
        speak("Good Afternoon")
    else:
        speak("Good Evening")        

    speak("Hello Suyash , How can I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return command
    



if __name__ == "__main__":
    wishme()
    
    while True:
        command = takeCommand().lower()


    if 'wikipedia' in command:
        speak('Searching Wikipedia....')
        command = command.replace("wikipedia","")
        result = wikipedia.summary(command,sentences = 2)
        speak("According to wikipedia")
        speak(result)
        print(result)
            
    elif 'youtube' in command:
        webbrowser.open("youtube.com")

    
    elif 'google' in command:
        webbrowser.open("google.com")    

    
    elif 'play music' in command:
        
        music = 'E:\\Best of Bands\\Ultimate_classics'
        songs = os.listdir(music)
        os.startfile(os.path.join(music,songs[random.randint(0,110)]))

