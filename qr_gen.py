from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
import qrcode
import os
import sys

class Function(ScreenManager):
    def qrgen(self, root):
        if self.ids.link.text != '':
            code = qrcode.QRCode(version=1.0, box_size=15, border=4)
            code.add_data(self.ids.link.text)
            code.make(fit=True)
            img = code.make_image()
            img.save("qr.png")
        

    def viewimg(self,root):
        self.ids.qr.source = "qr.png"
        root.current = "im"
        os.remove("qr.png")

    def restart(self):
        self.stop()
        return Function().run()

    def try_again(self,root):
        self.ids.link.text = ""
        root.current = "home"
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

class Main(MDApp):
    Builder.load_file('layout.kv')
    def build(self):
        return Function()

Main().run()