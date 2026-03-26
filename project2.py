from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np

N = 1000000  # Number of random matrices sampled
count = 0

A = np.random.randint(-100, 100, (3, 3))

while(np.linalg.det(A) != 1 or np.linalg.det(A)!=-1):
    A = np.random.randint(-20, 20, (3, 3))
    if np.linalg.det(A) == 1 or np.linalg.det(A)==-1: 
        break

keyArr = [0,0,0,0,0,0,0,0,0]
for i in range(9):
    keyArr[i] = int(A[int(i/3)][int(i%3)])+30
   

text = "Your public key is "+''.join(map(str,keyArr))

import random


def reload():
  A = np.random.randint(-100, 100, (3, 3))

  while(np.linalg.det(A) != 1 or np.linalg.det(A)!=-1):
    A = np.random.randint(-20, 20, (3, 3))
    if np.linalg.det(A) == 1 or np.linalg.det(A)==-1: 
        break

  keyArr = [0,0,0,0,0,0,0,0,0]
  for i in range(9):
      keyArr[i] = int(A[int(i/3)][int(i%3)])+30
  text = "Your public key is "+''.join(map(str,keyArr))
  pubKeyTitle.config(
      text= text
  )
  li = [''.join(map(str,keyArr))]
  for i in receiverList.get_children():
     if(receiverList.item(i).get("text")=="Yourself"):
        receiverList.item(i,text="Yourself",values=li)
    

def PaddingArray(array):
  if len(array) % 9 != 0:
    for i in range(9-len(array) % 9):
      array.append(round(random.random()*10)+1)
  return array

def TransformingArray(array):
  row=[]
  newarray=[]
  for i in range(len(array)):
    row.append(array[i])
    if (i+1)%3==0:
      newarray.append(row)
      row = []
  array = newarray
  return array

def CrudeEncryption(array,key):
  newarray = []
  row = []
  for k in range(int(len(array)/3)):
    for i in range(3):
      for j in range(3):
        row.append(array[i+3*k][0]*key[0][j]+array[i+k*3][1]*key[1][j]+array[i+k*3][2]*key[2][j])
      newarray.append(row)
      row = []
  array = newarray
  return array

def Numbershift(array):
  for j in range(int(len(array))):
    for k in range(3):
      array[j][k] = array[j][k] + (30000)
  return array

def CipherText(array):
  Text = []
  for i in range(int(len(array))):
    for j in range(3):
      Text.append(chr(int(array[i][j])))
  Text = "".join(Text)
  return Text

def ReturnCrude(array):
  for i in range(len(array)):
    array[i] = array[i]-30000
  return array

def ReturnArray(array):
  Text = []
  for i in range(int(len(array))):
    for j in range(3):
      Text.append(array[i][j])
  return Text

def DeletePadding(array):
  flag = 0
  newarray = []
  for i in range(len(array)):
    if array[i]==0:
      flag = i
      break
  for j in range(flag-1):
    newarray.append(array[j])
  array = newarray
  return array

def DecipherText(array):
  Text = []
  print(int(len(array)))
  for i in range(int(len(array))):
    Text.append(chr(int(array[i])))
  Text = "".join(Text)
  return Text

#Here you can add more keys for more users
PrivateKey1 = [[0,0,1],[-1,-1,0],[0,1,0]]
PublicKey1 = [[0,-1,-1],[0,0,1],[1,0,0]]

PrivateKey2 = [[1,2,-3],[0,1,2],[0,0,1]]
PublicKey2 = [[1,-2,7],[0,1,-2],[0,0,1]]

PrivateKey3 = [[3,-3,4],[2,-3,4],[0,-1,1]]
PublicKey3 = [[1,-1,0],[-2,3,-4],[-2,3,-3]]

PrivateKey4 = [[1,0,1],[-4,1,-1],[6,-2,1]]
PublicKey4 = [[-1,-2,-1],[-2,-5,-3],[2,2,1]]
#Here you can choose the pair of key for encryption and decryption.
EncryptionKey = PublicKey2
DecryptionKey = PrivateKey2

def encrypt(a,key):
  UnencryptedUNICODE = []
  EncryptedUNICODE = []
  for i in range(len(a)):
    UnencryptedUNICODE.append(ord(a[i]))
  Length = len(UnencryptedUNICODE)
  UnencryptedUNICODE.append(Length)
  UnencryptedUNICODE.append(0)

  UnencryptedUNICODE = PaddingArray(UnencryptedUNICODE)
  UnencryptedUNICODE = TransformingArray(UnencryptedUNICODE)
  EncryptedUNICODE = CrudeEncryption(UnencryptedUNICODE,key)
  EncryptedUNICODE = Numbershift(EncryptedUNICODE)


  return CipherText(EncryptedUNICODE)


