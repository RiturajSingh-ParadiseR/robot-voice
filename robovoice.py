import sys
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

    except:
        pass
    return command

def modulator():
    command = take_command()
    print(command)
    talk(command)

    if 'stop' in command:
        engine.say('bye')
        engine.runAndWait()
        engine.stop()
        sys.exit()

while True:
    modulator()
