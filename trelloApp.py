import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import *
import tkinter.font as tkFont
import time
import os

from lib import getTrelloData as getApi

root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Trello Application')
save = False
importFlag = False
fileName = ''
isExport = False

def success_popup():
   top= Toplevel(root)
   Label(top, text= "Finish successfully !" + os.linesep + "Get data finish, please check !", font=('Arial 10')).place(x=10,y=80)

def import_success():
   top= Toplevel(root)
   Label(top, text= "Finish successfully !" + os.linesep + "Import data finish, please check !", font=('Arial 10')).place(x=10,y=80)

def error1_popup():
   top= Toplevel(root)
   Label(top, text= "Error!" + os.linesep + "Please check your token!!", font=('Arial 10')).place(x=10,y=80)

def error2_popup():
   top= Toplevel(root)
   Label(top, text= "Error!" + os.linesep + "Unexpected error occur!!", font=('Arial 10')).place(x=10,y=80)

def setText(textContent):
    processLine.configure(state="normal")
    processLine.insert("end", textContent)
    processLine.insert("end", os.linesep)
    processLine.configure(state="disable")
    root.update()

def setButtonState(state):
    btnExport["state"] = state
    btnToken["state"] = state
    btnImport["state"] = state

def UploadAction(event=None):
    global importFlag
    if importFlag == False:
        global fileName
        fileName = filedialog.askopenfilename()
        if fileName == '':
            return 0
        importFlag = True
        setText('Please input your board_id (if needed)')
        entry.delete(0, 'end')
        entry.place(x=30,y=260,width=533,height=30)
        btnCancel.place(x=30,y=320,width=129,height=39)
        btnImport['text'] = 'START IMPORT'
    else:
        idBoard = entry.get()
        setButtonState("disabled")
        root.update()
        setText("Start import data...")
        entry.place_forget()
        btnCancel.place_forget()
        root.update()
        board_id = getApi.uploadData(fileName,idBoard)
        if board_id == "err":
            error2_popup()
            setText("Import data error!")
        else:
            setText("Import finish. Check product imported at:")
            setText("https://trello.com/b/" + board_id)
            import_success()
        setButtonState("normal")
        btnImport['text'] = 'IMPORT DATA'
        importFlag = False

def runGetData():
    global isExport
    if isExport == False:
        isExport = True
        text = StringVar()
        l = Label(root, textvariable=text, fg='blue', font=(".VnMonotype corsiva", 15))
        l.place(x=30,y=260,width=533,height=30)
        text.set('Exportinggg.....Please wait!!!')
        setButtonState("disabled")
        root.update()
        time.sleep(2)
        l.place_forget()
        setButtonState("normal")
        result = getApi.getData()
        if (result == 0):
            success_popup()
            setText("Export data success!")
        elif (result == 1):
            error1_popup()
            setText("Error! Please check your token!")
        else:
            error2_popup()
            setText("Error! Unexpected error occur!")
        isExport = False
def getData():
    setText('Start change export data... Please wait!')
    runGetData()

def execute():
    global save
    if (save == False):
        save = True
        setText('Start change Token')
        setText('Please input your api key and token')
        entry.delete(0, 'end')
        entry.place(x=30,y=260,width=533,height=30)
        btnCancel.place(x=30,y=320,width=129,height=39)
        btnToken['text'] = 'SAVE TOKEN'
    else:
        with open("lib"+os.path.sep+"data.txt", "w") as f2:
            f2.write(entry.get())
        f2.close()
        entry.place_forget()
        btnCancel.place_forget()
        btnToken['text'] = 'CHANGE TOKEN'
        save = False
        setText('Save token successfully!!')

def cancel():
    global importFlag, save
    if save == True:
        btnCancel.place_forget()
        entry.delete(0, 'end')
        entry.place_forget()
        btnToken['text'] = 'CHANGE TOKEN'
        save = False
        setText('Cancel change successfully!!')
        return 0
    elif importFlag == True:
        btnCancel.place_forget()
        entry.delete(0, 'end')
        entry.place_forget()
        btnImport['text'] = 'IMPORT DATA'
        importFlag = False
        setText('Cancel import successfully!!')
        return 0
# label with a specific font
label = ttk.Label(
    root,
    text='TRELLO APPLICATION',
    font=("Tahoma", 13))

label.pack(ipadx=10, ipady=10)

btnImport = ttk.Button (
    root,
    text = "IMPORT DATA",
    width= 30,
    command=UploadAction
)
btnImport.place(x=30,y=60,width=135,height=42)
#btnImport.pack(ipadx=10, ipady=10, padx = 10)
#btnImport["state"] = "disabled"

btnExport = ttk.Button (
    root,
    text = "EXPORT DATA",
    width= 30,
    command=lambda:[getData()]
)
btnExport.place(x=30,y=130,width=135,height=42)
#btnExport.pack(ipadx=10, ipady=10, padx = 10, pady=10)

btnToken = ttk.Button (
    root,
    text = "CHANGE TOKEN",
    width= 30,
    command=lambda:[execute()]
)
btnToken.place(x=30,y=200,width=134,height=42)
#btnToken.pack(ipadx=10, ipady=10, padx = 10, pady=10)

btnCancel = ttk.Button (
    root,
    text = "CANCEL",
    width= 30,
    command=lambda:[cancel()]
)

processLine=tk.Text(root)
processLine["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
processLine["font"] = ft
processLine["fg"] = "#0000ff"
processLine.place(x=220,y=60,width=341,height=185)
processLine.configure(state="disable")

entry = ttk.Entry (
    root,
    width= 450
)

def main():
    root.mainloop()

if __name__ == "__main__":
    main()
