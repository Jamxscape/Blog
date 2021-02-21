[TOP]

# 目录

## [基础概念](#1)

### [从另一个文件中引用另外的类函数](#1.1)

# 内容

## <a name="1">基础概念</a>

### <a name="1.1">从另一个文件中引用另外的类函数</a>

![1.1](/Users/mayuan/Desktop/Hi-Story/github_blog/Blog/language/img/python3_1_1.png)

关系为CSS_Position继承CSS，然后getdata.py要引用CSS__Position这个类

问题出在CSS_Position中，由于getdata.py想要引用 from CSS.CSS_P import CSSP

没什么问题，但是CSS_P 在引用CSS.py时，使用了相对路径，使得进一步getdata引用过程中仍然使用相对路径，故出错

应该直接使用from CSS.CSS import CSS 这样的绝对路径

https://blog.csdn.net/sinat_27693393/article/details/70037718