import json
import queue
import os
import sys
import time

import sounddevice as sd
import vosk

import voices
import chat
from threading import Thread
import app
import skills

q = queue.Queue()

model = vosk.Model('model_small')
close_flag = True

try:
    device = sd.default.device = 1, 4
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
except:
    voices.speaker_silero('Включи микрофон!')
    sys.exit(1)

def callback(indata, frames, time, status):
    if os.getenv('STATUS_MICRO') == "0":
        pass
    elif os.getenv('STATUS_MICRO') == "1":
        q.put(bytes(indata))

def recognize(data):
    if len(data) < 7:
        return
    with open(os.getcwd() + '/temporary_files/txt_files/cmnds.json', "r", encoding='utf-8') as read_file:
        commands = json.load(read_file)

    triggers = []
    for trigger in [ind['triggers'] for ind in commands]:
        triggers.append(trigger)

    assist_name = list(set(os.getenv('ASSIST_NAME').split(',')).intersection(set(data.split())))

    if not assist_name:
        if os.getenv('CHATGPT') != '1':
            return
        voices.speaker_silero(chat.start_dialogue(data))
        return

    all_triggers = []
    answer = None
    input_str = ""

    data = data.replace(f'{assist_name[0]} ','')
    for trigger in triggers:
        all_triggers.extend(trigger)
    if any(trg in data for trg in all_triggers):
        for trg in triggers:
            for trgIn in trg:
                if data.startswith(trgIn):
                    answer = commands[triggers.index(trg)]
                    input_str = data.split(trgIn)[1]
    else:
        voices.speaker_silero("Команда не распознана")
        return
    func_name = answer['make']
    exec('skills.' + func_name + f'{answer, input_str, commands, data}')

def main():
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data)

if __name__ == '__main__':
    p1 = Thread(target=main,daemon=True)
    p1.start()
    app.app_start()