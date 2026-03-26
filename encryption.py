
import numpy as np
from tkinter import END
from tkinter import Text
from tkinter import ttk
from tkinter import Label
import random

#Attribute for generating a key

#generateKeys() - A function that generate a 3x3 matrix with determinant of 1 (to ensure all value are integers) and map it into a 1D array
def generateKeys(): 
  A = np.random.randint(-100, 100, (3, 3))

  while(np.linalg.det(A) != 1 or np.linalg.det(A)!=-1):
      A = np.random.randint(-10, 10, (3, 3))
      if np.linalg.det(A) == 1 or np.linalg.det(A)==-1: 
          break

  keyArr = [0,0,0,0,0,0,0,0,0]

  for i in range(9):
      keyArr[i] = int(A[int(i/3)][int(i%3)])+30

  text = "Your public key is "
  key = ""
  for i in keyArr:
     text += str(i)
     key += str(i)
  return (key, text)
  
keyText = generateKeys()
key = keyText[0]
text = keyText[1]


#Helper functions for interface.py to access the necessary information
def getText():
   return text

def getKey():
   return key


#When reload button is pressed in interface.py, another set of keys are generated
def reload(pubKeyTitle,receiverList):
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

def startEncryption(x,receiverList,inputText,outputText):
  print(receiverList.item(receiverList.focus()).get("values"))
  x = x.get()
  print(x)
  if(x==0):
    key = receiverList.item(receiverList.focus()).get("values")[0]
    code = str(inputText.get("1.0",END))
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(9):
      temp[(8-i)//3][(8-i)%3] = key%100-30
      key = key // 100
    
    outputText.delete("1.0",END)
    print(temp)
    outputText.insert(
       "1.0",encrypt(code,temp)
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



def loadFile(filedialog,receiverList,pubKeyLabel):


   filePath = filedialog.askopenfilename()
   file = open(filePath,"r")
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
   pubKeyLabel.config(
      text= text
   )
   for i in range(3,len(arr),2):
    receiverList.insert(parent='',index="end",text=arr[i],values=arr[i+1])

   file.close()

def saveFile(receiverList,filedialog):

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
   




def addToList(receiverList,text1,text2):
    print(text2.get("1.0",END))
    if(len(text2.get("1.0",END))!=19):
        print("Invalid Input")
    else:
        receiverList.insert(parent='',index='end',text=text1.get("1.0",END),values=(text2.get("1.0",END)))

def delete(receiverList):
    receiverList = receiverList
    try:
      if(receiverList.selection()[0]=="0"):
          print("Cannot Delete")
          
      else:
          try:
              print(receiverList.item(receiverList.focus()).get('text'))
          except IndexError:
              print("Error")
          receiverList.delete(receiverList.selection()[0])
    except:
       print("Nothing Here")
        

