# Heaven

> 下阶段任务：按照 Python 第三方库规范完善 STRUCTURE

## 一、简介

本仓库集成了一些常用功能，包括数据科学处理过程、日常工作效率提升，以及一些有趣的功能。目前正在开发中，如果效果良好将在以后继续完善，打造一个数据科学专用工具箱。数据科学包括多个维度，具体针对哪方面的问题...暂时还没想好。

安装方法：

```bash
cd %PYTHON_HOME%/Lib/
git clone https://github.com/paradiseeee/heaven
```

*PS：本人小白，纯属瞎搞，路过的朋友如果感兴趣欢迎交流指教*


## 二、详情

### [***Heaven***](./) -- 根目录，数据分析工具

- <strong><i>\_\_init\_\_.py</i></strong>
    - 功能：显示 module 信息，包括 LISENCE、DOC-STRING、具体内容
    - 状态：同步更新
    - 使用： `python -m Heaven.__init__`

- <strong><i>mysql_helper.py</i></strong>
    - 功能：将 MySQL 终端的常用功能集成到 Python 环境，解决变量交互问题
    - 状态：完成
    - 使用： `from Heaven.mysql_helper import MysqlHelper` ； `help(MysqlHelper)`

- <strong><i>mpl_tools.py</i></strong>
    - 功能：matplotlib 的补充功能
    - 状态：[进行中...]()
    - 使用： `from Heaven.mpl_tools import MyFuncAnimation, Font`

- <strong><i>scorpion.py</i></strong>
    - 功能：爬虫开发常用工具
    - 状态：[进行中...]()
    - 使用： `from Heaven import scorpion; help(scorpion)`

- <strong><i>其他文件</i></strong>
    - `.gitignore`
    - `.gitattributes`
    - `_UserKeys`： 用户的密钥配置，例如 API 密钥、数据库密钥等；
    - `_UserKeys_PublicFormat`： 脱敏后的 _UserKeys，用来参考密钥配置；
    - `update_python_lib.bat`： 更新 %PYTHON_HOME%\LIB\Heaven 的批处理；
    - `LISENCE`
    - `README.md`
    - `_config.yml`：GitHub Page 主题

### [***Heaven.util***](./util) -- 其他乱七八糟的小工具

<!-- <details>
    <summary>展开<strong><em>模块列表</em></strong></summary> -->

- <strong><i>translater.py</i></strong>
    - 功能：实时翻译剪切板中的文本
    - 状态：完成
    - 使用： `python -m Heaven.util.translater`

- <strong><i>text_identify.py</i></strong>
    - 功能：文本识别，并输出文件，支持中文/英文
    - 状态：完成
    - 使用： `python -m Heaven.util.text_identify`

- <strong><i>text_reader.py</i></strong>
    - 功能：输入文本转换为语音，支持中文/英文、文本文件/命令行输入
    - 状态：完成
    - 使用： `python -m Heaven.util.text_reader`

- <strong><i>pdf_processor.py</i></strong>
    - 功能：预览 PDF 文件信息、拆分 PDF、合并 PDF
    - 状态：完成
    - 使用： `python -m Heaven.util.pdf_processor`

- <strong><i>mouse_coord.py</i></strong>
    - 功能：实时显示鼠标位置坐标
    - 状态：完成
    - 使用： `python -m Heaven.util.mouse_coord`

- <strong><i>img_down.py</i></strong>
    - 功能：自动解析地址下载 Bing 首页背景图高清大图
    - 状态：完成
    - 使用： `python -m Heaven.util.img_down`

- <strong><i>get_dns.py</i></strong>
    - 功能：自动获取域名的 DNS，并更新 DNS 缓存
    - 状态：完成
    - 使用： `python -m Heaven.util.get_dns`

- <strong><i>make_ico.py</i></strong>
    - 功能：输入图片生成 ICO 图标文件
    - 状态：完成
    - 使用： `python -m Heaven.util.make_ico`

- <strong><i>[encryption.py](./util/encryption.py)</i></strong>
    - 功能：加密与解密文档
    - 状态：[进行中……](./util/encryption.py)
    - 使用： `python -m Heaven.util.encryption`

- <strong><i>log_reader.py</i></strong>
    - 功能：读取大型文本文件，可以写出文件或打印到终端
    - 状态：完成
    - 使用： `python -m Heaven.util.log_reader`

<!-- </details> -->
