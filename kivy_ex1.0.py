# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.properties import ListProperty
# import kivy
#
# class RootWidget(BoxLayout):
#     def __init__(self,**kwargs):
#         super(RootWidget,self).__init__(**kwargs)
#         self.add_widget(Button(text="btn 1"))
#         cb=CustomBtn()
#         cb.bind(pressed=self.btn_pressed)
#         self.add_widget(cb)
#         self.add_widget(Button(text="btn 2"))
#
#     def btn_pressed(self,instance,pos):
#         print("pos:printed from root widget:{pos}".format(pos=pos))
#
# class CustomBtn(Widget):
#     pressed=ListProperty([0,0])
#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             self.pressed=touch.pos
#             return True
#         return super(CustomBtn, self).on_touch_down(touch)
#
#     def on_pressed(self,instance,pos):
#         print("pressed at {pos}".format(pos=pos))
#
# class TestApp(App):
#     def build(self):
#         return RootWidget()
#
# if __name__=="__main__":
#     TestApp().run()


# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.image import Image
# from kivy.properties import ObjectProperty
# from kivy.lang import Builder
#
#
# Builder.load_string('''
# <CustomLayout>
#     canvas.before:
#         BorderImage:
#             # BorderImage behaves like the CSS BorderImage
#             border: 10, 10, 10, 10
#             texture: self.background_image.texture
#             pos: self.pos
#             size: self.size
#
# <RootWidget>
#     CustomLayout:
#         size_hint: .9, .9
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         rows:1
#         Label:
#             text: "I don't suffer from insanity, I enjoy every minute of it"
#             text_size: self.width-20, self.height-20
#             valign: 'top'
#         Label:
#             text: "When I was born I was so surprised; I didn't speak for a year and a half."
#             text_size: self.width-20, self.height-20
#             valign: 'middle'
#             halign: 'center'
#         Label:
#             text: "A consultant is someone who takes a subject you understand and makes it sound confusing"
#             text_size: self.width-20, self.height-20
#             valign: 'bottom'
#             halign: 'justify'
# ''')
#
#
# class CustomLayout(GridLayout):
#
#     background_image = ObjectProperty(
#         Image(
#             source='jian,jpg'
#             ))
#
#
# class RootWidget(FloatLayout):
#     pass
#
#
# class MainApp(App):
#
#     def build(self):
#         return RootWidget()
#
# if __name__ == '__main__':
#     MainApp().run()


with self.canvas:
   # draw a line using the default color
   # 用默认颜色画一条线
   Line(points=(x1, y1, x2, y2, x3, y3))

   # lets draw a semi-transparent red square
   # 接下来画一个半透明的红方块
   Color(1, 0, 0, .5, mode='rgba')
   Rectangle(pos=self.pos, size=self.size)