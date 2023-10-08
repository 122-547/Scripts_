from tkinter import *
from tkinter import ttk
import keyboard
from time import sleep


def global_run():
    #root.withdraw()
    bkb = ent1.get()
    refresh = ent2.get()
    blink = ent3.get()
    skill3 = ent4.get()
    ult = ent5.get()
    total = ent6.get()

    print(bkb, refresh, blink, skill3, ult, total)


    def function():
        keyboard.send(bkb)#bkb
  
        keyboard.send(blink)#blink

        keyboard.send(skill3)#3 skill
   
        keyboard.send(ult)#ult
        sleep(4.8)
  
        keyboard.send(refresh)#refresher
        sleep(0.1)
        keyboard.send(bkb)#bkb
        sleep(0.1)
        keyboard.send(ult)#ult



    keyboard.wait(total)
    keyboard.add_hotkey(total, function)

root = Tk()
root.resizable(0,0)
root.geometry('300x320')
lab = Label(root, text='ENIGMA BINDS', font='Arial 20 bold')
lab.pack()

lab1 = Label(root, text='bind B-K-B')
lab1.pack()
ent1 = ttk.Entry(root)
ent1.pack()

lab2 = Label(root, text='bind blink')
lab2.pack()
ent2 = ttk.Entry(root)
ent2.pack()

lab3 = Label(root, text='bind 3 skill')
lab3.pack()
ent3 = ttk.Entry(root)
ent3.pack()

lab4 = Label(root, text='bind ult')
lab4.pack()
ent4 = ttk.Entry(root)
ent4.pack()

lab5 = Label(root, text='bind refresher')
lab5.pack()
ent5 = ttk.Entry(root)
ent5.pack()

lab6 = Label(root, text='bind TotalKey')
lab6.pack()
ent6 = ttk.Entry(root)
ent6.pack()

but = ttk.Button(root, text='Подтвердить', command=global_run)
but.pack()

root.mainloop()