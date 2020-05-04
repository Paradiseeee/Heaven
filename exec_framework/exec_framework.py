# coding = utf-8
"""
    暂时完成不支持结构语句和多行注释的参数化功能。
    添加识别for循环、while循环、if语句、函数定义语句等功能。
"""

# 在test.py上进行测试，测试完成后打包成参数化函数


def run_file_with_kwargs(filepath, **kwargs):
    '''关键字参数需要根据被执行文件手动确定和输入'''
    # 解释文件 ==========================================================
    # 读取文件为文本列表
    with open(filepath, encoding='utf-8') as f:
        text = f.readlines()
    # 移除coding = utf-8（首行会出现奇怪字符，丢掉）
    for i, t in enumerate(text):
        if '#' in t and 'coding' in t and 'utf-8' in t and len(t)<20:
            text.pop(i)
    # 移除换行符
    for i, t in enumerate(text):
        text[i] = t.replace('\n', '')
    # 移除超参数定义行
    for i, t in enumerate(text):
        if 'def args' in t:
            start = i + 1
        if 'end args' in t:
            end = i - 1
    for _ in range((end - start + 1)):
        text.pop(start)   # 有多少行pop多少次，每次都pop开始行，下一行上移

    # 暂时不处理注释和空行（不会在遍历中移除列表元素，尴尬）

    # 将关键字参数列表解析为可执行文本
    for key, value in kwargs.items():
        text.insert(start, f'{key}={value}')

    # 执行部分 ============================================================
    for t in text:
        exec(t)

if __name__ == '__main__':
    abs_path = "C:/Program Files/Python37/Lib/site-packages/\
        my_module/exec_framework/test.py"
    run_file_with_kwargs('test.py', d=2, n=100)