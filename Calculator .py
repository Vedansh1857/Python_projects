from tkinter import *

root =Tk()
root.geometry("544x900")
root.title("Calculator in Tkinter")
root.wm_iconbitmap("1.ico")

def click(event):
    global value
    text = event.widget.cget("text")
    if text == "=":
        if value.get().isdigit():
            item = int(value.get())
        else:
            try:
                item = eval(myentry.get())
            except Exception as e:
                print(e)
                item = "ERROR"
                
        value.set(f"{value.get()} = {item}")
        myentry.update()

    elif text == "C":
        value.set("")
        myentry.update()
    else:
        value.set(value.get() + text)
        myentry.update()

value = StringVar()
myentry = Entry(root, textvariable=value, font="lucida 30 bold")
myentry.pack(pady=20, fill=X, padx=20, ipady=8)

f1 = Frame(root, bg="grey")
b = Button(f1, text="9", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f1, text="8", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f1, text="7", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f1.pack()

f2 = Frame(root, bg="grey")
b = Button(f2, text="6", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f2, text="5", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f2, text="4", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f2.pack()

f3 = Frame(root, bg="grey")
b = Button(f3, text="3", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f3, text="2", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f3, text="1", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f3.pack()

f5 = Frame(root, bg="grey")
b = Button(f5, text="=", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f5, text="C", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f5, text="0", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f5.pack()

f4 = Frame(root, bg="grey")
b = Button(f4, text=".", padx=16, pady=10, font="comicsansms 25 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f4, text="00", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f4, text="%", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f4.pack()

f6 = Frame(root, bg="grey")
b = Button(f6, text="+", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f6, text="-", padx=16, pady=10, font="comicsansms 25 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f6, text="*", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)

b = Button(f6, text="/", padx=16, pady=10, font="comicsansms 17 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, pady=12, padx=18)
f6.pack()

root.mainloop()