# coding=utf-8
from aip import AipOcr

#输入百度云应用的APP_ID、API_KEY、SERET_KEY
AI='15164766'
AK='op8G4tpcaqL0mV0F7xcMvWFv'
SK='nMYrgi9Xfi47mtnnStIu0ZcAUV1XyIgM'

client=AipOcr(AI,AK,SK)

#读入测试图片
def get_file_content(filename='捕获.JPG'):
    with open(filename,'rb') as f:
        #'rb'表示读取二进制编码
        return f.read()

def identify_image():
    #可以定义参数变量：
    options={
        #定义图像方向
        'detect_direction':'True',
        #识别语言类型一般设置为'CHN_ENG'中英文混合
        'language_type':'CHN_ENG',  #应用于识别验证码，改为'ENG'
        }

    #调用通用文字识别接口
    image = get_file_content()
    result = client.basicGeneral(image, options)
    content = []
    for word in result['words_result']:
        content.append(word['words'])
    return '\n'.join(content)
    
def export_text(content):
    '''写出到txt文件方便查看'''
    os.remove('content.txt')
    with open('content.txt', 'w') as f:
        f.write(content)

if __name__ == '__main__':
    content = identify_image()
    with open('output.txt', 'w') as f:
        f.write(content)
    print('已输出文本。。。')
    
