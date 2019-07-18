import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x200')#窗口大小


var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0)&(var3.get() == 0):
        l.config(text='you have selected A')
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() ==0):
        l.config(text='you have selected B')
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() ==1):
        l.config(text='you have selected C')
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() ==0):
        l.config(text='you have selected AB')
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() ==1):
        l.config(text='you have selected BC')
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() ==1):
        l.config(text='you have selected AC')
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() ==0):
        l.config(text='you have selected ')
    else:
        l.config(text='you have selected ABC')
        
r1=tk.Radiobutton(window,text='Option A',
                  variable=var1,onvalue=1,offvalue=0,
                  command=print_selection)
r1.pack()

r2=tk.Radiobutton(window,text='Option B',
                  variable=var2,onvalue=1,offvalue=0,
                  command=print_selection)
r2.pack()

r3=tk.Radiobutton(window,text='Option C',
                  variable=var3,onvalue=1,offvalue=0,
                  command=print_selection)
r3.pack()

window.mainloop()
