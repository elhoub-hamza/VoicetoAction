import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os

# define variable name engine
engine = pyttsx3.init()

# Voice option and speak rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voice[1] = male , voice[0] = female

# Voice speak rate
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


# Voice Speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # speak("This is the python assistant tutorial")


# Time Function
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is :")
    speak(Time)  # time()


# Date Function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is :")
    speak(date)
    speak(month)
    speak(year)  # date()


# Greet Us Function
def wishme():
    speak("welcome back sur !")
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    elif 18 <= hour <= 24:
        speak("Good afternoon")
    else:
        speak("Good night")

    speak("Hamza at your service. How I can help you ?")


# wishme()


# Take Command Function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, 'en=US')
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"

        return query
# takeCommand()

#send email function
def sendmail(to, content):
    server = smtplib.SMTP('smtp.mail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("text@gmail.com", to, content)
    server.close()



# The main function
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()

        # Wikipedia Search
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence=2)
            speak(result)

        # Send email
        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        # Chrome Search
        elif "search in chrome" in query:
            speak("what should i search?")
            chromepath = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")

        #Logout ,Shutdown, Restart Function
        elif "log out" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #Play music
        elif "play songs" in query:
            songs_dir = "F:\musics\music"
            songs = os.listdir(songs_dir)
            os.statfile(os.path.join(songs_dir,songs[0]))

        # Remember function
        elif "remember that" in query:
            speak("what shoud i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        # Reminder function
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that"+remember.read())