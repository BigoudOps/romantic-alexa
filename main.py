import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import psutil

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "french")
wikipedia.set_lang("fr")

def bye():
    talk('Ok, à bientot')
    from sys import exit
    exit(0)

def cpu():
    usage  = str(psutil.cpu_percent())
    talk("le cpu est actuellement à " + usage + " %")

def meteo():
     url = ''  # Open api link here
     res = requests.get(url)
     data = res.json()

     weather = data['weather'][0]['main']
     temp = data['main']['temp']
     wind_speed = data['wind']['speed']

     latitude = data['coord']['lat']
     longitude = data['coord']['lon']

     description = data['weather'][0]['description']
     talk('Temperature : {} degree celcius'.format(temp))
     print('Wind Speed : {} m/s'.format(wind_speed))
     print('Latitude : {}'.format(latitude))
     print('Longitude : {}'.format(longitude))
     print('Description : {}'.format(description))
     print('weather is: {} '.format(weather))
     talk('la météo est : {} '.format(description))


def pendule():
    time = datetime.datetime.now().strftime('%H:%M')
    talk('il est actuellement  ' + time)   


def talk(text):
    engine.say(text)
    engine.runAndWait()

def tanks():
    talk("de rien maitre")

def period():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        talk('Bonjour!')

    if currentH >= 12 and currentH < 18:
        talk('Bonne après-midi!')

    if currentH >= 18 and currentH != 0:
        talk('Bonsoir!')
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    time = datetime.datetime.now().strftime('%H:%M')
    talk("Je m'appelle Alexa , je suis la pour vous aider au quotidien")
    print(time + (" ") + str(date) + ("/") + str(month) + '/' + str(year))



def take_command():
    try:
        with sr.Microphone() as source:
            print("à l' écoute...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='fr-FR')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'joue' in command:
        song = command.replace('joue', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif "qui est" in command:
        person = command.replace("qui est", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "cpu" in command:
        cpu()
    elif "météo" in command:
        meteo()
    elif 'blague' in command:
        talk(pyjokes.get_joke('fr'))
    elif 'bye' in command:
        bye()
    elif "donne-moi l'heure" in command:
        pendule()
    elif "merci" in command:
        tanks()
    else:
        talk("répéter la commande svp")


if __name__ == '__main__':
    period()
    while True:
        run_alexa()
