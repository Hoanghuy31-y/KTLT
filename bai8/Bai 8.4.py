print("Sinh vien: Nguyen Hoang Huy")
print("MSSV: 245752021610060")
print("######################")


from tkinter import *


window = Tk()
window.title("Ví dụ Tkinter")
window.geometry("350x200")


lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!!")


btn = Button(window,
             text="Click Me",
             command=clicked,
             bg="lightblue",   
             fg="red")        
btn.grid(column=1, row=0)


window.mainloop()
