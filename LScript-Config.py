from tkinter import *
from tkinter import ttk
import keyboard



def global_run():
    #root.withdraw()
    bkb = ent1.get()
    blink = ent2.get()
    eul = ent3.get()
    skill1 = ent4.get()
    ult = ent5.get()
    total = ent6.get()

    


    def function():
        keyboard.send(bkb)#bkb
  
        keyboard.send(blink)#blink

        keyboard.send(eul)#bm
        
        keyboard.send(skill1)#1 skill

        keyboard.send(ult)#
        
  
        



    keyboard.wait(total)
    keyboard.add_hotkey(total, function)

root = Tk()
root.resizable(0,0)
root.geometry('300x320')
lab = Label(root, text='LEGION BINDS', font='Arial 20 bold')
lab.pack()

lab1 = Label(root, text='bind B-K-B')
lab1.pack()
ent1 = ttk.Entry(root)
ent1.pack()

lab2 = Label(root, text='bind blink')
lab2.pack()
ent2 = ttk.Entry(root)
ent2.pack()

lab3 = Label(root, text='bind BM')
lab3.pack()
ent3 = ttk.Entry(root)
ent3.pack()

lab4 = Label(root, text='bind 1 skill')
lab4.pack()
ent4 = ttk.Entry(root)
ent4.pack()

lab5 = Label(root, text='bind ult')
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