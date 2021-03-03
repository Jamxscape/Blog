[TOC]

# <a name = "top">目录</a>

## [基础概念](#1)

### [1.1三级标题](#1.1)

### [1.2三级标题](#1.2)

## [项目bug](#2)

### [OkHttp3在Android P](#2.1)

### [Could not find com.android.tools.build:aapt2:3.2.0-alpha14-4748712.](#2.2)

### [Android7.0调用相机 FileProvider.getUriForFile 报空指针](#2.3)

### [app图标](#2.4)

### [Android 动态设置padding跟margin的问题](#2.5)

### [动态清空LinearLayout中的所有控件](#2.6)

### [动态增加textView](#2.7)

### [SQL lite查询](#2.8)

### [Android Studio新建empty activity，MainActivity.java报错，继承的AppCompatActivity红色字体报错，如何解决：](#2.9)

### [Fragment刷新](#2.10)

### [数据库更新](#2.11)

### [安卓去标题代码](#2.12)

### [Fragment框架下控制其他Activity页面的监听](#2.13)

### [五个页面跳转](#2.14)

## [XML相关](#3)

### [drawable写一个圆.xml](#3.1)

### [拖拉文件与AndroidManiFest.xml中文件上声明](#3.2)

### [圆弧按钮](#3.3)

### [基本表格布局](#3.4)

### [圆形头像](#3.5)

### [页面下滑](#3.6)

## [开源项目](#4)

### [时间选项选择](#4.1)

# 内容

## <a name ="1">1二级标题</a>

