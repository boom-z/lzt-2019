import tkinter as tk

window = tk.Tk()
window.title('my window') # 窗口名字
window.geometry('200x200')

#canvas = tk.Canvas(window, height=150, width=500)
canvas=tk.Canvas(window,bg='blue',height=100,width=200)
image_file=tk.PhotoImage(file='ins.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.grid(row=1, column=1)
#tk.Label(window, text='1').pack(side='top')
#tk.Label(window, text='1').pack(side='bottom')
#tk.Label(window, text='1').pack(side='left')
#tk.Label(window, text='1').pack(side='right')

#for i in range(4):
#    for j in range(3):
       # tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
        #tk.Label(window, text=1).grid(row=i, column=j, ipadx=10, ipady=10)
        #按几行几列的格子放置

#tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()
