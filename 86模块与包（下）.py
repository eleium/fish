#如何将程序分享到pypi上 (python package index) python的包的索引
#用pip命令下载包，就是去pypi下载

#pypi官网的上传模块完整框架：
"""
    project                                     #项目的主目录
      |----  LICENSE                            #开源许可证
      |----  pyproject.toml                     #指定安装环境
      |----  README.md                          #项目的介绍
      |----  src/
      |       |----img_compress/                #源代码主目录
      |               |---- __init__.py         #包的初始化文件
      |               |----compress.py          #源代码
      |----  tests/                             #测试文件夹
      """

# LICENSE  是一个文本文件。需要指定一个开源许可证，最简单的 MIT许可证


#pyproject.toml 也是一个文本文件，用于定义包的安装环境，指定安装的套件的工具等。根据模板自己修改
#项目的名字不能跟pypi上已有的重复。每个版本只能上传一次。
"""
pyproject.toml的详细解析：
name 指定项目的名称，可以包含字母、数字、点号（.）、下划线（_）、逗号（,）和减号（-），不能跟 PyPI 上已有的项目同名；

version 指定项目的版本信息；

authors 指定项目的作者，可以指定多名作者及维护者的信息；

description 指定一个简短的项目描述摘要；

readme 指定一个描述文件的路径（通常是 "README.md"），包含该项目的详细描述，文件内容将显示在 PyPI 上面的详细信息页面；

requires-python 指定项目所支持的 Python 版本，pip 会遍历项目的历史版本，然后找到与用户使用的 Python 版本相匹配的软件包安装；

classifiers 为索引和 pip 提供了一些关于该项目的附加元数据，
比如上面的内容指定了 "该项目仅兼容 Python 3，根据 MIT 许可证协议，并且与操作系统无关"（至少应该包含这三个内容），
另外还可以指定其它超多的信息，请参考 - https://pypi.org/classifiers/

dependencies 指定该项目所依赖的其他模块（这里演示的项目，需要导入第三方 tinify 模块）

最后，[project-urls] 则允许你指定与该项目相关的一些额外的链接。
"""


#REASDME.md  需要编写详细的文档，告诉用户如何调用这个模块来实现功能。一个产品介绍

#对将要发布的项目进行封装：需要下载pip install --upgrade build 封装项目
#封装完成后，项目文件夹会出现dict文件夹，里面有两个包，*.tar.gz 原发行版和 *.whl，已构建的一个发行版
#选择使用twine工具上传。先pip install twine下载工具，python -m twine upload --repository pypi dict/*
#输入用户名及密码，完成了。

#可以正常的用pip 下载这个模块了。