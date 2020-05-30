# Heaven

## 简介

本仓库集成了一些常用功能，包括数据科学处理过程、日常工作效率提升，以及一些有趣的功能。目前正在开发中，如果效果良好将在以后继续完善，打造一个数据科学专用工具箱。数据科学包括多个维度，具体针对哪方面的问题...暂时还没想好。

安装方法：

```bash
cd %PYTHON_HOME%/Lib/
git clone https://github.com/paradiseeee/heaven
```

*PS：本人小白，纯属瞎搞，路过的朋友如果感兴趣欢迎交流指教*


## 详情

### Heaven -- 根目录，数据分析工具，导入所有类和对象

- <strong><i>__init__.py</i></strong>
    - 功能：注意到会增加 import 用时
        - 直接引入所有脚本中可复用的类对象
        - 显示 module 信息，包括 LISENCE、DOC-STRING、具体内容
    - 状态：同步更新
    - 使用： `python -m Heaven.__init__`

- <strong><i>mysql_helper.py</i></strong>
    - 功能：将 MySQL 终端的常用功能集成到 Python 环境，解决变量交互问题
    - 状态：完成
    - 使用： `from Heaven import MysqlHelper` ； `MysqlHelper??`

<!-- usage update below undone -->

- <string><i>其他文件</i></strong>
    - _DOCS: 除了 User Keys 以及脚本文件的其他文本文件；
    - _UserKeys: 用户的密钥配置，例如 API 密钥、数据库密钥等；
    - _UserKeys_PublicFormat: 脱敏后的 _UserKeys，用来参考密钥配置；
    - update_python_lib.bat: 更新 %PYTHON_HOME%\LIB 的批处理；
    - LISENCE
    - .gitignore
    - .gitattributes
    - README.md

### [***Heaven.util***](./util) -- 其他乱七八糟的小工具

<!-- <details>
    <summary>展开<strong><em>模块列表</em></strong></summary> -->

- <strong><i>chinese_encoding.py</i></strong>
    - 功能：快速设置 matplotlib 绘图中文字体，以免每次都要设置 rcParams
    - 状态：完成
    - 使用： `from Heaven.chinese_encoding import *` 

- <strong><i>[encryption.py](./util/encryption.py)</i></strong>
    - 功能：加密与解密文档
    - 状态：[进行中……](./util/encryption.py)
    - 使用： `python -m Heaven.encryption`

- <strong><i>pdf_processor.py</i></strong>
    - 功能：预览 PDF 文件信息、拆分 PDF、合并 PDF
    - 状态：完成
    - 使用： `python -m Heaven.pdf_processor` ； `from Heaven import PDFProcessor`

- <strong><i>log_reader.py</i></strong>
    - 功能：读取大型文本文件，可以写出文件或打印到终端
    - 状态：完成
    - 使用： `python -m Heaven.log_reader` ； `from Heaven import LogReader`

- <strong><i>get_dns.py</i></strong>
    - 功能：自动获取域名的 DNS
    - 状态：完成
    - 使用： `python -m Heaven.get_dns` ； `from Heaven import DNSParser`

- <strong><i>make_ico.py</i></strong>
    - 功能：输入图片生成 ICO 图标文件
    - 状态：完成
    - 使用： `python -m Heaven.make_ico` ； `from Heaven import ICOGenerator`


<!-- </details> -->