import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You:", command)
        return command

    except:
        return ""

speak("Hello! I am your Python Voice Assistant.")

while True:

    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)

    elif "date" in command:
        today = datetime.date.today()
        speak(str(today))

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't understand.")