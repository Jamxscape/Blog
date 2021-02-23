[TOC]

# 目录

## [概念](#1)

### [读书笔记](#1.1)

## [常见问题](#2)

## [杂项](#3)

# 内容

## <a name ="1">常用指令</a>

### <a name="1.2">读书笔记</a> 

*<!--2016/12/15-->*

1. C语言规定，标识符只能由字母(A~Z, a~z)、数字(0~9)和下划线(_)组成，并且第一个字符必须是字母或下划线。以下标识符是合法的：

   a, x, x3, BOOK_1, sum5

   以下标识符是非法的：

   3s  不能以数字开头

   s*T  出现非法字符*

   -3x  不能以减号(-)开头

   bowy-1  出现非法字符减号(-)

2. 在标识符中，大小写是有区别的，例如BOOK和book 是两个不同的标识符。

3. %d称为格式控制符，它指明了以何种形式输出数据。格式控制符均以%开头，后跟其他字符。%d 表示以十进制形式输出一个整数。除了 %d，printf 支持更多的格式控制，例如：

4. - %c：输出一个字符。c 是 character 的简写。
   - %s：输出一个字符串。s 是 string 的简写。
   - %f：输出一个小数。f 是 float 的简写。

5. C语言支持单行注释和多行注释：

6. - 单行注释以//开头，直到本行末尾（不能换行）；
   - 多行注释以/*开头，以*/结尾，注释内容可以有一行或多行。

7. 在C语言中，表达式a=a#b可以简写为a#=b，#表示 +、-、*、/、% 中的任何一种运算符。

8. ++ 在前面叫做前自增（例如 ++a）。前自增先进行自增操作，再进行其他操作。

9. ++ 在后面叫做后自增（例如 a++）。后自增先进行其他操作，再进行自增操作。

10. 对于语句赋值语句a=b=c;，先执行b=c，再执行a=b，而不是反过来，这说明赋值操作符=具有右结合性。

11. C语言的运算符众多，具有不同的优先级和结合性，我们将它们全部列了出来，方便大家对比和记忆：

