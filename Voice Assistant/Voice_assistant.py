import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import wolframalpha
client = wolframalpha.Client('(your wolframalpha_id')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am zira Sir. Please tell me how may I help you")
    print("I am zira Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 20000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say again please...")
        speak("Say again please...")
        return ""
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your_mail_id', '(your_Password)')
    server.sendmail('Your_mail_id', to, content)
    server.close()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    sublime ="D:\\Sublime Text 3\\sublime_text"

    subprocess.Popen([sublime, file_name])

if __name__ == "__main__":
    wishMe()
    while True:
 
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            query = query.replace("on wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'hello' in query:
            speak("how are you?")
        elif 'goodbye' in query:
            speak("OK, bye sir")
            break

        elif 'youtube' in query:
            speak("Opening in youtube")
            query = query.replace("play","")
            query = query.replace("on youtube","")
            query = query.replace(" ", "")
            webbrowser.open("http://www.youtube.com/results?search_query=" + ''.join(query))
        elif 'search book on' in query:
            speak("searching!")
            query=query.replace("search book on","")
            webbrowser.open("https://libgen.is/search.php?req="+''.join(query))

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'google' in query:
            query = query.replace("search", "")
            query = query.replace("on google", "")
            webbrowser.open("https://www.google.com/search?q=" + ''.join(query))


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")


        elif 'play music' in query:
            music_dir = 'D:\\New folder\song\\00-Kaabil (2016)'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open sublime' in query:
            codePath = "D:\\Sublime Text 3\\sublime_text"
            os.startfile(codePath)
        elif 'open notepad' in query:
            notepad ="C:\\WINDOWS\\system32\\notepad"
            os.startfile(notepad)

        elif 'make a note' in query:
            speak("What would you like me to write down?")
            note_text = takeCommand()
            note(note_text)
            speak("I've made a note of that.")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recievers_mail_id"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
            except:
                speak('I don\'t know Sir! Google is smarter than me!')

                webbrowser.open('www.google.com')