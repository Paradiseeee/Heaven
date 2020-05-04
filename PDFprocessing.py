# coding = utf-8
"""
    模块中集成关于PDF处理的相关方法
"""
import PyPDF2 as pp

DOC = """
    * 说明：
        使用PyPDF2模块，集成一些常用的pdf操作，尤其是拆分与合并功能。并且生成
    用户友好的操作界面；
    * 操作提示：
        ·输入需要操作的pdf文件所在文件夹的绝对路径(可直接从资源管理器中复制)
        ·然后选择操作类型（包括拆分、合并两项）
        ·然后输入需要拆分或者合并的文件名（拆分的选项还需要给定页码）
        ·是否生成在与源文件相同的目录下？
        ·输入生成文件的路径
        ·最后输入生成文件的文件名（默认且只能保存到源文件的相同目录）
    """
# 源文件目录
PATH = input("请输入源文件所在目录（输入带盘符的绝对路径）：\n")

# 操作类型
TYPE = input("请选择操作的类型（输入 split 或 merge）：拆分PDF或合并PDF\n")

# 文件列表
if TYPE == "merge":
    temp = input("请输入要合并的文件（两个或多个，用逗号隔开）：\n")
    FILENAMES = [f.replace(' ', '') for f in temp.split(',')]

# 文件名以及提取的页数
if TYPE == "split":
    FILENAME = input("请输入要提取的文件名：\n")
    temp = input("请输入需要获取的页码（从第一页数起，用逗号隔开）：\n")
    PAGES = [int(p.replace(' ', '')) for p in temp.split(',')]

# 输出路径
temp = input("是否生成在与源文件相同的目录下？（yes / no）\n")
if temp == 'yes':
    OUTPUT_PATH = PATH
elif temp == 'no':
    OUTPUT_PATH = input("请输入新的路径（带盘符的绝对路径）：\n")

# 输出文件名
OUTPUT = input("请定义生成文件的文件名：\n")
if ".pdf" not in OUTPUT:
    OUTPUT += ".pdf"



def test():
    print("test")