12. | 优先级 | 运算符           | 名称或含义                | 使用形式                  | 结合方向 | 说明             |
    | ------ | ---------------- | ------------------------- | ------------------------- | -------- | ---------------- |
    | 1      | []               | 数组下标                  | 数组名[常量表达式]        | 左到右   |                  |
    | ()     | 圆括号           | （表达式）/函数名(形参表) |                           |          |                  |
    | .      | 成员选择（对象） | 对象.成员名               |                           |          |                  |
    | ->     | 成员选择（指针） | 对象指针->成员名          |                           |          |                  |
    | 2      | -                | 负号运算符                | -表达式                   | 右到左   | 单目运算符       |
    | (类型) | 强制类型转换     | (数据类型)表达式          |                           |          |                  |
    | ++     | 自增运算符       | ++变量名/变量名++         | 单目运算符                |          |                  |
    | --     | 自减运算符       | --变量名/变量名--         | 单目运算符                |          |                  |
    | *      | 取值运算符       | *指针变量                 | 单目运算符                |          |                  |
    | &      | 取地址运算符     | &变量名                   | 单目运算符                |          |                  |
    | !      | 逻辑非运算符     | !表达式                   | 单目运算符                |          |                  |
    | ~      | 按位取反运算符   | ~表达式                   | 单目运算符                |          |                  |
    | sizeof | 长度运算符       | sizeof(表达式)            |                           |          |                  |
    | 3      | /                | 除                        | 表达式/表达式             | 左到右   | 双目运算符       |
    | *      | 乘               | 表达式*表达式             | 双目运算符                |          |                  |
    | %      | 余数（取模）     | 整型表达式/整型表达式     | 双目运算符                |          |                  |
    | 4      | +                | 加                        | 表达式+表达式             | 左到右   | 双目运算符       |
    | -      | 减               | 表达式-表达式             | 双目运算符                |          |                  |
    | 5      | <<               | 左移                      | 变量<<表达式              | 左到右   | 双目运算符       |
    | >>     | 右移             | 变量>>表达式              | 双目运算符                |          |                  |
    | 6      | >                | 大于                      | 表达式>表达式             | 左到右   | 双目运算符       |
    | >=     | 大于等于         | 表达式>=表达式            | 双目运算符                |          |                  |
    | <      | 小于             | 表达式<表达式             | 双目运算符                |          |                  |
    | <=     | 小于等于         | 表达式<=表达式            | 双目运算符                |          |                  |
    | 7      | ==               | 等于                      | 表达式==表达式            | 左到右   | 双目运算符       |
    | !=     | 不等于           | 表达式!= 表达式           | 双目运算符                |          |                  |
    | 8      | &                | 按位与                    | 表达式&表达式             | 左到右   | 双目运算符       |
    | 9      | ^                | 按位异或                  | 表达式^表达式             | 左到右   | 双目运算符       |
    | 10     | \|               | 按位或                    | 表达式\|表达式            | 左到右   | 双目运算符       |
    | 11     | &&               | 逻辑与                    | 表达式&&表达式            | 左到右   | 双目运算符       |
    | 12     | \|\|             | 逻辑或                    | 表达式\|\|表达式          | 左到右   | 双目运算符       |
    | 13     | ?:               | 条件运算符                | 表达式1? 表达式2: 表达式3 | 右到左   | 三目运算符       |
    | 14     | =                | 赋值运算符                | 变量=表达式               | 右到左   |                  |
    | /=     | 除后赋值         | 变量/=表达式              |                           |          |                  |
    | *=     | 乘后赋值         | 变量*=表达式              |                           |          |                  |
    | %=     | 取模后赋值       | 变量%=表达式              |                           |          |                  |
    | +=     | 加后赋值         | 变量+=表达式              |                           |          |                  |
    | -=     | 减后赋值         | 变量-=表达式              |                           |          |                  |
    | <<=    | 左移后赋值       | 变量<<=表达式             |                           |          |                  |
    | >>=    | 右移后赋值       | 变量>>=表达式             |                           |          |                  |
    | &=     | 按位与后赋值     | 变量&=表达式              |                           |          |                  |
    | ^=     | 按位异或后赋值   | 变量^=表达式              |                           |          |                  |
    | \|=    | 按位或后赋值     | 变量\|=表达式             |                           |          |                  |
    | 15     | ,                | 逗号运算符                | 表达式,表达式,…           | 左到右   | 从左向右顺序运算 |

13. puts() 函数在输出结束时会自动换行，而 printf() 和 putchar() 不会，需要手动添加换行符\n

14. printf 格式控制字符的完整形式如下：[flags][width][.precision]type

15. ![img](data:image/jpeg;base64,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)                                             i f(判断条件){

      语句块1

    }else{

      语句块2

    }

16. C语言规定，else 总是与它前面最近的 if 配对，

17. 关系运算符的运算结果只有 0 或 1。当条件成立时结果为 1，条件不成立结果为 0。我们将运算结果 1 称为“真”，表示条件成立，将 0 称为“假”，表示条件不成立。

18. | 运算符 | 说明                           | 结合性 | 举例                   |
    | ------ | ------------------------------ | ------ | ---------------------- |
    | &&     | 与运算，双目，对应数学中的“且” | 左结合 | 1&&0、(9>3)&&(b>a)     |
    | \|\|   | 或运算，双目，对应数学中的“或” | 左结合 | 1\|\|0、(9>3)\|\|(b>a) |
    | !      | 非运算，单目，对应数学中的“非” | 右结合 | !a、!(2<5)             |

19. **break** 是C语言中的一个关键字，专门用于跳出 switch 语句。所谓“跳出”，是指一旦遇到 break，就不再执行 switch 中的任何语句，包括当前分支中的语句和其他分支中的语句；也就是说，整个 switch 执行结束了，接着会执行整个 switch 后面的代码。

20. 在C语言中，共有三大常用的程序结构：

21. - 顺序结构：代码从前往后执行，没有任何“拐弯抹角”；
    - 选择结构：也叫分支结构，重点要掌握 if else、switch 以及条件运算符；
    - 循环结构：重复执行同一段代码。

