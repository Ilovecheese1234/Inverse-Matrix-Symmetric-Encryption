from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import encryption

def addTitle(window):
    title = LabelFrame(
        window,
        text="IMAE Interface",
        font=('Segoul',15,'bold'),
        fg="cyan",
        bg="black",
        pady=10
    )

    title.grid(column=0,row=0,columnspan=3, rowspan = 2, sticky="NESW")

    title.columnconfigure(0,weight=1)
    title.columnconfigure(1,weight=1)
    title.columnconfigure(2,weight=1)

    title.rowconfigure(0,weight=1)
    title.rowconfigure(1,weight=1)

def addPubKeyLabel(title):
    pubKeyLabel = Label(
        title,
        text= encryption.getText(),
        height=1,
        bg="black",
        fg="white",
        font=('Segol',13),
        pady=10,
    )
    pubKeyLabel.grid(column=0,row=0,columnspan=3)
    return pubKeyLabel

def addInputFrame(window):
    input = LabelFrame(
        window,
        fg="cyan",
        text="Your Message: ",
        font=('Segoul',15,'bold'),
        bg="black",
    )

    input.grid(column=0,row=2, columnspan=2, sticky="NESW")

    input.columnconfigure(0,weight=1)
    input.rowconfigure(0,weight=1)
    return input

def addInputTextbox(frame):
    inputText = Text(
        frame,
        height=1,
        width=1,
        font=('Segol',13),
        padx=10,
        pady=10,
        bg="black",
        fg="white",
        border=0,
        insertbackground="white"
    )
    inputText.grid(column=0,row=0,sticky="EWNS")
    return inputText

def addEncryprionSelectionFrame(window):
    encryptSelection = Frame(
        window,
        bg="black",
    )
    encryptSelection.grid(column=0,row=4,sticky="NEWS")
    encryptSelection.columnconfigure(0,weight=1)
    encryptSelection.columnconfigure(1,weight=1)
    return encryptSelection


def addModeRadioButtons(frame):
    selection = ["Encryption (Please Select a Recipient)","Decryption"]
    x=IntVar()
    for i in range(len(selection)):
        encryptButton = Radiobutton(
            frame,
            text=selection[i],
            variable=x,
            value=i,
            bg="black",
            fg="cyan",
            selectcolor="black",
            font=("Segol",10)
        )
        encryptButton.grid(column=i,row=0,sticky="NEWS")
    return encryptButton,x


def addOutputFrame(window):
    output = LabelFrame(
        window,
        text="Ciphered Text",
        font=("Segol",15,"bold"),
        bg="black",
        fg="cyan"
    )
    output.grid(column=0,row=6,columnspan=2,sticky="NEWS")
    output.columnconfigure(0,weight=1)
    output.rowconfigure(0,weight=1)
    return output


def addOutputTextBox(frame):
    outputText = Text(
        frame,
        font=("Segol",13),
        bg="black",
        fg="white",
        border=0,
        width=1,
        height=1,
        padx=10,
        pady=10,
    )
    outputText.grid(column=0,row=0,columnspan=2,sticky="NEWS")
    return outputText

def addReceiverFrame(window):
    receiver = LabelFrame(
        window,
        fg="cyan",
        bg="black",
        text="Recipient",
        font=("Segol",15,"bold"),
    )
    receiver.grid(column=2,row=2,rowspan=4,sticky="NEWS")
    receiver.columnconfigure(0,weight=1)
    receiver.rowconfigure(0,weight=1)
    return receiver

def addReceiverList(frame):
    receiverList = ttk.Treeview(
        frame,

    )

    receiverList['columns'] = ("#1")
    receiverList.column("#0",width=1,anchor="center")
    receiverList.column("#1",width=1,anchor="center")

    receiverList.heading("#0",text="Name")
    receiverList.heading("#1",text="Public Key")

    receiverList.insert(parent='',index='end',iid=0, text="Yourself", values=(''.join(map(str, encryption.getKey()))))
    receiverList.grid(column=0,row=0,sticky="NEWS")
    return receiverList


def addReceiverInfo(window):

    receiverInfo = LabelFrame(
        window,
        fg="cyan",
        bg="black",
        text="Add New Recipient",
        font=("Segol",15,"bold"),
    )

    style = ttk.Style(receiverInfo)
    style.theme_use("default")
    style.configure(
    "Treeview",
    background="black",
    fieldbackground="black",
    foreground="white",
    font=("Segol",10),
    rowheight=30,
    )
    style.configure(
    "Treeview.Heading",
    background="black",
    fieldbackground="black",
    foreground="cyan",
    relief = "solid",
    borderwidth=0,
    font=("Segol",13),
    rowheight=30,
    )

    receiverInfo.grid(column=2,row=6,rowspan=1,sticky="NEWS")
    receiverInfo.columnconfigure(0,weight=10)
    receiverInfo.columnconfigure(1,weight=10)
    receiverInfo.columnconfigure(2,weight=1)

    receiverInfo.rowconfigure(0,weight=1)
    receiverInfo.rowconfigure(1,weight=1)
    receiverInfo.rowconfigure(2,weight=1)

    return receiverInfo

