# encoding = utf-8
"""
    实现输入密码作为密钥，在明文和密文之间互换
    功能有点煞笔，再重构和具体化功能模块就好玩了。
"""
encrypt = input('明文转密文请输入1，反之输入2，按ENTER确定...\n')
#text = input('请输入原文本，按ENTER确定...\n')
lines = []
while True:
    tmp = input('请输入原文本，键入“quit”结束输入...\n')
    lines.append(tmp)
    if tmp == 'quit':
        break
text = '\n'.join(lines)
pw = input('请输入密钥，按ENTER确定...\n')

def generate(text, offset, encrypt=encrypt):
    char_list = list(text)
    code_list = []
    for char in char_list:
        code = ord(char)
        # 这个条件判断最好放在for循环后，影响速度；另外最好改为列表推倒式
        if encrypt == '1':
            code_list.append(code + int(offset))
        else:
            code_list.append(code - int(offset))
    output_text = ''.join([chr(c) for c in code_list])
    return output_text

if __name__ == "__main__":
    # 采用简单的密钥字符ASCII编码的均值生成密钥（极容易被破解）
    offset = sum([ord(p) for p in list(pw)]) / len(list(pw))
    encrypted = generate(text, offset)
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(encrypted)
    print('结果已输出至当前路径下的 output.txt 文件！')
