import datetime
import webbrowser
import os
import pyttsx3
import wikipedia
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) # To get the male voice 
# print(voices[1].id) # To get the female voice 

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
speak("I am Jarvis sir, speed 1 zettabyte, memory 1 terrabyte. How can I help you?")

def takecommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query} \n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vedanshgupta606@gmail.com', '2444666668888888')
    server.sendmail('vedanshgupta606@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    if 1:
        query = takecommands().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("query", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query :
            webbrowser.open("youtube.com")

        elif "open google" in query :
            webbrowser.open("google.com")

        elif "open stackoverflow" in query :
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = 'C:\\Users\\91936\\Music\\Free YouTube Downloader'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            tym = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, the time is {tym}")
            print(tym)

        elif "open code" in query:
            codePath = "C:\\Users\\91936\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)

        elif "send mail" in query :
            try:
                speak("What should I say ?")
                content = takecommands()
                to = "kaushkigupta5400@gmail.com"
                sendEmail(to, content)
                speak("The email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry sir. I am unable to send this email")