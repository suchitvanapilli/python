import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import pywhatkit
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    # engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I am Jarvis. How may I help you?")
    elif hour < 18:
        speak("Good afternoon! I am Jarvis. How may I help you?")
    else:
        speak("Good evening! I am Jarvis. How may I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print("You said:", query)
    except Exception:
        speak("Sorry, I didn't catch that. Say it again.")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish()
    while True:
        query = take_command()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'play song' in query:
            song = query.replace('play song', '')
            pywhatkit.playonyt(song)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break
        elif 'open notepad' in query:
            os.system('notepad.exe')
