import os, sys, json, keyboard
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox
from PySide6.QtGui import *
from PySide6 import QtCore, QtGui, QtWidgets

import main
from design import *
import setting

class SettWidget(QMainWindow):
    def __init__(self):
        super(SettWidget, self).__init__()
        #settings windows
        self.setWindowIcon(QIcon('icons/assist.svg'))
        self.ui_settings = Ui_MainWindow()
        self.ui_settings.setupUi(self)
        #settings functions
        self.ui_settings.btnInstruction.clicked.connect(self.btn_show_instructions)
        self.ui_settings.btnAllCommands.clicked.connect(self.btn_all_commands)
        #tab 1
        self.ui_settings.btnSaveExt.clicked.connect(self.btn_save_external_sett)
        #tab 2
        self.ui_settings.btnChooseFile.hide()
        self.ui_settings.lblFile.hide()
        self.ui_settings.lineFile.hide()
        self.ui_settings.btnAddCommand.clicked.connect(self.btn_add_command)
        self.ui_settings.btnAddHotkey.clicked.connect(self.btn_add_hotkey)
        self.ui_settings.cmbAction.currentIndexChanged.connect(self.cmbAction_Changes)
        self.ui_settings.btnChooseFile.clicked.connect(self.btn_choose_file)
        self.ui_settings.cmbAction.setCurrentIndex(3)
        #tab 3
        self.ui_settings.btnSaveTok.clicked.connect(self.btn_save_tokens)

    def action_show_hide(self, action_show_hide):
        self.open_settings()
        if self.isVisible():
            action_show_hide.setText('Открыть окно настроек')
            self.hide()
        else:
            action_show_hide.setText('Закрыть окно настроек')
            self.showNormal()

    def micro_off_on(self, micro_off_on):
        if os.getenv('STATUS_MICRO') == "0":
            os.environ.update(STATUS_MICRO="1")
            micro_off_on.setText('Выключить микрофон')
        elif os.getenv('STATUS_MICRO') == "1":
            os.environ.update(STATUS_MICRO="0")
            micro_off_on.setText('Включить микрофон')

    def open_settings(self):
        #Внешние настройки / Tab 1
        self.ui_settings.lineNamesAssist.setText(os.getenv('ASSIST_NAME'))
        self.allItems = [self.ui_settings.cmbVoice.itemText(i) for i in range(self.ui_settings.cmbVoice.count())]
        self.ui_settings.cmbVoice.setCurrentIndex(self.allItems.index(os.getenv('SPEAKER_NAME')))
        #Токены/ Tab 3
        self.ui_settings.lineWeatherTok.setText(os.getenv('WEATHER_API_KEY'))
        self.ui_settings.lineGPTTok.setText(os.getenv('OPENAI_API_KEY'))
        self.ui_settings.linetCity.setText(os.getenv('CITY_WEATHER'))

    def btn_show_instructions(self):
        os.startfile(os.getcwd() + '/temporary_files/txt_files/instruction.txt')

    def btn_all_commands(self):
        os.startfile(os.getcwd() + '/temporary_files/txt_files/cmnds.json')


    def btn_save_external_sett(self):
        with open('temporary_files/txt_files/config.txt', 'r', encoding='utf-8') as f:
            old_data = f.readlines()

        old_data[2] = 'ASSIST_NAME: ' + self.ui_settings.lineNamesAssist.text() + '\n'
        old_data[3] = 'SPEAKER_NAME: ' + self.allItems[self.ui_settings.cmbVoice.currentIndex()] + '\n'

        with open('temporary_files/txt_files/config.txt', 'w', encoding='utf-8') as f:
            f.writelines(old_data)
        setting.config()

    def btn_add_command(self):
        action = self.ui_settings.cmbAction.currentText()
        lineNameCmnd = self.ui_settings.lineNameCmnd.text()
        lineVoiceCmnd = self.ui_settings.lineCommand.text().lower()
        lineAnswer = self.ui_settings.lineAnswer.text()
        lineParams = ""
        if action == 'open_url' or action == 'open_file':
            lineParams = self.ui_settings.lineFile.text()
        elif action == 'hotkey':
            lineParams = self.ui_settings.lineHotkey.text().split('+')

        new_cmd = {"command": f"{lineNameCmnd}",
             "make":f"{action}",
             "parameters": lineParams,
             "say": lineAnswer.split(' | '),
             "triggers": lineVoiceCmnd.split(' | ')
             }
        self.write_json(new_cmd)

        self.ui_settings.lineCommand.setText('')
        self.ui_settings.lineAnswer.setText('')
        self.ui_settings.lineFile.setText('')
        self.ui_settings.lineHotkey.setText('')
        self.ui_settings.lineNameCmnd.setText('')

    def write_json(self, new_data, filename = os.getcwd() + '/temporary_files/txt_files/cmnds.json'):
        with open(filename, 'r+', encoding='utf-8') as file:
            file_data = json.load(file)
            file_data.append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def btn_choose_file(self):
        nameFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите .exe файла, который будет запускаться')
        self.ui_settings.lineFile.setText(nameFile[0].replace('/','\\\\'))
        return nameFile[0].replace('/','\\\\')

    def btn_add_hotkey(self):
        hotkey = self.ui_settings.lineHotkey.text().split('+')
        if hotkey[0] == '':
            hotkey.pop(0)
        if keyboard.is_pressed(keyboard.read_key()):
            hotkey.append(keyboard.read_key())
        self.ui_settings.lineHotkey.setText('+'.join(hotkey))

    def btn_save_tokens(self):
        with open('temporary_files/txt_files/config.txt', 'r', encoding='utf-8') as f:
            old_data = f.readlines()

        old_data[0] = 'WEATHER_API_KEY: ' + self.ui_settings.lineWeatherTok.text() + '\n'
        old_data[1] = 'OPENAI_API_KEY: ' + self.ui_settings.lineGPTTok.text() + '\n'
        old_data[4] = 'CITY_WEATHER: ' + self.ui_settings.linetCity.text() + '\n'

        with open('temporary_files/txt_files/config.txt', 'w', encoding='utf-8') as f:
            f.writelines(old_data)
        setting.config()

    def cmbAction_Changes(self):
        if self.ui_settings.cmbAction.currentIndex() == 0:
            self.elementsHotkey_hide()
            self.ui_settings.btnChooseFile.hide()
            self.elementsFile_show()
            self.ui_settings.lblFile.setText('Ссылка')
        elif self.ui_settings.cmbAction.currentIndex() == 1:
            self.elementsHotkey_hide()
            self.ui_settings.btnChooseFile.show()
            self.elementsFile_show()
            self.ui_settings.lblFile.setText('Файл')
        elif self.ui_settings.cmbAction.currentIndex() == 2:
            self.elementsHotkey_show()
            self.elementsFile_hide()
            self.ui_settings.btnChooseFile.hide()
        else:
            self.elementsHotkey_hide()
            self.elementsFile_hide()
            self.ui_settings.btnChooseFile.hide()

    def elementsFile_hide(self):
        self.ui_settings.lblFile.hide()
        self.ui_settings.lineFile.hide()

    def elementsFile_show(self):
        self.ui_settings.lblFile.show()
        self.ui_settings.lineFile.show()

    def elementsHotkey_hide(self):
        self.ui_settings.lblHotkey.hide()
        self.ui_settings.lineHotkey.hide()
        self.ui_settings.btnAddHotkey.hide()

    def elementsHotkey_show(self):
        self.ui_settings.lblHotkey.show()
        self.ui_settings.lineHotkey.show()
        self.ui_settings.btnAddHotkey.show()

def app_start():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    mainApp = SettWidget()
    tray = QSystemTrayIcon(QIcon('icons/assist.svg'))
    menu = QMenu()

    action_show_hide = QAction("Открыть окно настроек")
    action_show_hide.triggered.connect(lambda: mainApp.action_show_hide(action_show_hide))
    menu.addAction(action_show_hide)
    micro_off_on = QAction("Выключить микрофон")
    micro_off_on.triggered.connect(lambda: mainApp.micro_off_on(micro_off_on))
    menu.addAction(micro_off_on)

    exit = QAction("Закрыть")
    exit.triggered.connect(lambda: sys.exit())
    menu.addAction(exit)
    tray.setToolTip("Настройки ассистента")
    tray.setContextMenu(menu)
    tray.show()
    sys.exit(app.exec())