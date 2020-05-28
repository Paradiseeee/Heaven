# -*- coding: utf-8 -*-
import json
from aip import AipOcr
from Heaven import __ROOT__


class TextIdentify():

    def __init__(self, pic_name='捕获.JPG', lang='CHN_ENG'):

        with open(__ROOT__+'/_UserKeys/baidu-ocr-key.json', 'r') as f:
            self.keys = json.loads(f.read())
        with open('捕获.JPG', 'rb') as f:
            self.img = f.read()
        
        self.options = {'detect_direction': 'True', 'language_type': lang}
        self.client = None


    def identify_image(self, keys=None):
        
        if keys:
            self.keys = keys
        self.client = AipOcr(
            self.keys['API_ID'], 
            self.keys['API_KEY'],
            self.keys['SECRET_KEY'])
        
        result = self.client.basicGeneral(self.img, self.options)
        content = []
        for word in result['words_result']:
            content.append(word['words'])
        return '\n'.join(content)


if __name__ == '__main__':

        content = TextIdentify().identify_image()
        with open('output.txt', 'w') as f:
            f.write(content)
        print('已输出文本。。。')
    
