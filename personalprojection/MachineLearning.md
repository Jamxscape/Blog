[TOC]

# <a name ="top">目录</a>

## [图片转文字描述](#1)

### [coco](#1.1)

### [jupyter notebook](#1.2)

## [图片转网页](#2)

### [HelloWorld篇章 YeP机器人做出的第一个网站](#2.1)

### [相关构思](#2.2)

## [图片转为文字](#3)

### [AtesseractORC 字母识别](#3.1)

### [3.2目录](#3.2)

### [3.3目录](#3.3)

### [3.4目录](#3.4)

### [3.5目录](#3.5)

### [3.6目录](#3.6)

### [3.7目录](#3.7)

### [3.8目录](#3.8)

## [4目录](#4)

### [4.1目录](#4.1)

### [4.2目录](#4.2)

### [4.3目录](#4.3)

### [4.4目录](#4.4)

# 内容

[🔝](#top)

## <a name ="1">图片转文字</a>

[🔝](#top)

### <a name = "1.1">coco</a>

#### 1) COCO 安装

[项目地址](https://github.com/pdollar/coco)

安装其实很简单, 运行下面的命令:

```shell
git clone https://github.com/pdollar/coco.git

cd coco/PythonAPI
# 如果使用的是 python2, 运行下面的命令:  
make -j8
# 如果使用的是 python3, 需要更改 Makefile:  
vi Makefile
# 将 Makefile 中的 python 改为 python3, 然后:
make -j8
```

#### 2) 加载 json 文件, 并解析其中的标注信息

下面这个是运行程序需要的包, 提前导入.

1.记录创建时的各个版本号

```Python
from __future__ import print_function
import os, sys
import numpy as np
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)
# Record package versions for reproducibility
print("os: %s" % os.name)
print("sys: %s" % sys.version)
print("numpy: %s, %s" % (np.__version__, np.__file__))
```

输出结果

```shell
os: posix
sys: 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
numpy: 1.15.2, /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/numpy/__init__.py
```

#### 2.第一个初始化程序

```python
from pycocotools.coco import COCO
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)
#初始化coco
dataDir='..'
dataType='val2017'
annFile='annotations/captions_train2017.json'.format(dataDir,dataType)
#必须创建这样的一个数据集，找到正确测试数据集才可以初始化成功，GitHub上自带的和CSDN上的数据集都是不正确的，只有在
#http://images.cocodataset.org/annotations/annotations_trainval2017.zip 里面的才可以正确测试运行，当然还有好多，例如14年的测试集，需要后续测试

# initialize COCO api for instance annotations  初始化标注数据的 COCO api 
coco=COCO(annFile)
```

```shell
#输出结果是
loading annotations into memory...
Done (t=1.58s)
creating index...
index created!
```

#### 4.说明文档

> COCO API - http://cocodataset.org/
>
> 如何使用CocoAPI，识别出图片中的内容：
>
> COCO is a large image dataset designed for object detection对象检查, segmentation对象分割, person key points detection人物关键点检查, stuff segmentation对象分割, and caption generation. This package provides Matlab, Python, and Lua APIs that assists in loading, parsing句法分析, and **visualizing the annotations**肉眼分析并注释 in COCO. Please visit http://cocodataset.org/ for more information on COCO, including for the data, paper, and tutorials辅导课. The exact format of the annotations is also described on the COCO website. The Matlab and Python APIs are complete, the Lua API provides only basic functionality.[x]
>
> In addition to this API, please download both the COCO images and annotations in order to run the demos and use the API. Both are available on the project website.
>
> -Please download, unzip, and place the images in: coco/images/
>
> -Please download and place the annotations in: coco/annotations/
>
> For substantially more details on the API please see http://cocodataset.org/#download.
>
> After downloading the images and annotations, run the Matlab, Python, or Lua demos for example usage.
>
> To install:
>
> -For Matlab, add coco/MatlabApi to the Matlab path (OSX/Linux binaries provided)
>
> -For Python, run "make" under coco/PythonAPI
>
> -For Lua, run “luarocks make LuaAPI/rocks/coco-scm-1.rockspec” under coco/
>
> Copyright (c) 2014, Piotr Dollar and Tsung-Yi Lin
>
> All rights reserved.
>
> Redistribution重新分配:and use in source and binary forms, with or without
>
> modification, are permitted provided that the following conditions are met:
>
> \1. Redistributions of source code must retain the above copyright notice, this
>
>   list of conditions and the following disclaimer.
>
> \2. Redistributions in binary form must reproduce the above copyright notice,
>
>   this list of conditions and the following disclaimer in the documentation
>
>   and/or other materials provided with the distribution.
>
> this software is provided by the copyright holders and contributors "as is" and
>
> any express or implied warranties, including, but not limited to, the implied
>
> warranties of merchantability and fitness for a particular purpose are
>
> disclaimed否认，拒绝承认. in no event shall the copyright owner or contributors be liable for
>
> any direct, indirect间接引致的, incidental附带的; 伴随的; 次要的:, special, exemplary, or consequential damages
>
> (including, but not limited to, procurement of substitute代替者 goods or services;
>
> loss of use, data, or profits; or business interruption) however caused and
>
> on any theory of liability, whether in contract, strict liability, or tort
>
> (including negligence or otherwise) arising in any way out of the use of this
>
> software, even if advised of the possibility of such damage.
>
> The views and conclusions contained in the software and documentation are those
>
> of the authors and should not be interpreted as representing official policies,
>
> either expressed or implied, of the FreeBSD Project.

[🔝](#top)

### <a name = "1.2">jupyter notebook</a>

`pip install jupyter notebook#下载notebook组件`

终端输入 

`jupyter notebook`

 在浏览器打开文件目录 上传文件 之后读取

[🔝](#top)

## <a name ="2">图片转网页</a>

### <a name = "2.1">HelloWorld篇章 YeP机器人做出的第一个网站（设想）</a>

首先ORC识别出图纸上的文字，然后分辨出边距，比例大小

边框大小是问题？？？CoCo图片识别是否可以解决？

Python写代码 读写文件

`#创建一个名为web的文件夹和HelloWorld的HTML文件操作`

`#直接使用`

`os.mkdir(‘web’)`

用到os中的mkdir方法直接创建文件夹

path可以为相对路径和绝对路径，不需要使用转移符，直接即可创建

下面是直接在当前文件夹下创建一个web文件夹

```python 
filename = filedir+'/'+text+'.html'
saveFile = open(filename, 'w’)
```

\#在指定的filedir文件夹下 生成文件名 用/ 这个斜杠才可以指定路径 

升级版本：

对图片进行分割 识别文字所占比例

先转换成二制图

然后分别对上下左右边距进行计算

计算出所占的比例，设置出字体的大小

写出CSS部分，完成

[🔝](#top)

### <a name = "2.2">相关构思</a>

##### 1.识别每一部分的框架

 网页的UI 按钮 视频组件 音频组件 选项框，链接 等等

##### 2.选出对应的框架UI，进行匹配

######  1》.在此之前要有最精简的UI框架 要求只需要调用最基本的CSS 和 JS代码块

######  2》.批量修改加入大量代码块

######  3》.识别文字，将要识别的文字加入 保留字段 

######  4》.识别图片 ，识别出图片与文字和UI界面的不同

######  5》.多层次的

######  6》.对于不同设备的处理，适应不同设备屏幕的UI模板

##### 3.动态层 数据库 跳转 动态文字图片   

  如何识别出  加入保留字段 需要应用该字段的文字 做出并加入相应的功能

  动态文字 动态图片（如轮播图等）

  网页滑动后产生的不同效果

##### 4.需要写的语言 SQL HTML JS CSS jQuery

用于开发的语言 暂时只有python 

机器学习的开发

python 中的TensorFlow用于神经网络的深度学习

输出一个Helloworld的HTML 

第一阶段开发：识别出框架图的英文文字

识别出HelloWorld

（对于没有UI界面的网页直接输出文字）

 转到ORC字母识别页 

  

[🔝](#top)

## <a name ="3">图片转文字</a>

[🔝](#top)

### <a name ="3.1">tesseractORC 字母识别</a>

[参考](https://blog.csdn.net/zhutianfu521/article/details/78666890)

源码下载以及环境配置

错误解决：这个里面解决的不对！！！

[错误参考](https://blog.csdn.net/manmanxiaowugun/article/details/83268759)

出现报错；

```shell
tesseract_ocr.cpp:648:10: fatal error: 'tesseract/baseapi.h' file not found
  \#include "tesseract/baseapi.h"
​       ^~~~~~~~~~~~~~~~~~~~~
  1 error generated.
  error: command 'gcc' failed with exit status 1
```

解决：

安装brew：

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

//之后用brew下载即可

`brew install tesseract`

既然pip下载不了 tesseract 那么为什么不用brew 呢 ，直接下载安装，所有错误搞定！个人觉得pip下载没有那好用

识别出文字 完美print出

[🔝](#top)

### <a name ="3.2">3.2内容</a>

[🔝](#top)

### <a name ="3.3">3.3内容</a>

[🔝](#top)

### <a name ="3.4">3.4内容</a>

[🔝](#top)

### <a name ="3.5">3.5内容</a>

[🔝](#top)

### <a name ="3.6">3.6内容</a>

[🔝](#top)

### <a name ="3.7">3.7内容</a>

[🔝](#top)

### <a name ="3.8">3.8内容</a>

[🔝](#top)

## <a name ="4">tensorflow</a>

[🔝](#top)

### <a name ="4.1">tensorflow 下载安装 Mac</a>

#### 1. Install the Python development environment on your system

Python 3 Python 2.7

Check if your Python environment is already configured:

Requires Python 3.4, 3.5, or 3.6

```shell
python3 --version
pip3 --version
virtualenv --version
```

If these packages are already installed, skip to the next step.

Otherwise, install [Python](https://www.python.org/), the [pip package manager](https://pip.pypa.io/en/stable/installing/), and [Virtualenv](https://virtualenv.pypa.io/en/stable/):

##### mac OS

Install using the Homebrew package manager:

```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
brew update
brew install python # Python 3
sudo pip3 install -U virtualenv # system-wide install
```



#### 2. Create a virtual environment (recommended)

Python virtual environments are used to isolate package installation from the system.

#####  mac OS

Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:

virtualenv --system-site-packages -p python3 ./venv

Activate the virtual environment using a shell-specific command:

source ./venv/bin/activate # sh, bash, ksh, or zsh

When virtualenv is active, your shell prompt is prefixed with (venv).

Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:

`pip install --upgrade pip`

`pip list # show packages installed within the virtual environment`

And to exit virtualenv later:

`deactivate # don't exit until you're done using TensorFlow`

#### 3. Install the TensorFlow pip package

Choose one of the following TensorFlow packages to install [from PyPI](https://pypi.org/project/tensorflow/):

- tensorflow —Current release for CPU-only *(recommended for beginners)*
- tensorflow-gpu —Current release with [GPU support](https://tensorflow.google.cn/install/gpu) *(Ubuntu and Windows)*
- tf-nightly —Nightly build for CPU-only *(unstable)*
- tf-nightly-gpu —Nightly build with [GPU support](https://tensorflow.google.cn/install/gpu) *(unstable, Ubuntu and Windows)*

Package dependencies are automatically installed. These are listed in the [setup.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py) file under REQUIRED_PACKAGES.

##### Virtualenv install

##### System install

`pip3 install --user --upgrade tensorflow # install in $HOME`

Verify the install:

`python3 -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"`

**Success:** TensorFlow is now installed. Read the [tutorials](https://tensorflow.google.cn/tutorials) to get started.

##### 报错：Tensorflow+python3 常见运行问题及其解决方法

https://blog.csdn.net/shanglianlm/article/details/79390615

[🔝](#top)

### <a name ="4.2">4.2内容</a>

[🔝](#top)

### <a name ="4.3">4.3内容</a>

[🔝](#top)

### <a name ="4.4">4.4内容</a>

[🔝](#top)

### <a name ="4.5">4.5内容</a>