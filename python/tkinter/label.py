import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x100')#窗口大小


var=tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,
           height=2)
l.pack()#放置label

on_hit=False  # 控制是否显示


def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
    
b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)#点击就运行hit_me

b.pack()

window.mainloop()#不断刷新
