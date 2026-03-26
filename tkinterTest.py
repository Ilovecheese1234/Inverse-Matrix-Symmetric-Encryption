from tkinter import *

window = Tk()
photo = PhotoImage(
    file='image/arrow.png'
)


label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=10,
              image=photo,
              compound='bottom'
              )
label.pack()

def getSubmit():
    username = entry.get()
    print(username)

count = 0

def getSubmit():
    username = entry.get()
    print(username)

def deleteSubmit():
    entry.delete(0,END)

def backSubmit():
    entry.delete(len(entry.get())-1,END)
buttonSubmit = Button(
    window,
    text="submit",
    fg="green",
    activeforeground='green',
    activebackground='green',
    command= getSubmit,
    compound="right"
)

buttonDelete = Button(
    window,
    text="delete",
    command = deleteSubmit
)
buttonBackspace = Button(
    window,
    text="backspace",
    command= backSubmit
)

entry = Entry(
    window,
    font=('Arial',18),
)


def display():
    if(x.get()==1):
        print("you agreee")
    else:
        print("You disagree :(")
x = IntVar()
check_button = Checkbutton(
    window,
    text="Hello World",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display
)

food = ["pizza","hamburger","hotdog"]

entry.pack()
buttonSubmit.pack(anchor="center")
buttonDelete.pack(anchor="center")
buttonBackspace.pack(anchor="center")
check_button.pack()

def getOrder():
    print(y.get())

y = IntVar()
for i in range(len(food)):
    radioButton = Radiobutton(
        window,
        text=food[i],
        variable=y,
        value = i,
        command = getOrder
    )
    radioButton.pack()


scale = Scale(
    window,
    from_=0,
    to=105,
    orient="vertical",
    font=("Arial",10),
    tickinterval = 50,
    
)


def submit():
    print("the temp is "+str(scale.get())+" degree Celcius")
    print(listbox.get(listbox.curselection()))
button2 = Button(
    window,
    text="submit",
    command = submit,
)
scale.pack()
button2.pack()

    


listbox = Listbox(
    window,
    bg="#f7ffde",
    font=("Constantia",35),
    width=12
)

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")
listbox.place(x=200,y=100)

listbox.config(
    height=listbox.size()
)
def addFood():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(
        height = listbox.size()
    )
entryBox = Entry(window)
addButton = Button(window,text="Add",command=addFood)
addButton.pack()
entryBox.pack()

window.mainloop()