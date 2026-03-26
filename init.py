# import encryption
import interface
import encryption
from tkinter import Frame


if __name__ == "__main__":

    #Initialize window
    window = interface.init()

    #Title and information for keys
    title = interface.addTitle(window)
    pubKeyLabel = interface.addPubKeyLabel(window)

    
    #Input section
    inputFrame = interface.addInputFrame(window)
    inputTextbox = interface.addInputTextbox(inputFrame)
    
    #Encryption Selection Radio Boxes
    encryptSelectionFrame = interface.addEncryprionSelectionFrame(window)
    encryptionRadioBox,x = interface.addModeRadioButtons(encryptSelectionFrame)

    #Output textbox
    outputFrame = interface.addOutputFrame(window)
    outputTextbox = interface.addOutputTextBox(outputFrame)

    #Receiver
    receiverFrame = interface.addReceiverFrame(window)
    receiverList = interface.addReceiverList(receiverFrame)
    receiverInvite = interface.addReceiverInfo(window)

    #File Buttons
    reloadButton = interface.addReloadButton(title,pubKeyLabel,receiverList)
    loadButton = interface.addLoadButton(title,receiverList,pubKeyLabel)
    saveButton = interface.addSaveButton(title,receiverList)

    #Insert new receiver information
    nameTextBoxLabel = interface.addNameLabel(receiverInvite)
    nameTextBox = interface.addNameTextBox(receiverInvite)
    keyTextBoxLabel = interface.addKeyLabel(receiverInvite)
    keyTextBox = interface.addKeyTextbox(receiverInvite)

    #Recipient Buttons
    addRecipientLabel = interface.addInsertRecipientFrame(receiverInvite)
    addRecipientButton = interface.addInsertRecipientButton(addRecipientLabel,receiverList,nameTextBox,keyTextBox)
    resetButton = interface.addDeleteRecipientButton(addRecipientLabel,receiverList)

    #Execution Button
    executionButton = interface.addExecutionButton(window,x,receiverList,inputTextbox,outputTextbox)
    


    interface.terminate(window)

    