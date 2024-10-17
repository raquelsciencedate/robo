#import a biblioteca de automação pip install
import pyautogui
import pyautogui as auto

auto.PAUSE = 0.9                

                    
#pedindo para o programa abrir o edge
auto.press("win")
auto.write("edge")
auto.press("enter")

auto.write("python.org")
auto.press("enter")
auto.hotkey("ctrl","t")
auto.write("google.com.br")
auto.press("enter")
auto.write("logo python")
auto.press("enter")


for i in range(13):
    auto.press("tab")
    
auto.press("enter")


