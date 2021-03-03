[TOC]

# <a name ="top">目录</a>

## [基础概念](#1)

### [String 和 StringBuffer](#1.1)

### [1.2三级标题](#1.2)

## [普通算法](#2)

### [日期计算（计算这一天的前(后)n天的日期）](#2.1)

### [字符串与数字互转](#2.2)

### [日期格式转换](#2.3)

### [字符串比较](#2.4)

### [字符串与数字互转](#2.5)

### [字符串与数字互转](#2.6)

### [字符串与数字互转](#2.7)

### [字符串与数字互转](#2.8)

# 内容

## <a name ="1">基础概念</a>

[🔝](#top)

### <a name = "1.1">String 和 StringBuffer</a>

将StringBuffer转换成String

   StringBuffer类成员toString函数可将其转换成String类型。实例如下：

```java
StringBuffer stringBuffer = new StringBuffer(“Hello World.”);
String c = stringBuffer.toString();// 调用toString函数将StringBuffer对象转换成String对象
```

将String转换成StringBuffer

​    方式一：利用构造函数

    ```java
String str=“Hello World.”;
StringBuffer buffer = new StringBuffer(str);
    ```

​    方式二：调用append函数

```java
String str=“Hello World.”;    
StringBuffer buffer2 = new StringBuffer();
buffer2.append(str);
```

### <a name = "1.2">1.2三级标题</a>

## <a name ="2">普通算法</a>

### <a name = "2.1">日期计算（计算这一天的前(后)n天的日期）</a>

```java
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
public class test {  
  
    public static void main(String[] args) {  
        Date date = new Date(); // 新建一个日期  
  
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd"); // 格式化日期  
  
        String beforeDate = sdf.format(getDateBefore(date, 10));  //调用前几天日期计算的方法
        System.out.println(beforeDate);  
        String afterDate = sdf.format(getDateAfter(date, 10));  //调用后几天日期的计算方法
        System.out.println(afterDate);  
    }  
  
    /** 
     * 得到几天前的时间 
     */  
  
    public static Date getDateBefore(Date d, int day) {  
        Calendar now = Calendar.getInstance();  
        now.setTime(d);  
        now.set(Calendar.DATE, now.get(Calendar.DATE) - day);  
        return now.getTime();  
    }  
  
    /** 
     * 得到几天后的时间 
     */  
      
    public static Date getDateAfter(Date d, int day) {  
        Calendar now = Calendar.getInstance();  
        now.setTime(d);  
        now.set(Calendar.DATE, now.get(Calendar.DATE) + day);  
        return now.getTime();  
    }  
}
```

[🔝](#top)

### <a name = "2.2">字符串与数字互转</a>

#### **一、字符串转数字**

1、通过基本类型对应的包装类则可以实现把字符串转换成基本类型。Java为8种基本类型都提供了对

应的包装类：boolean对应Boolean、byte对应Byte、short对应Short、int对应Integer、long对

应Long、char对应Character、float对应Float、double对应Double，8个包装类都提供了一个

parseXxx(String str)静态方法用于将字符串转换成基本类型。（**注意：如果字符串不是数值型字**

**符串，转换将导致一个运行时错误。**）

```java
String s = "123";
byte b = Byte.parseByte(s);
short t = Short.parseShort(s);
int i = Integer.parseInt(s);
long l = Long.parseLong(s);
Float f = Float.parseFloat(s);
Double d = Double.parseDouble(s);
boolean bo = Boolean.parseBoolean(s);
char c = Character.parseCharacter(s);
```

2、`i=Integer.valueOf(s).intValue();`

**总结：**方法1直接使用静态方法，不会产生多余的对象，但会抛出异常。方法2，Integer.valueOf(s

) 相当于new Integer(Integer.parseInt(s))，也会抛异常，但会多产生一个对象。

#### **二、数字转字符串**

1、`String.valueOf(Object)`

各种数字类型转换成字符串型：

```java
// 其中 value 为任意一种数字类型。将不用担心object是否为null值这一问题。
String s = String.valueOf(value);
```

Jdk里String. valueOf(Object)源码如下：

```java
/** *
 \* Returns the string representation of the Object argument.
 \* @param  obj  an Object.
 \* @return if the argument is null, then a string equal to
 \* “null”; otherwise, the value of
 \* obj.toString() is returned.
 \* @see  java.lang.Object#toString()
 */
public static String valueOf(Object obj) {
  return (obj == null) ? “null” : obj.toString();
}
```

从上面的源码可以很清晰的看出null值不用担心的理由。但是，这也恰恰给了我们隐患。我们应当注

意到，当object为null时，String.valueOf（object）的值是字符串”null”，而不是null！！！

在使用过程中切记要注意。

2、`Object.toString()`

在使用时要注意，必须保证object不是null值，否则将抛出NullPointerException异常。

3、`i + ""`

4、（String）要转换的对象

使用这种方法时，需要注意的是类型必须能转成String类型。因此最好用instanceof做个类型检查，

以判断是否可以转换。否则容易抛出CalssCastException异常。此外，需特别小心的是因定义为

Object类型的对象在转成String时语法检查并不会报错，这将可能导致潜在的错误存在。这时要格外

小心。此外，因null值可以强制转换为任何java类类型，`(String)null`也是合法的。

**效率：方法2>方法3>方法1，方法1和方法3差别不大。**

[🔝](#top)

### <a name = "2.3">日期格式转换</a>

#### **日期格式化显示**

```java
package org.maoge.common;
        import java.text.SimpleDateFormat;
        import java.util.Date;
public class SimpleDateFormatDemo {
    public static void main(String[] args) {
        //默认输出格式
        Date date=new Date();
        System.out.println(date);//Fri Oct 27 16:56:37 CST 2017
        //日期格式化显示，首先定义格式
        SimpleDateFormat sdf1=new SimpleDateFormat("yyyyMMdd");//显示20171027格式
        SimpleDateFormat sdf2=new SimpleDateFormat("yyyy-MM-dd");//显示2017-10-27格式
        SimpleDateFormat sdf3=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");//显示2017-10-27 10:00:00格式
        SimpleDateFormat sdf4=new SimpleDateFormat("yyyy年MM月dd日HH时mm分ss秒");//显示2017年10月27日10时00分00秒格式
        //将格式应用于日期
        System.out.println(sdf1.format(date));//20171027
        System.out.println(sdf2.format(date));//2017-10-27
        System.out.println(sdf3.format(date));//2017-10-27 17:11:13
        System.out.println(sdf4.format(date));//2017年10月27日17时11分13秒
    }
}

```

#### **将字符串转换为对应日期**

注意，因为可能定义的格式和实际字符串提供的格式不符合，所以会抛出异常

```java
package org.maoge.common;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
public class SimpleDateFormatDemo {
    public static void main(String[] args) {
        //首先定义格式
        SimpleDateFormat sdf1=new SimpleDateFormat("yyyyMMdd");
        SimpleDateFormat sdf2=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        //按格式进行转换
        String strDate1="20151010";//符合sdf1格式
        String strDate2="20171027 10:00:00";//不符合格式
        try {
            Date date1=sdf1.parse(strDate1);
            System.out.println(date1);//正常输出Sat Oct 10 00:00:00 CST 2015
            Date date2=sdf2.parse(strDate2);//报错java.text.ParseException: Unparseable date: "20171027 10:00:00"
            System.out.println(date2);
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
}
```

[🔝](#top)

### <a name="2.4">字符串比较</a>

**Java空字符串与null的区别：**



1、类型

null表示的是一个对象的值，而并不是一个字符串。例如声明一个对象的引用，`String a = null ;`

""表示的是一个空字符串，也就是说它的长度为0。例如声明一个字符串`String str = "" ;`

2、内存分配

`String str = null ;` 表示声明一个字符串对象的引用，但指向为null，也就是说还没有指向任何的内存空间；

String str = "";  表示声明一个字符串类型的引用，其值为""空字符串，这个str引用指向的是空字符串的内存空间；

在java中变量和引用变量是存在栈中（stack），而对象（new产生的）都是存放在堆中（heap）：

就如下：

`String str = new String("abc") ;`

> ps：=左边的是存放在栈中（stack），=右边是存放在堆中（heap）。 

```java
if(temp.equals("")) {
  Toast.*makeText*(getName.this,"姓名不能为空",Toast.*LENGTH_SHORT*).show();
}//安卓开发中java判断是否为空时用equals()
```

