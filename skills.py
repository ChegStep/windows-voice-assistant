import os, webbrowser, sys, requests, subprocess, pyttsx3, time
import random
import keyboard

import voices

engine = pyttsx3.init()
engine.setProperty('rate', 180)
import chat


def speaker(text):
    engine.say(text)
    engine.runAndWait()

def of_bot(answer, input_str = "", commands=None, data=None):
    voices.speaker_silero(random.choice(answer['say']))
    sys.exit()

def open_url(answer, input_str = "", commands=None, data=None):
    try:
        webbrowser.open(answer['parameters'] + input_str)
    except:
        voices.speaker_silero('Произошла ошибка, проверьте код')

def open_file(answer, input_str = "", commands=None, data=None):
    try:
        path_file = ''
        if os.path.isfile(answer['parameters']):
            path_file = os.path.abspath(answer['parameters'])
        if os.path.isdir(answer['parameters']):
            path_file = os.path.realpath(answer['parameters'])
        os.startfile(path_file)
    except:
        voices.speaker_silero('Произошла ошибка, проверьте код')


def weather(answer, input_str = "", commands=None, data=None):
    try:
        params = {'q': os.getenv('CITY_WEATHER'), 'units': 'metric', 'lang': 'ru', 'appid': os.getenv('WEATHER_API_KEY')}
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        w = response.json()
        voices.speaker_gtts(f"На улице {round(w['main']['temp'])} градусов")
    except:
        voices.speaker_silero('Произошла ошибка, проверьте код')

def passive(answer, input_str = "", commands=None, data=None):
    try:
        voices.speaker_silero(random.choice(answer['say']))
    except:
        voices.speaker_silero('Произошла ошибка, проверьте код')

def hotkey(answer, input_str = "", commands=None, data=None):
    try:
        pressed_keys = '+'.join(answer["parameters"])
        print(pressed_keys)
        keyboard.press_and_release(pressed_keys)
        time.sleep(0.1)

    except:
        voices.speaker_silero('Произошла ошибка, проверьте код')

def open_gpt(answer, input_str = "", commands=None, data=None):
    try:

        if os.getenv('CHATGPT') == '1' and any(trg in data for trg in commands[8]['triggers']):
            voices.speaker_silero("Уже включён")
            return
        elif os.getenv('CHATGPT') == '0' and any(trg in data for trg in commands[9]['triggers']):
            voices.speaker_silero("Уже выключен")
            return

        if os.getenv('CHATGPT') == '0':
            os.environ.update(CHATGPT=answer['parameters'])
        elif os.getenv('CHATGPT') == '1':
            os.environ.update(CHATGPT=answer['parameters'])
            chat.write_history()
        voices.speaker_silero('Готово')
    except:
        voices.speaker_silero('Ошибка запуска')
