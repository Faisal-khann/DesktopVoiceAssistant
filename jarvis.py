#Import Packages for working 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess

# Taking Voice for jarvis
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices) -> We Can find the type of voice whose present in sapi5
# set voices for jarvis
engine.setProperty("voice", voices[1].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. please tell me how may I help you")


def takeCommand():
    # it takes microphones input from the user and returns string outputs

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# Main Function
if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if (
            "wikipedia" in query
        ):  # if wikipedia found in the query then this block will be executed
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com") 

        elif "open camera" in query:
            subprocess.run('start microsoft.windows.camera:', shell=True)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\faisa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif "open notepad" in query:
           os.startfile("C:\\Users\\faisa\\Desktop\\Notepad.lnk")



        


        
