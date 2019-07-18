import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x200')#窗口大小


l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected '+v) #可以改变label参数

s=tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,
           length=200,showvalue=0,tickinterval=3,resolution=0.01,
           command=print_selection)
           #orient  显示方向 tickinterval 标签单位长度 resolution 小数位数
s.pack()

window.mainloop()
