# -*- encoding: utf-8 -*-
"""
    实现输入密码作为密钥，在明文和密文之间互换
    使用一个较简单的加密逻辑，后续再进行优化
"""


def get_text():
    
    _type_ = input('选择输入类型：选择文件（1）| 直接输入（2）\n')
    if _type_ == '1':
        name = input('请输入文件路径')
        try:
            with open(name, 'r') as f:
                text = f.read()
        except:
            with open(name, 'r', encoding='gbk') as f:
                text = f.read()
    else:
        text = input('请输入原文本，按ENTER确定...\n')
        lines = []
        while True:
            tmp = input('请输入原文本，键入“quit”结束...\n')
            lines.append(tmp)
            if tmp == 'quit':
                break
        text = '\n'.join(lines)

        return text


def generate(text, func):

    # 加密逻辑在这里
    pw = input('请输入密钥：\n')
    offset = sum([ord(p) for p in list(pw)]) / len(list(pw))
    char_list = list(text)
    code_list = []
    for char in char_list:
        code = ord(char)
        # 这个条件判断最好放在for循环后，影响速度；另外最好改为列表推倒式
        if func == '1':
            code_list.append(code + int(offset))
        else:
            code_list.append(code - int(offset))
    output_text = ''.join([chr(c) for c in code_list])

    return output_text

if __name__ == "__main__":

    '''
    func = input('选择功能：明文转密文（1）| 密文转明文（2）\n')
    text = get_text()
    output = generate(text, func)
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(output)
    print('结果已输出到 output.txt！')
    '''
    print('此功能未上线，作者正在攻读密码学！')