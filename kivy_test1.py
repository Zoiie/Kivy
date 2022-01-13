from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
    	#建立网格布局
    	#cols表示水平布局容纳的部件个数，超过总部件以后不会再增加网格格数
        layout=GridLayout(cols=2)
        btn=Button(text="hello",font_size=100)
        btn1=Button(text="kivy",font_size=50)
        btn2=Button(text="Cleck",font_size=150)
        btn3 = Button(text="again", font_size=50)
        layout.add_widget(btn)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

if __name__=="__main__":
    GridLayoutApp().run()
