from kivy.app import App
from kivy.uix.checkbox import CheckBox

# class CheckboxApp(App):
#     def build(self):
#         def on_checkbox_active(checkbox,value):#定义选择框函数，输入checkbox是选择框，value是选择框状态
#             if value:#value是选择状态，True表示勾选，False表示不勾选
#                 print("勾选",checkbox)
#             else:
#                 print("不勾选",checkbox)
#
#         checkbox=CheckBox()#定义一个Checkbox
#         checkbox.bind(active=on_checkbox_active)#将状态绑定到checkbox上
#         return checkbox
#
# if __name__=="__main__":
#     CheckboxApp().run()

from kivy.app import App
from kivy.uix.image import Image
import os

class ImageApp(App):
    def build(self):

        img=Image(source=f)#载入图片
        return img

if __name__=="__main__":
    Address = input("请输入需要转换的文件所在文件夹地址：")  # 输入文件地址
    docunames = os.listdir(Address)
    for f in docunames:
        ImageApp().run()
