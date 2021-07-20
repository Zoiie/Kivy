# Python Kivy（App开发） Windows安装打包步骤

学了很久的深度学习，一直在电脑上折腾，希望能拿到手机上做点玩具，于是我尝试寻找在python上制作App的方法。于是向我的老师求助，他告诉我在欧洲大家会用kivy创建移动端应用来在移动端实现自己的想法。于是我在试着在国内找这方面的资料，可惜很少，大部分都是重复且零散的。于是我慢慢摸索，暂时找到了适合现在（2020.7）的安装实现步骤。希望能帮到大家，kivy还是比较好玩的一个模块哈哈。

## 一、准备工具


 1. **Pycharm** ，也可以用**Jupyter**或者其它编辑器代替，只是一个编辑器罢了；
 2. 虚拟机**[VirtualBox](https://www.virtualbox.org/wiki/Downloads)**，我下载的是Windows平台的；
 3. 插件：**[Oracle_VM_VirtualBox_Extension_Pack-4.3.12-93733.vbox-extpack](https://download.virtualbox.org/virtualbox/4.3.12/)**，**kivydev.ova(VirtualBox附带)**；
 

## 二、安装kivy
可以在CMD运行框内键入pip install指令安装kivy，然后用在Jupyter上进行编辑。由于我用的编辑器主要是Pycharm，所以我在Pycharm上安装。

   1.在cmd命令框内键入（使用Jupyter的用户参考）


```python
pip install Kivy-1.11.1-cp37-cp37m-win_amd64.whl
pip install kivy_deps.glew-0.2.0-cp37-cp37m-win_amd64.whl
pip install kivy_deps.gstreamer-0.2.0-cp37-cp37m-win_amd64.whl
pip install kivy_deps.sdl2-0.2.0-cp37-cp37m-win_amd64.whl
```

2.在Pycharm里安装kivy
![angle也可以不安装](https://img-blog.csdnimg.cn/20200727164459203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
*[注]angle也可以不安装*

或者在Pycharm的命令框里安装，和CMD里安装是一样的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727164809580.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
同样在里面键入

```python
pip install Kivy-1.11.1-cp37-cp37m-win_amd64.whl
pip install kivy_deps.glew-0.2.0-cp37-cp37m-win_amd64.whl
pip install kivy_deps.gstreamer-0.2.0-cp37-cp37m-win_amd64.whl
pip install kivy_deps.sdl2-0.2.0-cp37-cp37m-win_amd64.whl
```


## 三、安装虚拟机
1.下载VirtualBox以后，安装到自定义的目录下（强烈建议全英文）

2.安装插件：双击Oracle_VM_VirtualBox_Extension_Pack-4.3.12-93733.vbox-extpack文件，就能安装。
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727165445777.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
## 四、建立共享文件夹
因为虚拟机无法和Windows直接交互，所以文件传输必须依靠**共享文件夹**进行）。

我在这里创建了一个**VirtualDisk**文件夹作为**共享文件夹**
【这一步可以理解为创建一个空白文件夹】，我们需要记住它的位置。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727170736955.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
然后将之前下载好的kivydev.ova复制到这个文件夹里（不复制也可以，但是要保证所有文件的路径都是英文路径）

## 五、导入kivydev.ova系统
安装完成的虚拟机是没有任何系统的，此时需要导入kivydev.ova系统。![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727165730778.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
在【管理】菜单下，点击【导入虚拟电脑】
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727165841259.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
选择下载好的kivydev.ova文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727170100677.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
导入
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727171706815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
等两三分钟就可以完成导入。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727171751618.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
导入完成。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727171906121.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)



## 六、配置虚拟机
点击**设置**，进入虚拟机的设置界面，然后找到最下面的【**共享文件夹**】，点击右边的加号，添加共享文件夹位置。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727172314902.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
粘贴我们之前创建的【共享文件夹】位置，将【自动挂载】打勾，点击确定，配置完成。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727172452119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
*其它配置可以调节运行内存（我比较喜欢设为1024），显存（我设置为128）等等，也可以不动。*

至此，我们已经完成了kivy安装和虚拟机部分的安装，接下来就要写一个写一个程序，进行打包测试。

## 七、编辑一个kivy程序进行测试
可以将我的代码复制到Pycharm里进行编译，编译没问题的话将文件复制到共享文件夹内，重命名为“main.py”，方便下一步在虚拟机内进行调用。
*这是一个简易画板功能的代码。*
```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from random import random
from kivy.uix.button import Button

class MyWidgetWidget(Widget):
    def on_touch_down(self, touch):
        color=(random(),random(),random())
        with self.canvas:
            Color(*color)
            touch.ud['Line']=Line(points=(touch.x,touch.y),width=5)

    def on_touch_move(self, touch):
        touch.ud['Line'].points=touch.ud['Line'].points+[touch.x,touch.y]

class MyPaintApp(App):
    def build(self):
        parent=Widget()
        self.painter=MyWidgetWidget()
        clearbtn=Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__=="__main__":
    MyPaintApp().run()
```
运行效果(按住鼠标左键随便在画布上画几笔）：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727202242990.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727173514553.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)



## 八、打包成Apk文件
打开我们创建完成的虚拟机。点击**启动**。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727192414708.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
加载会比较慢，耐心等待到进入Linux桌面。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727192833774.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)

如果出现错误，cancel掉就可以继续了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727192756399.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
打开桌面的**File System**，接着点击左边栏**sf_VirtualDisk**（我们之前创建的共享文件夹）。里面有我们保存的"main.py"和"kivydev.ova"。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727192958915.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
点击左边栏kivydev目录下找到kivy，在kivy目录下进入accordion。再将"main.py"复制到当前目录下（即**/home/kivydev/kivy/accordion/**目录下）。它会覆盖此目录下的示例——一个main.py文件。因为打包的时候，主程序的名字都是main.py。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727193400548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
右击空白区域，打开 **Open Terminal Here**命令框。
![在这里插入图片描述](https://img-blog.csdnimg.cn/202007271940279.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020072719415625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
（**如果目录下没有buildozer.spec文件，执行这一步**）在此框内键入

```python
buildozer init
```
生成一个**buildozer.spec**文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727194548685.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
接着再输入命令

```python
gedit buildozer.spec
```
打开buildozer.spec文件，主要修改**Title**(应用名字，我设置为SamplePainter)，**package.name**(打包名，同样设置成SamplePainter)，**package.domain**(打包成哪一种ios或者安卓，这里我不改，默认打包成安卓文件)。其余的建议暂时不要修改。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727194911325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
修改完成后保存 **Save**，关闭文件，回到命令框。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727195549812.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
在命令框内键入：

```python
buildozer android_new debug
```

进行打包，此过程需要等待几分钟。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727200200963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
打包完成，按照提示的地址寻找打包后的文件。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727200930647.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
关闭命令框，在bin文件夹下看见我们的应用**SamplePainter**，另一个MyApplication是示例文件，不予理会。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727201112598.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
把这个文件复制到共享文件夹内。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727201350852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)

## 九、发送到手机并安装
回到Windows，打开我们的共享文件夹**VirtualDis**，可以看见创建的SamplePainter.apk文件。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727201846161.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
把文件发送到手机，【注意】如果文件名后缀不是apk，请手动重命名为apk后缀。安装到手机。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727202407734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)

打开App，看看效果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200727202713666.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MDMwNDAw,size_16,color_FFFFFF,t_70)
还可以。

## 十、总结
kivy功能不算强大，但是很便捷，可以把想法快速部署到移动端，希望大家创造自己独特的App！有空再写写我的kivy小项目嘿嘿！
