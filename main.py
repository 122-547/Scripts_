from tkinter import *
from tkinter import ttk
import os
def click1():
    
    os.system('python EScript-Config.py')


def click2():
    
    os.system('python SFScript-Config.py')

def click3():
    
    os.system('python LScript-Config.py')
    


root = Tk() 
root.resizable(0,0)
os.system('cd Script-Config')
root.geometry('85x110')
classF = [click1, click2, click3]
classN = ['Enigma', 'SF', 'Legion']
classUN = ['but1', 'but2', 'but3']
y = 5
#root.overrideredirect(1)

for i in range(0, 3):
    
    classU = classUN[i]
    classU = ttk.Button(root, text=classN[i], command=classF[i])
    classU.place(y=y, x=5, height=30)
    y += 35
    print(classF[i], classUN[i], classN[i])
    
    
    

root.mainloop()