22. for 循环的一般形式为：

    for(表达式1; 表达式2; 表达式3){

      语句块

    }

    它的运行过程为：

    1) 先执行“表达式1”。

    2) 再执行“表达式2”，如果它的值为真（非0），则执行循环体，否则结束循环。

    3) 执行完循环体后再执行“表达式3”。

    4) 重复执行步骤 2) 和 3)，直到“表达式2”的值为假，就结束循环。上面的步骤中，2) 和 3) 是一次循环，会重复执行，for 语句的主要作用就是不断执行步骤 2) 和 3)。

    “表达式1”仅在第一次循环时执行，以后都不会再执行，可以认为这是一个初始化语句。“表达式2”一般是一个关系表达式，决定了是否还要继续下次循环，称为“循环条件”。“表达式3”很多情况下是一个带有自增或自减操作的表达式，以使循环条件逐渐变得“不成立”。

23. break，用它来跳出 switch 语句。当 break 关键字用于 while、for 循环时，会终止循环而执行整个循环语句后面的代码。break 关键字通常和 if 语句一起使用，即满足条件时便跳出循环。

24. continue 语句的作用是跳过循环体中剩余的语句而强制进入下一次循环。continue语句只用在 while、for 循环中，常与 if 条件语句一起使用，判断条件是否成立。

25. a[3][4] 表示a数组第3行第4列的元素。

26. 二维数组的初始化可以按行分段赋值，也可按行连续赋值。

    例如对数组a[5][3]，按行分段赋值可写为：

    int a[5][3]={ {80,75,92}, {61,65,71}, {59,63,70}, {85,87,90}, {76,77,85} };

    按行连续赋值可写为：

    int a[5][3]={80, 75, 92, 61, 65, 71, 59, 63, 70, 85, 87, 90, 76, 77, 85};

    这两种赋初值的结果是完全相同的。1）可以只对部分元素赋初值，未赋初值的元素自动取0值。例如：

    int a[3][3]={{1},{2},{3}};

27. 在C语言中，输出字符串的函数有两个：

28. - puts()：直接输出字符串，并且只能输出字符串。
    - printf()：通过格式控制符 %s 输出字符串。除了字符串，printf() 还能输出其他类型的数据。
    - 在C语言中，输入字符串的函数有两个：
    - - scanf()：通过格式控制符 %s 输入字符串。除了字符串，scanf() 还能输入其他类型的数据。
      - gets()：直接输入字符串，并且只能输入字符串。

29. 如果希望读取的字符串中不包含空格，那么使用 scanf() 函数；如果希望获取整行字符串，那么使用 gets() 函数，它能避免空格的截断。

30. 返回值类型可以是C语言中的任意数据类型，例如 int、float、char 等。

31. 函数名是标识符的一种，命名规则和标识符相同。函数名后面的括号( )不能少。

32. 函数体是函数需要执行的代码。即使只有一个语句，也要由{ }包围。

33. 在函数体中使用**return**语句返回数据。

34. 函数定义时给出的参数称为形式参数，简称形参；函数调用时给出的参数（传递的数据）称为实际参数，简称实参。函数调用时，将实参的值传递给形参，相当于一次赋值操作。注意：实参和形参的类型、数目必须一致。

35. 形参和实参有以下几个特点：

    1) 形参变量只有在函数被调用时才会分配内存，调用结束后，立刻释放内存，所以形参变量只有在函数内部有效，不能在函数外部使用。

    2) 实参可以是常量、变量、表达式、函数等，无论实参是何种类型的数据，在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参，所以应该提前用赋值、输入等办法使实参获得确定值。

    3) 实参和形参在数量上、类型上、顺序上必须严格一致，否则会发生“类型不匹配”的错误。

    函数调用中发生的数据传送是单向的，只能把实参的值传送给形参，而不能把形参的值反向地传送给实参。 因此在函数调用过程中，形参的值发生改变，而实参中的值不会变化。

36. 函数声明给出了函数名、返回值类型、参数列表（参数类型）等与该函数有关的信息，称为函数原型（Function Prototype）。

37. http://www.cplusplus.com/reference/clibrary/C++学习者的福利网站