def addNameLabel(frame):
    name1 = Label(
        frame,
        text="Name: ",
        fg="white",
        bg="black",
        font=("Segol",10),
    )
    name1.grid(column=0,row=0,sticky="NEW")
    return name1

def addNameTextBox(frame):
    text1 = Text(
        frame,
        bg="black",
        fg="white",
        border=3,
        insertbackground="white",
        font=("Segol",10),
        height=1,
        width=10
    )
    text1.grid(column=1,row=0,sticky="NEW")
    return text1

def addKeyLabel(frame):
    name2 = Label(
        frame,
        text="Public Key: ",
        fg="white",
        bg="black",
        font=("Segol",10),
    )
    name2.grid(column=0,row=1,sticky="NEW")
    return name2

def addKeyTextbox(frame):
    text2 = Text(
        frame,
        bg="black",
        fg="white",
        border=3,
        insertbackground="white",
        font=("Segol",10),
        height=1,
        width=10
    )
    text2.grid(column=1,row=1,sticky="NEW")
    return text2

def addInsertRecipientFrame(frame):
    buttonFrame = Frame(
        frame,
        bg="black"
    )
    buttonFrame.grid(column=0,row=2,columnspan=2,sticky="NEWS")
    buttonFrame.columnconfigure(0,weight=1)
    buttonFrame.columnconfigure(1,weight=10)
    buttonFrame.columnconfigure(2,weight=3)
    buttonFrame.columnconfigure(3,weight=10)
    buttonFrame.columnconfigure(4,weight=1)

    buttonFrame.rowconfigure(0,weight=10)
    buttonFrame.rowconfigure(1,weight=3)
    return buttonFrame

def addInsertRecipientButton(frame,receiverList,text1,text2):
    button1 = Button(
        frame,
        font=("Segol",10),
        text="Add",
        bg="black",
        fg="white",
        command= lambda: encryption.addToList(receiverList,text1,text2)
    )
    button1.grid(column=1,row=0,sticky="NEWS")
    return button1

def addDeleteRecipientButton(frame,receiverList):
    button2 = Button(
        frame,
        font=("Segol",10),
        text="Delete",
        bg="black",
        fg="white",
        command= lambda: encryption.delete(receiverList)
    )
    button2.grid(column=3,row=0,sticky="NEWS")
    return button2

def addReloadButton(frame,pubKeyLabel,receiverList):
    reloadButton = Button(
        frame,
        text="Generate New Key",
        width=20,
        pady=5,
        bg="black",
        fg="white",
        activebackground="black",
        activeforeground="black",
        relief="groove",
        font=("Arial",10),
        command= lambda: encryption.reload(pubKeyLabel,receiverList)
    )
    reloadButton.grid(column=0,row=1,sticky="N")
    return reloadButton

def addLoadButton(frame,receiverList,pubKeyLabel):
    loadButton = Button(
        frame,
        text="Load",
        width=20,
        pady=5,
        bg="black",
        fg="white",
        activebackground="black",
        activeforeground="black",
        relief="groove",
        font=("Arial",10),
        command = lambda: encryption.loadFile(filedialog,receiverList,pubKeyLabel)
    )
    loadButton.grid(column=1,row=1,sticky="N")
    return loadButton

def addSaveButton(frame,receiverList):
    saveButton = Button(
        frame,
        text="Save",
        width=20,
        pady=5,
        bg="black",
        fg="white",
        activebackground="black",
        activeforeground="white",
        relief="groove",
        font=("Arial",10),
        command= lambda: encryption.saveFile(receiverList,filedialog)
    )
    saveButton.grid(column=2,row=1,sticky="N")

def addExecutionButton(window,x,receiverList,inputText,outputText):
    startOperation = Button(
        window,
        text="Start Encryption / Decryption",
        fg="white",
        background="black",
        border=3,
        font=("Segol",15),
        activebackground="#555555",
        activeforeground="white",
        command = lambda: encryption.startEncryption(x,receiverList,inputText,outputText)
    )
    startOperation.grid(column=0,row=8,sticky="NEWS",columnspan=3)

def init():
    window = Tk()
    window.geometry("900x700")
    window.title("IMAE")

    window.config(
        bg="black",
        padx=10,
        pady=10
    )
    window.rowconfigure(0,weight=7)
    window.rowconfigure(1,weight=1)
    window.rowconfigure(2,weight=7)
    window.rowconfigure(3,weight=1)
    window.rowconfigure(4,weight=1)
    window.rowconfigure(5,weight=1)
    window.rowconfigure(6,weight=10)
    window.rowconfigure(7,weight=1)
    window.rowconfigure(8,weight=1)

    window.columnconfigure(0,weight=10)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=8)
    return window


def terminate(window):
    window.mainloop()