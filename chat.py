import os, subprocess, string, openai, datetime
import voices

base_dialogue = [
    {'role': 'system', 'content': 'Ты ворчливый, грубо отвечающий короткими фразами собеседник.'},
    {'role': 'user', 'content': 'Привет, давай о чем нибудь поговорим?'},
    {'role': 'assistant', 'content': 'А оно мне надо? Ну давай, че там...'},
    {'role': 'user', 'content': 'Какие темы можешь предложить?'},
    {'role': 'assistant', 'content': 'Мне вообще всёравно, отстань от меня'},
]

messages = []
messages.extend(base_dialogue)

def write_history():
    len_base_dialogue = len(base_dialogue)

    if len(messages) == len_base_dialogue:
        return

    file_name = datetime.datetime.now()

    with open(f'temporary_files/gpt_history/{file_name}.txt', 'w', encoding='utf-8') as r:
        for i in messages[len_base_dialogue:]:
            r.writelines(i['content'] + '\n')


def new_dialogue():
    write_history()
    messages.clear()
    messages.extend(base_dialogue)


def clear_text(response):
    table = str.maketrans({'`': '', '(': '', ')': ' ', '@': 'at ', '_': ' '})
    response = response.translate(table)
    print(response)

    return response


def save_code(code):
    with open('temporary_files/codes/code.py', 'w', encoding='utf-8') as r:
        r.write(code)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    code_path = os.path.join(dir_path, 'temporary_files', 'code.py')

    subprocess.Popen(['python', '-m', 'idlelib', '-e', code_path])


def check_response(response):
    if '```' in response:
        parts = response.split('```')
        text = ''
        code = ''

        count = 1
        for i in parts:
            if count % 2 == 0:
                code += f'{i} \n'
            else:
                text += f'{i} \n'
            count += 1
        save_code(code)
        response = clear_text(text)
        return response
    else:
        response = clear_text(response)
        return response


def start_dialogue(text):
    try:
        # проверяем нужно-ли изменить значение env о том что есть активный диалог
        openai.api_key = os.getenv('OPENAI_API_KEY')

        # добавляем наш запрос в диалог
        messages.append({'role': 'user', 'content': text})
        # отправляем диалог
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        # берем ответ
        response = response['choices'][0]['message']['content']
        # добавляем ответ gpt в историию диалога
        messages.append({'role': 'assistant', 'content': response})

        # обработка ответа (проверка на наличие кода и очистка перед озвучкой)
        response = check_response(response)
        # обработаный текст ответа отправляем на озвучку
        return response
    except:
        voices.speaker_silero('Произошла ошибка, возможно, вы не добавили ваш токен')
