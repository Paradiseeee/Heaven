# Heaven

> 下阶段任务：按照 Python 第三方库规范完善 STRUCTURE

## 一、简介

本仓库集成了一些数据科学常用功能，包括数据分析过程、日常工作效率提升，以及一些有趣的工具。目前正在持续更新，如果效果良好将在以后继续完善，打造一个专用的工具箱。

安装方法：

```bash
cd %PYTHON_HOME%/Lib/
git clone https://github.com/paradiseeee/heaven
```

*PS：本人小白，路过的朋友欢迎交流指教*


## 二、详情

### [***Heaven***](./) -- 根目录，数据分析工具

- <strong><i>\_\_init\_\_.py</i></strong>
    - Module 的信息、常量

- <strong><i>mysql_helper.py</i></strong>
    - 将 MySQL 终端的常用功能集成到 Python 环境，解决变量交互问题

- <strong><i>mpl_tools.py</i></strong>
    - matplotlib 的补充功能

- <strong><i>scorpion.py</i></strong>
    - 爬虫开发常用工具

- <strong><i>iotools.py</i></strong>
    - 系统编程常用工具

- <strong><i>其他文件</i></strong>
    - `README.md`
    - `LISENCE`
    - `.gitignore`
    - `.gitattributes`
    - `_UserKeys`： 用户的密钥配置，例如 API 密钥、数据库密钥等；
    - `_UserKeys_PublicFormat`： 脱敏后的 _UserKeys，用来参考密钥配置；
    - `update_python_lib.bat`： 更新 %PYTHON_HOME%\LIB\Heaven 的批处理；
    - `_config.yml`：GitHub Page 主题

### [***Heaven.util***](./util) -- 其他乱七八糟的工具

<!-- <details>
    <summary>展开<strong><em>模块列表</em></strong></summary> -->

Name|Description|Status
-:|:-|:-:|
<strong><i>translater.py</i></strong>|实时翻译剪切板中的文本，中英互译|完成|
<strong><i>text_identify.py</i></strong>|识别图片中的文本并输出，支持中文或英文|完成|
<strong><i>text_reader.py</i></strong>|将文本转换为语音并播放，支持中文或英文|完成|
<strong><i>pdf_processor.py</i></strong>|PDF 拆分合并功能|完成|
<strong><i>mouse_coord.py</i></strong>|实时显示鼠标位置坐标|完成|
<strong><i>get_dns.py</i></strong>|获取域名IP地址，并更新 DNS 缓存|完成|
<strong><i>img_down.py</i></strong>|下载 Bing 首页背景图|完成|
<strong><i>make_ico.py</i></strong>|图片转换为图标文件|完成|

<!-- </details> -->
