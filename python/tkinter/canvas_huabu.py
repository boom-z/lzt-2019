import tkinter as tk

window=tk.Tk()   #建立窗口
window.title('my window') # 窗口名字
window.geometry('200x200')#窗口大小


canvas=tk.Canvas(window,bg='blue',height=100,width=200)
image_file=tk.PhotoImage(file='ins.gif')

image=canvas.create_image(0,0,anchor='nw',image=image_file)

x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)#划线
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')#圆形
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,fill='red',start=0,extent=180)#扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20) #长方形

canvas.pack()
#canvas.place(x=20, y=10, anchor='nw')
def moveit():
    canvas.move(image,2,2)
b=tk.Button(window,text='move',command=moveit).pack()
window.mainloop()