[🔝](#top)

### <a name = "1.1">1.1三级标题</a>

### <a name = "1.2">1.2三级标题</a>

## <a name ="2">项目bug</a>

[🔝](#top)

### <a name = "2.1">OkHttp3在Android P</a>

#### **使用OkHttp3在Android P 出现的错误：CLEARTEXT communication to host not permitted by network security policy**

#### **问题描述:**

使用OkHttp3做网络请求框架时，如果是http请求而非https请求，会导致请求失败，因为Android P之后系统限制了明文的网络请求，非加密请求会被系统禁止掉。

同样如果您使用了WebView加载http协议下的页面，也会出现加载失败，https则不受影响。

#### **分析:**

OkHttp3的源码可以看到，它做了请求的检查

```java
if (!Platform.get().isCleartextTrafficPermitted(host)) {
   throw new RouteException(new UnknownServiceException(
   "CLEARTEXT communication to " + host + " not permitted by network security policy"));
}
```

如果请求是明文流量，默认情况下，在Android P版本Okhttp3就会抛出异常:

> CLEARTEXT communication to " + host + " not permitted by network security policy

#### **解决办法:**

##### **1.禁用掉明文流量请求的检查**

在 res 下新建一个 xml 目录，然后创建一个名为：network_security_config.xml 文件 ，该文件内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
<base-config cleartextTrafficPermitted="true" />
</network-security-config>
```

然后在 AndroidManifest.xml application 标签内应用上面的xml配置：

```xml
<application
    android:name=".App"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:networkSecurityConfig="@xml/network_security_config"
    android:roundIcon="@mipmap/ic_launcher_round"
    android:theme="@style/AppTheme"></application>
```

##### **2.推荐方式**

> 服务器和本地应用都改用 https

##### **3.修改应用目标版本**

> 将targetSdkVersion 降级回到 27

[🔝](#top)

### <a name = "2.2">Could not find com.android.tools.build:aapt2:3.2.0-alpha14-4748712.</a>

[地址](https://blog.csdn.net/lx6101989/article/category/7017765)android studio 升级到了3.0 取消了apt 报了这个错

```shell
Could not find com.android.tools.build:aapt2:3.2.0-alpha14-4748712.
Searched in the following locations:
  file:/D:/android_sdk/extras/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712.pom
  file:/D:/android_sdk/extras/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712-windows.jar
  file:/D:/android_sdk/extras/google/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712.pom
  file:/D:/android_sdk/extras/google/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712-windows.jar
  file:/D:/android_sdk/extras/android/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712.pom
  file:/D:/android_sdk/extras/android/m2repository/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712-windows.jar
  https://jcenter.bintray.com/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712.pom
  https://jcenter.bintray.com/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712-windows.jar
  https://jitpack.io/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712.pom
  https://jitpack.io/com/android/tools/build/aapt2/3.2.0-alpha14-4748712/aapt2-3.2.0-alpha14-4748712-windows.jar
```

在最上级的builde.gralde增加谷歌库 解决问题

```xml
allprojects {
  repositories {
  	google()//新增的
  	jcenter()
  }
}
```

[🔝](#top)

### <a name = "2.3">Android7.0调用相机 FileProvider.getUriForFile 报空指针</a>

做项目的时候遇到了问题，在7.0的安卓上使用FileProvider获取[content://Uri](content://Uri)的时候总是报空指针

```shell
NullPointerException: 'android.content.res.XmlResourceParser android.content.pm.PackageItemInfo.loadXmlMetaData(android.content.pm.PackageManager, java.lang.String)
```

跟踪方法到：

```shell
final ProviderInfo info = context.getPackageManager()
.resolveContentProvider(authority, PackageManager.*GET_META_DATA*);
```

这里info为null，所以会报空指针。

一般解决步骤有两个：

```
1、<provider>标签中的authorities有没有写错
2、<provider>标签需要写在<application>标签里面。
```

[🔝](#top)

### <a name = "2.4">app图标</a>

**可以修改`AndroidManifest.xml`的这个节点，a** 

`android:icon="@drawable/ic_launcher”`

然后mip文件下，修改图片和xml文件即可

[🔝](#top)

### <a name = "2.5">Android 动态设置padding跟margin的问题</a>

`textview.setPadding(120,0,0,0);//设置textview的位置`

一、使用方式：

1、padding:

`view.setPadding(int left, int top, int right, int bottom);`

2、margin:

```
LayoutParams lp = (LayoutParams) view.getLayoutParams();
lp.setMargins(int left, int top, int right, int bottom);
```

举个例子：

```xml
<LinearLayout
  android:id="@+id/ll"
  android:layout_width="match_parent"
  android:layout_height="wrap_content">
  <TextView
  android:id="@+id/tv"
  android:layout_width="wrap_content"
  android:layout_height="wrap_content"
  android:text="例子文字" />
</LinearLayout>
```

如果是margin的话，要注意view.getLayoutParams()是需要强制转换的，个人觉得是要看view的父元素是什么容器。

例如上面要对tv进行设置的话，应该是这样：

```xml
LinearLayout.LayoutParams lp = (LinearLayout.LayoutParams) tv.getLayoutParams();
lp.setMargins(int left, int top, int right, int bottom)
```

如果tv外面是RelativeLayout,那相应的(RelativeLayout.LayoutParams) tv.getLayoutParams();

二、单位问题：

1、padding:

我们可以定位到setPadding所在的View.class可以看到上面单位的描述，这里就看看paddingLeft，其他三个方向同理

```
/***
** The left padding in pixels, that is the distance in pixels between the*
** left edge of this view and the left edge of its content.*
** {**@hide**}*
**/
@ViewDebug.ExportedProperty(category = "padding")

protected int mPaddingLeft = 0;
```

看到源码中的注解pixels?这里表示的就是单位为px

2、margin:

其实跟padding差不多，不过就是setMargin是在ViewGroup.class中，但是不一样的是，setMargin是属于MarginLayoutParams.class内部类的。所以我们定位到这个内部类看下leftMargin，其他三个方向同理

```
/***
** The left margin in pixels of the child. Margin values should be positive.*
** Call {**@link* *ViewGroup#setLayoutParams(LayoutParams)} after reassigning a new value*
** to this field.*
**/*
@ViewDebug.ExportedProperty(category = "layout")
public int leftMargin;
```

看到源码中的注解pixels?这里表示的也是单位为px

三、处理适配：

如果我们直接在代码中设置两者的话，估计就是px单位了，说实话确实没错。不过去到其他分辨率的手机估计就变形了。这是为什么呢？你想想我们在布局中设置两者的时候是dip单位，在其他分辨率却没有问题，那你估计就发现了问题了。

是的，你想的没错。一般设置dip单位的话，是比较好适配的。

如果你不行的话，可以在布局中设置为px去不同分辨率手机试试看，完全变形。

px设置布局当初是我做项目的一个大坑。当我开发测试的时候很舒服， 没问题。可是到了项目快完成的时候，去了其他分辨率的试了下，变形了，内心千万个草泥马在奔腾。

说了这么多，就来说说怎么适配。其实很简单就是你在设置的时候dip转换为px.

```
/***
** dp转px*
***
*** *@param* *context*
*** *@param* *dpVal*
*** *@return*
**/*
public static int dp2px(Context context, float dpVal) {
return (int) TypedValue.applyDimension([TypedValue.COMPLEX_UNIT_DIP](http://typedvalue.complex_unit_dip/),
dpVal, context.getResources().getDisplayMetrics());
}
```

用法：

setPadding(int left, int top, int right, int bottom);这里我们就当成left要设置的dp2px(context，dpval)，margin也是同样的意思，最好都是设置dp转px。

[🔝](#top)

### <a name = "2.6">动态清空LinearLayout中的所有控件</a>

```java
  LinearLayout header_ll;//创建对象
  header_ll = (LinearLayout) findViewById(R.id.MyTable);//绑定控件
  header_ll.removeAllViews();//清空布局
```

[🔝](#top)

### <a name = "2.7">动态增加textView</a>

```xml
LinearLayout mainLinerLayout = (LinearLayout) this.findViewById(R.id.MyTable);
TextView textview=new TextView(this);
textview.setText(cursor.getString(3));
mainLinerLayout.addView(textview);
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fillViewport="true"
    android:scrollbars="none"
    >
    <HorizontalScrollView
        android:id="@+id/scroll_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scrollbarAlwaysDrawHorizontalTrack="false"
        android:scrollbars="none">

        <LinearLayout
            android:id="@+id/MyTable"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="9dp"
            android:orientation="vertical"
            >
        </LinearLayout>

    </HorizontalScrollView>
</ScrollView>
```

[🔝](#top)

### <a name = "2.8">SQL lite查询</a>

问题：当时刚接触sqlite和contentProvider时候记得cursor初始位置不正确 所以要moveToFirst 才能使cursor正确指向第一个位置。那么问题来了，遍历的时候要用moveToNext（在我印象中是同时使用的），所以脑海中默认写法是这样：

```java
if (cursor!=null){
try{
cursor.moveToFirst()
while(cursor.moveToNext()){
String address=cursor.getString(cursor.getColumnIndex(ContactsContract.CommonDataKinds.Email.ADDRESS));
Log.d(TAG, address);
}
}catch (Exception e){
e.printStackTrace();
}finally {
if (cursor!=null) {
cursor.close();
}
}
}
```

但是这样并不对啊，这样把第一条结果略过了！那么为什么去掉moveToFirst()就正确了呢？

```java
try{
//去掉moveToFirst
while(cursor.moveToNext()){
String address=cursor.getString(cursor.getColumnIndex(ContactsContract.CommonDataKinds.Email.ADDRESS));
Log.d(TAG, address);
}
}
```

先看下面这段代码：

```java
Cursor cursor=contentResolver.query(ContactsContract.CommonDataKinds.Email.CONTENT_URI,null,null,null,null);
Log.d(TAG,"cursor初始位置"+cursor.getPosition());
cursor.moveToFirst();
Log.d(TAG,"movetofirst的位置"+cursor.getPosition()+"");
```

就是把初始位置和moveToFirst的位置记录一下，看logcat显示：

cursor初始位置-1

movetofirst的位置0

也就是说：cursor初始位置是在-1,而数据是从0开始的，所以cursor.moveToNext刚好是从-1变成0，不需要moveToFirst而是直接循环moveToNext就可以完成遍历。

钻下牛角尖：那我想两者一起用怎么办？其实也没什么难。

```java
if (cursor!=null && cursor.moveToFirst()){
do {
String address = cursor.getString(cursor.getColumnIndex(ContactsContract.CommonDataKinds.Email.ADDRESS));
Log.d(TAG, address);
} while (cursor.moveToNext());
//或者
cursor.moveToFirst();
while(!cursor.isAfterLast()){
//dosomething
cursor.moveToNext();
}
/**
   \* Move the cursor to the first row.
   *
   \* <p>This method will return false if the cursor is empty.
   *
   \* @return whether the move succeeded.
   */
```

这是moveToFirst()的源码注释，是一个boolean值，如果是空（查询不到结果，与null区分）返回false,所以moveToFirst也可以当作判断条件。

```javs
WaterDB = new WaterDB(getActivity());
db = WaterDB.getWritableDatabase();
Cursor cursor = db.query("water",null,"data=?",new String[]{curDate},null,null,null);
Integer count = cursor.getCount();
if(count == 0){
  water_sum.setText("0");
  Toast.*makeText*(getActivity(),"没有数据",Toast.*LENGTH_SHORT*).show();
} else {
  Integer tempWater = 0;
  while(cursor.moveToNext()) {
  tempWater = tempWater + Integer.*parseInt*(cursor.getString((4)));
  }//通过循环，将所有的值相加
  water_sum.setText(String.*valueOf*(tempWater));
}
cursor.close();
db.close();
```

[🔝](#top)

### <a name = "2.9">**Android Studio新建empty activity，MainActivity.java报错，继承的AppCompatActivity红色字体报错，如何解决：**</a>

尝试办法但失败了：

点击file

![andriod_1_1](/Users/mayuan/Desktop/Hi-Story/github_blog/Blog/personalprojection/img/andriod_1_1.png)

点击箭头所示选择Invalidate and Restart：

![](/Users/mayuan/Desktop/Hi-Story/github_blog/Blog/personalprojection/img/android_1_2.png)

重启之后发现报错解决。



有效办法：

> File -- Other Settings -- Default Settings--
>
> Compiler -- Java Compiler --Project bytecode version选择版本最高的，然后重启项目就解决了。

[🔝](#top)

### <a name = "2.10">Fragment刷新</a>

```java
private boolean isFirstLoading = true;
/**
 * 在fragment可见的时候，刷新数据
 */
@Override
public void onResume() {
    super.onResume();
    if (!isFirstLoading) {
        find();
    }
    isFirstLoading = false;
}//在要刷新的页面
@Override
protected void onResume() {
    super.onResume();
    findInforSQL();//要刷新数据的函数
}//这个是activity刷新的页面，如果不对的话是证明你前面的数据库写错了，而不是这儿错了
```

[🔝](#top)

### <a name="2.11">数据库更新</a>

```java
values.put("name", name);
db.update("INFORMATION",values,"name=?",new String[]{tempName});
```

> name=? 是找到名字为这个的列 后面new String是name为这个值诗，put是要更新的数据，将此上传
> tempName是数据库中当前的值
> 也可以用id查找，即为_id=?   1+””  就自动转换成字符串了
> 还有数据删除的地方
> id会一直增加，不会因为delete而清空

### [🔝](#top)<a name="2.12">安卓去标题代码</a>

`<item name="windowNoTitle">true</item>`

在styles.xml的APPtheme中加这一句即可，其他的均不需要

### <a name="2.13">Fragment框架下控制其他Activity页面的监听</a>

```java
public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    //不同的Activity对应不同的布局
    View view = inflater.inflate(R.layout.activity_main2, container, false);
    ButterKnife.bind( this , view ) ;//摄者ButterKnife作为本页面的监听和当前视图的监听，而不需要setContentView(R.layout.id)作为
       //先前页面的监听
    return view;
}
```

### [🔝](#top)<a name="#2.14">五个页面跳转</a>

```java
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {
        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:{
                    return true;
                }
                case R.id.navigation_hobby:{
                    Intent intent = new Intent(MainActivity.this, Main2Activity.class);
                    startActivity(intent);
                    return true;
                }
                case R.id.navigation_photo:
                    mTextMessage.setText("相册");
                    return true;
                case R.id.navigation_resume:
                    mTextMessage.setText("简历");
                    return true;
                case R.id.navigation_account:
                    mTextMessage.setText("账户");
                    return true;
            }
            return false;
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }

}
```

[🔝](#top)

## <a name ="3">XML相关</a>

[🔝](#top)

### <a name ="3.1">drawable写一个圆.xml</a>

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval">
    <solid
        android:color="@color/blue"/>
    <size
        android:width="120dp"
        android:height="120dp"/>
</shape>
```

[🔝](#top)

### <a name="3.2">拖拉文件与AndroidManiFest.xml中文件上声明</a>

直接将文件拖进工程时，AndroidManiFest.xml是不会自动添加的，需要手动添加

[🔝](#top)

### <a name="3.3">圆弧按钮</a>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<shape
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <!-- 填充的颜色 -->
    <solid android:color="#6495ED" />
    <!-- 设置按钮的四个角为弧形 -->
    <!-- android:radius 弧形的半径 -->
    <corners android:radius="5dip" />

    <!-- padding：Button里面的文字与Button边界的间隔 -->
    <padding
        android:left="10dp"
        android:top="10dp"
        android:right="10dp"
        android:bottom="10dp"
        />
</shape>
<!—在drawable中建此文件，然后按钮那儿引用background即可—>
```

[🔝](#top)

### <a name="3.4">基本表格布局</a>

```xml
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fillViewport="false">
<TableLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layout_marginTop="0dp">

    <!--第一行-->
    <TableRow
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="0dp">
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_gravity="center_vertical"
            android:orientation="vertical"
            android:layout_marginLeft="0dp"
            android:layout_marginTop="0dp">
            <RelativeLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:layout_marginTop="0dp">
        </LinearLayout>
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_gravity="center_vertical"
            android:orientation="vertical"
            android:layout_marginLeft="4dp">
            <RelativeLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent">
            </RelativeLayout>
        </LinearLayout>
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_gravity="center_vertical"
            android:orientation="vertical"
            android:layout_marginLeft="4dp">
            <RelativeLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent">
            </RelativeLayout>
        </LinearLayout>
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_gravity="center_vertical"
            android:orientation="vertical"
            android:layout_marginLeft="3dp">
            <RelativeLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent">
            </RelativeLayout>
        </LinearLayout>
    </TableRow>
   </TableLayout>
</ScrollView>
```

### [🔝](#top)<a name="3.5">圆形头像</a>

在drawable文件中建.xml

```xml
<?xml version="1.0" encoding="utf-8"?>

<layer-list xmlns:android="http://schemas.android.com/apk/res/android" >
    <!-- 图层1(oval) -->
    <!-- left,top,right,bottom定义为-10，是为了扩大oval，达到覆盖四角的效果 -->
    <item android:left="-10dp" android:top="-10dp" android:right="-10dp" android:bottom="-10dp">
        <shape
            android:shape="oval">
            <!-- oval_inner[内部] -->
            <solid android:color="#F00" />
            <!-- oval_outer[边线] ，使用时改成父控件颜色即可-->
            <stroke
                android:width="10dp"
                android:color="#FFFFFF" />
            <!-- oval_inner_size[大小(除去边线)] ，也是最终裸露出来的圆形图像区域— >
            <size
                android:height="50dp"
                android:width="50dp" />
            <!-- 使oval_inner透明，裸露出将来设置的背景图片 -->
            <gradient android:centerColor="#0000" />
        </shape>
    </item>
</layer-list>
```

之后做如下设置

```xml
android:background="@drawable/aobama"
android:src="@drawable/round”/>  <!—来源用上面的round.xml，背景用要用到的头像—->
```

### [🔝](#top)<a name="3.6">页面下滑</a>

```xml
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fillViewport="false”>
</ScrollView>
```

[🔝](#top)

## <a name="4">开源项目</a>

[🔝](#top)

### <a name="4.1">时间和选项选择</a>

#### [项目地址](https://github.com/Contrarywind/Android-PickerView)

##### 例子：生日选择

###### 依赖项

``implementation 'com.contrarywind:Android-PickerView:4.1.8'``

```java
import com.bigkoo.pickerview.view.TimePickerView;
import com.bigkoo.pickerview.builder.TimePickerBuilder;
import com.bigkoo.pickerview.listener.OnTimeSelectListener;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
    private void showTimePicker() {
        //时间选择器
        TimePickerView pvTime = new TimePickerBuilder(this, new OnTimeSelectListener() {
            @Override
            public void onTimeSelect(Date date, View v) {
                user_birth.setText(getTime(date));
            }
        })
                .setSubmitText("确定")//确定按钮文字
                .setCancelText("取消")//取消按钮文字
                .setTitleText("生日选择")//标题
                .build();
        pvTime.show();
    }
    private String getTime(Date date) {//可根据需要自行截取数据显示
//        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        return format.format(date);
    }
```

