from kivy.config import Config
Config.set('graphics', 'resizable', '1') 
Config.set('graphics', 'width', '400')    
Config.set('graphics', 'height', '400')


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
Window.title = "X AND O"
'''Config.set('graphics', 'resizable', '1') 
Config.set('graphics', 'width', '400')    
Config.set('graphics', 'height', '400')
Config.write()'''


class Main(Screen):
    pass

class GameWindow(Screen):
    pass

class Manager(ScreenManager):
    pass

class MainApp(MDApp):
    w = False
    def build(self):
        self.title = "X And O"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.trun = "X"
        

        return Builder.load_file("tool.kv") 

    
    def restart(self):
        for i in range(1,10):
            btn = self.game_screen.ids[f"b{i}"]
            btn.text =""
            btn.disabled = False
        self.main = self.root.get_screen("main")    
        use = self.main.ids.use.text    
        self.game_screen.ids.head.text =f"Hello {use.title()}" 
        self.w = False   

    def diabel(self):
        for i in range(1,10):
            btn = self.game_screen.ids[f"b{i}"]
            btn.disabled = True
    def draw(self):      
        if self.w == False and \
            (self.game_screen.ids.b1.disabled==True and \
            self.game_screen.ids.b2.disabled==True and \
            self.game_screen.ids.b3.disabled==True and \
            self.game_screen.ids.b4.disabled==True and \
            self.game_screen.ids.b5.disabled==True and \
            self.game_screen.ids.b6.disabled==True and \
            self.game_screen.ids.b7.disabled==True and \
            self.game_screen.ids.b8.disabled==True and \
            self.game_screen.ids.b9.disabled==True): 
            self.game_screen.ids.head.text = "game is draw".title()

    def end_game(self,a,b,c):
        a.color =  0,1,0,1
        b.color =  0,1,0,1
        c.color = 0,1,0,1
        self.diabel()
        self.game_screen.ids.head.text = f"{a.text} WIN!!"
    def win(self):
        if self.game_screen.ids.b1.text != "" and self.game_screen.ids.b1.text == self.game_screen.ids.b2.text and self.game_screen.ids.b2.text ==self.game_screen.ids.b3.text:
            self.w = True
            self.end_game(self.game_screen.ids.b1,self.game_screen.ids.b2,self.game_screen.ids.b3)
        
        if self.game_screen.ids.b4.text != "" and self.game_screen.ids.b4.text == self.game_screen.ids.b5.text and self.game_screen.ids.b5.text ==self.game_screen.ids.b6.text:
            self.w = True
            self.end_game(self.game_screen.ids.b4,self.game_screen.ids.b5,self.game_screen.ids.b6) 
        
        if self.game_screen.ids.b7.text != "" and self.game_screen.ids.b7.text == self.game_screen.ids.b8.text and self.game_screen.ids.b8.text ==self.game_screen.ids.b9.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b7,self.game_screen.ids.b8,self.game_screen.ids.b9)
        
        if self.game_screen.ids.b1.text != "" and self.game_screen.ids.b1.text == self.game_screen.ids.b5.text and self.game_screen.ids.b5.text ==self.game_screen.ids.b9.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b1,self.game_screen.ids.b5,self.game_screen.ids.b9)
        
        if self.game_screen.ids.b3.text != "" and self.game_screen.ids.b3.text == self.game_screen.ids.b5.text and self.game_screen.ids.b5.text ==self.game_screen.ids.b7.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b3,self.game_screen.ids.b5,self.game_screen.ids.b7)
        
        if self.game_screen.ids.b1.text != "" and self.game_screen.ids.b1.text == self.game_screen.ids.b4.text and self.game_screen.ids.b4.text ==self.game_screen.ids.b7.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b1,self.game_screen.ids.b4,self.game_screen.ids.b7) 
        
        if self.game_screen.ids.b2.text != "" and self.game_screen.ids.b2.text == self.game_screen.ids.b5.text and self.game_screen.ids.b5.text ==self.game_screen.ids.b8.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b2,self.game_screen.ids.b5,self.game_screen.ids.b8) 
        
        if self.game_screen.ids.b3.text != "" and self.game_screen.ids.b3.text == self.game_screen.ids.b6.text and self.game_screen.ids.b6.text ==self.game_screen.ids.b9.text:
            self.w  =True
            self.end_game(self.game_screen.ids.b3,self.game_screen.ids.b6,self.game_screen.ids.b9)
        else:
            self.draw()


    def Board(self,BNO):
        
        if self.trun == "X":
            BNO.text = "X"
            self.trun = "O"

        else:
            BNO.text = "O"
            self.trun = "X" 
        self.game_screen.ids.head.text = f"{self.trun}'s Trun"   
        BNO.disabled = True
        BNO.color = [1, 0.6470588, 0, 1]

        self.win()


                         
    
    def Hi(self,use):
        self.game_screen = self.root.get_screen("gamewindow")
        self.game_screen.ids.head.text = f'Hello {use.text.title()}'

if __name__=="__main__":

    MainApp().run()
