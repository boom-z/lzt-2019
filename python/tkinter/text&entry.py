import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x200')#窗口大小

def insert_point():
    var=e.get()  #获取输入值
    t.insert('insert',var)  #插入到光标处
def insert_end():
    var=e.get()
    t.insert('end',var)
def insert_second():
    var=e.get()
    t.insert(2.0,var)

#e=tk.Entry(window,show='*')  #show表示输入后显示形式
e=tk.Entry(window,show=None)  #show表示输入后显示形式
e.pack()

    
b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)#点击就运行hit_me

b1.pack()
b2=tk.Button(window,text='insert end',width=15,height=2,command=insert_end)#点击就运行hit_me

b2.pack()

b3=tk.Button(window,text='insert second',width=15,height=2,command=insert_second)#点击就运行hit_me

b3.pack()


t=tk.Text(window,height=2)
t.pack()

window.mainloop()#不断刷新
