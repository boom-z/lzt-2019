import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x200')#窗口大小


var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected '+var.get()) #可以改变label参数


r1=tk.Radiobutton(window,text='Option A',
                  variable=var,value='A',
                  command=print_selection)
r1.pack()

r2=tk.Radiobutton(window,text='Option B',
                  variable=var,value='B',
                  command=print_selection)
r2.pack()

r3=tk.Radiobutton(window,text='Option C',
                  variable=var,value='C',
                  command=print_selection)
r3.pack()

window.mainloop()
