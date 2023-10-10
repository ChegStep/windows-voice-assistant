import os

CFG = {
    'CHATGPT': '0',
}

def config():
    with open('temporary_files/txt_files/config.txt', "r", encoding='utf-8') as file:
      lines = file.read().splitlines()

    for line in lines:
      key,value = line.split(': ')
      CFG.update({key:value})

    for key, value in CFG.items():
        os.environ[key] = value

config()