38. 定义在函数内部的变量称为局部变量（Local Variable），它的作用域仅限于函数内部， 离开该函数后就是无效的，再使用就会报错。在所有函数外部定义的变量称为全局变量（Global Variable），它的作用域默认是整个程序，也就是所有的源文件，包括 .c 和 .h 文件。

39. C程序的全部工作都是由各式各样的函数完成的，所以也把C语言称为函数式语言。

    标准C语言（[ANSI C](http://c.biancheng.net/cpp/html/1.html)）共定义了15 个头文件，称为“C标准库”，所有的编译器都必须支持，如何正确并熟练的使用这些标准库，可以反映出一个程序员的水平。

40. - 合格程序员：<stdio.h>、<ctype.h>、<stdlib.h>、<string.h>
    - 熟练程序员：<assert.h>、<limits.h>、<stddef.h>、<time.h>
    - 优秀程序员：<float.h>、<math.h>、<error.h>、<locale.h>、<setjmp.h>、<signal.h>、<stdarg.h>

41. main() 函数是主函数，它可以调用其它函数，而不允许被其它函数调用。因此，C程序的执行总是从 main() 函数开始，完成对其它函数的调用后再返回到 main() 函数，最后由 main() 函数结束整个程序。

42. 部分预处理指令：

43. | 指令     | 说明                                                      |
    | -------- | --------------------------------------------------------- |
    | #        | 空指令，无任何效果                                        |
    | #include | 包含一个源代码文件                                        |
    | #define  | 定义宏                                                    |
    | #undef   | 取消已定义的宏                                            |
    | #if      | 如果给定条件为真，则编译下面代码                          |
    | #ifdef   | 如果宏已经定义，则编译下面代码                            |
    | #ifndef  | 如果宏没有定义，则编译下面代码                            |
    | #elif    | 如果前面的#if给定条件不为真，当前条件为真，则编译下面代码 |
    | #endif   | 结束一个#if……#else条件编译块                              |

44. 编译（Compile）会将源文件（.c文件）转换为目标文件。对于VC/VS，目标文件后缀为 .obj；对于GCC，目标文件后缀为 .o。

45. 用尖括号 #include <>：

46. - 一般用于包含标准的库头文件，编译器会去系统配置的库环境变量和者用户配置的路径去搜索，而不会在项目的当前目录去查找

47. 用双引号 #include ""：

48. - 一般用于包含用户自己编写的头文件，编译器会先在项目的当前目录查找，找不到后才会去系统配置的库环境变量和用户配置的路径去搜索

49. 宏定义的一般形式为：

    \#define 宏名 字符串

50. **对宏定义的几点说明** 1) 宏定义是用宏名来表示一个字符串，在宏展开时又以该字符串取代宏名，这只是一种简单的替换。字符串中可以含任何字符，可以是常数，也可以是表达式，预处理程序对它不作任何检查，如有错误，只能在编译已被宏展开后的源程序时发现。

    2) 宏定义不是说明或语句，在行末不必加分号，如加上分号则连分号也一起替换。

    3) 宏定义必须写在函数之外，其作用域为宏定义命令起到源程序结束。如要终止其作用域可使用#undef命令。

51. 带参数的宏，在调用中，不仅要宏展开，而且要用实参去代换形参。

52. 对于带参宏定义不仅要在参数两侧加括号，还应该在整个字符串外加括号。

53. CPU 访问内存时需要的是地址，而不是变量名和函数名！变量名和函数名只是地址的一种助记符，当源文件被编译和链接成可执行程序后，它们都会被替换成地址。编译和链接过程的一项重要任务就是找到这些名称所对应的地址。

54. **对星号*********的总结**

55. - 表示乘法，例如int a = 3, b = 5, c; c = a * b;，这是最容易理解的。
    - 表示定义一个指针变量，以和普通变量区分开，例如int a = 100; int *p = &a;。
    - 表示获取指针指向的数据，是一种间接操作，例如int a, b, *p = &a; *p = 100; b = *p;。

56. 

## <a name ="2">常见问题</a>

## <a name="3">杂项</a>

