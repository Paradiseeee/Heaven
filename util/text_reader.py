# -*- coding: utf-8 -*-
from os import system
from gtts import gTTS

class Reader():
    '''reading input text in different language'''

    def __init__(self, mode=1, lang='en'):

        # 文本读取模式
        self.MODE = 'input' if mode == 1 else 'file'
        # 语言选项
        self.LANG = lang


    def get_text(self):

        if self.MODE == 'input':

            text = []
            print('\n>>> 请输入文本，输入[q]提交：\n')
            while True:
                t = input(':')
                if t == 'q':
                    break
                else:
                    text.append(t)
        elif self.MODE == 'file':
            path = input('\n>>> 请输入文件路径：\n')
            with open(path, 'r') as f:
                text = f.read()
            text = text.split('\n')
        
        return text


    def generate_voice(self, text):

        print('\n>>> 正在处理，请稍等...\n')
        speech = gTTS(text=' '.join(text), lang=self.LANG, slow=False)
        speech.save('output.mp3')
        print('\n>>> 正在打开音频文件...')
        system('start output.mp3')


    def run(self):

        print('\n' + '-'*72)
        print('欢迎使用文本朗读'.center(64, ' '))
        print('-'*72 + '\n')

        mode = input('\n>>> 请选择文本来源：输入(1) | 文件(2)\n')
        lang = input('\n>>> 请选择语言：中文(1) | 英文(2)\n')
        self.LANG = 'zh-CN' if lang == '1' else 'en'
        self.MODE = 'input' if mode == '1' else 'file'
        text = self.get_text()
        self.generate_voice(text)


if __name__ == "__main__":

    try:
        Reader().run()
    except:
        print('[WinError 10060] 无法连接到 translate.google.com！')