def decrypt(a,key):
  EncryptedUNICODE = []
  for i in range(len(a)):
    EncryptedUNICODE.append(ord(a[i]))
  EncryptedUNICODE = ReturnCrude(EncryptedUNICODE)
  EncryptedUNICODE = TransformingArray(EncryptedUNICODE)
  DecryptedUNICODE = CrudeEncryption(EncryptedUNICODE,key)
  DecryptedUNICODE = ReturnArray(DecryptedUNICODE)
  DecryptedUNICODE = DeletePadding(DecryptedUNICODE)
  DecryptedUNICODE = DecipherText(DecryptedUNICODE)

  print(DecryptedUNICODE)
  return DecryptedUNICODE

def startEncryption():
  if(x.get()==0):
    key = receiverList.item(receiverList.focus()).get("values")[0]
    code = str(inputText.get("1.0",END))
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(9):
      temp[(8-i)//3][(8-i)%3] = key%100-30
      key = key // 100
    outputText.delete("1.0",END)
    outputText.insert(
       "1.0",
       encrypt(code,temp)
    )
  else:
    key = int(receiverList.item(0).get("values")[0])
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(9):
      temp[(8-i)//3][(8-i)%3] = key%100-30
      key = key // 100
    temp = np.linalg.inv(temp)
    for i in range(9):
       temp[(8-i)//3][(8-i)%3] = round(temp[(8-i)//3][(8-i)%3])
    code = str(inputText.get("1.0",END))
    outputText.delete("1.0",END)
    outputText.insert(
       "1.0",
       decrypt(code,temp)
    )



def loadFile():
   filePath = filedialog.askopenfilename()
   file = open(filePath,"r")
   print(receiverList.get_children())
   text = str(file.read())
   arr = text.split()
   

   receiverList.delete(*receiverList.get_children())
   receiverList.insert(
      index=0,
      parent="",
      text="Yourself",
      values= [int(arr[0])],
      iid=0
   )

   text = "Your public key is "+ arr[0]
   pubKeyTitle.config(
      text= text
   )
   for i in range(3,len(arr),2):
    receiverList.insert(parent='',index="end",text=arr[i],values=arr[i+1])

   file.close()

def saveFile():
   print(receiverList.get_children())
   file = filedialog.asksaveasfile(defaultextension='.txt',
                                   filetypes=[
                                      ('Plain Text File','.txt')                  
                                   ])
   filetext = str(receiverList.item(0).get("values")[0])
   for i in receiverList.get_children():
      filetext = filetext + " " + str(receiverList.item(i).get("text"))
      filetext = filetext + " " + str(receiverList.item(i).get("values")[0])
      
   file.write(filetext)

   file.close()
   

window = Tk()
window.geometry("900x700")
window.title("IMAE")

window.config(
    bg="black",
    padx=10,
    pady=10
)

title = LabelFrame(
    window,
    text="IMAE Interface",
    font=('Segoul',15,'bold'),
    fg="cyan",
    bg="black",
    pady=10
)

pubKeyTitle = Label(
    title,
    text=text,
    height=1,
    bg="black",
    fg="white",
    font=('Segol',13),
    pady=10,
    

)

image = PhotoImage()

reloadButton = Button(
    title,
    text="Generate New Key",
    width=20,
    pady=5,
    bg="black",
    fg="white",
    activebackground="black",
    activeforeground="black",
    relief="groove",
    font=("Arial",10),
    command= reload

)

loadButton = Button(
    title,
    text="Load",
    width=20,
    pady=5,
    bg="black",
    fg="white",
    activebackground="black",
    activeforeground="black",
    relief="groove",
    font=("Arial",10),
    command = loadFile
)

saveButton = Button(
     title,
    text="Save",
    width=20,
    pady=5,
    bg="black",
    fg="white",
    activebackground="black",
    activeforeground="white",
    relief="groove",
    font=("Arial",10),
    command=saveFile
)

input = LabelFrame(
    window,
    fg="cyan",
    text="Your Message: ",
    font=('Segoul',15,'bold'),
    bg="black",
)

inputText = Text(
    input,
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

encryptSelection = Frame(
    window,
    bg="black",
)

selection = ["Encryption (Please Select a Recipient)","Decryption"]
x=IntVar()
for i in range(len(selection)):
    encryptButton = Radiobutton(
        encryptSelection,
        text=selection[i],
        variable=x,
        value=i,
        bg="black",
        fg="cyan",
        selectcolor="black",
        font=("Segol",10)
    )
    encryptButton.grid(column=i,row=0,sticky="NEWS")



output = LabelFrame(
    window,
    text="Ciphered Text",
    font=("Segol",15,"bold"),
    bg="black",
    fg="cyan"
)

outputText = Text(
    output,
    font=("Segol",13),
    bg="black",
    fg="white",
    border=0,
    width=1,
    height=1,
    padx=10,
    pady=10,
)

startOperation = Button(
    window,
    text="Start Encryption / Decryption",
    fg="white",
    background="black",
    border=3,
    font=("Segol",15),
    activebackground="#555555",
    activeforeground="white",
    command = startEncryption

)


def addToList():
    if(len(text2.get("1.0",END))!=19):
        print("Invalid Input")
    else:
        receiverList.insert(parent='',index='end',text=text1.get("1.0",END),values=(text2.get("1.0",END)))

def delete():
    if(receiverList.selection()[0]=="0"):
        print("Cannot Delete")
        
    else:
        try:
            print(receiverList.item(receiverList.focus()).get('text'))
        except IndexError:
            print("Error")
        receiverList.delete(receiverList.selection()[0])
        


receiver = LabelFrame(
    window,
    fg="cyan",
    bg="black",
    text="Recipient",
    font=("Segol",15,"bold"),
)


receiverList = ttk.Treeview(
    receiver,

)

receiverList['columns'] = ("#1")
receiverList.column("#0",width=1,anchor="center")
receiverList.column("#1",width=1,anchor="center")

receiverList.heading("#0",text="Name")
receiverList.heading("#1",text="Public Key")

receiverList.insert(parent='',index='end',iid=0, text="Yourself", values=(''.join(map(str,keyArr))))




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


name1 = Label(
    receiverInfo,
    text="Name: ",
    fg="white",
    bg="black",
    font=("Segol",10),
)

text1 = Text(
    receiverInfo,
    bg="black",
    fg="white",
    border=3,
    insertbackground="white",
    font=("Segol",10),
    height=1,
    width=10
)

name2 = Label(
    receiverInfo,
    text="Public Key: ",
    fg="white",
    bg="black",
    font=("Segol",10),
)

text2 = Text(
    receiverInfo,
    bg="black",
    fg="white",
    border=3,
    insertbackground="white",
    font=("Segol",10),
    height=1,
    width=10
)

buttonFrame = Frame(
    receiverInfo,
    bg="black"
)

button1 = Button(
    buttonFrame,
    font=("Segol",10),
    text="Add",
    bg="black",
    fg="white",
    command=addToList
)

button2 = Button(
    buttonFrame,
    font=("Segol",10),
    text="Delete",
    bg="black",
    fg="white",
    command=delete
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

title.grid(column=0,row=0,columnspan=3,sticky="NESW")

title.columnconfigure(0,weight=1)
title.columnconfigure(1,weight=1)
title.columnconfigure(2,weight=1)

title.rowconfigure(0,weight=1)
title.rowconfigure(1,weight=1)

pubKeyTitle.grid(column=0,row=0,columnspan=3)

reloadButton.grid(column=0,row=1,sticky="N")
loadButton.grid(column=1,row=1,sticky="N")
saveButton.grid(column=2,row=1,sticky="N")

input.grid(column=0,row=2,sticky="NESW")

input.columnconfigure(0,weight=1)
input.rowconfigure(0,weight=1)

inputText.grid(column=0,row=0,sticky="EWNS")

encryptSelection.grid(column=0,row=4,sticky="NEWS")
encryptSelection.columnconfigure(0,weight=1)
encryptSelection.columnconfigure(1,weight=1)

output.grid(column=0,row=6,sticky="NEWS")
output.columnconfigure(0,weight=1)
output.rowconfigure(0,weight=1)
outputText.grid(column=0,row=0,sticky="NEWS")

startOperation.grid(column=0,row=8,sticky="NEWS",columnspan=3)

receiver.grid(column=2,row=2,rowspan=4,sticky="NEWS")
receiver.columnconfigure(0,weight=1)
receiver.rowconfigure(0,weight=1)

receiverList.grid(column=0,row=0,sticky="NEWS")

receiverInfo.grid(column=2,row=6,rowspan=1,sticky="NEWS")
receiverInfo.columnconfigure(0,weight=10)
receiverInfo.columnconfigure(1,weight=10)
receiverInfo.columnconfigure(2,weight=1)

receiverInfo.rowconfigure(0,weight=1)
receiverInfo.rowconfigure(1,weight=1)
receiverInfo.rowconfigure(2,weight=1)

name1.grid(column=0,row=0,sticky="NEW")
name2.grid(column=0,row=1,sticky="NEW")
text1.grid(column=1,row=0,sticky="NEW")
text2.grid(column=1,row=1,sticky="NEW")

buttonFrame.grid(column=0,row=2,columnspan=2,sticky="NEWS")
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=10)
buttonFrame.columnconfigure(2,weight=3)
buttonFrame.columnconfigure(3,weight=10)
buttonFrame.columnconfigure(4,weight=1)

buttonFrame.rowconfigure(0,weight=10)
buttonFrame.rowconfigure(1,weight=3)
button1.grid(column=1,row=0,sticky="NEWS")
button2.grid(column=3,row=0,sticky="NEWS")
window.mainloop()


