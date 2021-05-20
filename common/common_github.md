## 目录

#### [**git克隆**](#1.1)    [On branch main Your branch is up to date with 'origin/main'.暂未解决]()

## 内容

#### <a name="1.1">git克隆</a>

1. #### 麻烦办法

GitHub desktop下载后，自动配置好git命令 终端中直接测试git 是否可以使用

`git config --global user.name “jamxscape”`  //配置用户名

`git config --global user.email ["228422060@qq.com](mailto:"228422060@qq.com)”` //配置邮箱号

`git config --global color.ui auto`  // 让Git以彩色显示。

`git clone <repository> <directory>` //使用clone指令可以复制数据库，在指定远程数据库的URL，在指定新目录的名称。

或者直接cd 到指定目录下 执行git clone <项目网址>  即可直接下载到当前的目录中 

2. #### 简单办法

   直接下载git安装包 [地址](https://git-scm.com/download/mac)

3. #### 其他方法

   [地址](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)

> 出现报错  

> ###### `SSL_connect: SSL_ERROR_SYSCALL in connection to [github.com:443](http://github.com:443/)`
>
> 使用命令 `git config --global --unset http.proxy`
>
> 然后再次使用IntelliJ IDEA push，OK，问题解决

> 解决办法：

> 1、open ~/.gitconfig
>
> 2、删除里面的
>
> [http "[https://github.com](https://github.com/)";]
>
> proxy = socks5://127.0.0.1:1080

