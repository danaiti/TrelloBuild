import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import *
import time

import getTrelloData as getApi


root = tk.Tk()
root.geometry('500x350')
root.resizable(False, False)
root.title('Trello Application')
save = False
isExport = False

def success_popup():
   top= Toplevel(root)
   Label(top, text= "Finish successfully ! \n Get data finish, please check !", font=('Arial 10')).place(x=10,y=80)

def error1_popup():
   top= Toplevel(root)
   Label(top, text= "Error! \n Please check your token!!", font=('Arial 10')).place(x=10,y=80)

def error2_popup():
   top= Toplevel(root)
   Label(top, text= "Error! \n Unexpected error occur!!", font=('Arial 10')).place(x=10,y=80)

def UploadAction(event=None):
    fileName = filedialog.askopenfilename()

    with open(fileName, "r") as f1:
        print (f1.read())
    f1.close()

    getApi.create_list("GTtrIMUe","Kaki")

def runGetData():
    global isExport
    if isExport == False:
        isExport = True
        text = StringVar()
        l = Label(root, textvariable=text, fg='blue', font=(".VnMonotype corsiva", 15))
        l.pack(ipadx=10, ipady=10, padx = 10)
        text.set('Exportinggg.....Please wait!!!')
        btnExport["state"] = "disabled"
        btnToken["state"] = "disabled"
        root.update()
        time.sleep(2)
        l.destroy()
        btnExport["state"] = "normal"
        btnToken["state"] = "normal"
        result = getApi.getData()
        if (result == 0):
            success_popup()
        elif (result == 1):
            error1_popup()
        else:
            error2_popup()
        isExport = False
def getData():
    runGetData()

def execute():
    global save
    if (save == False):
        save = True
        entry.pack(ipadx=10, ipady=10, padx = 10)
        btnToken['text'] = 'SAVE TOKEN'
    else:
        with open("data.txt", "w") as f2:
            f2.write(entry.get())
        f2.close()
        entry.pack_forget()
        btnToken['text'] = 'CHANGE TOKEN'
        save = False

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
btnImport.pack(ipadx=10, ipady=10, padx = 10)
btnImport["state"] = "disabled"

btnExport = ttk.Button (
    root,
    text = "EXPORT DATA",
    width= 30,
    command=lambda:[getData()]
)
btnExport.pack(ipadx=10, ipady=10, padx = 10, pady=10)

btnToken = ttk.Button (
    root,
    text = "CHANGE TOKEN",
    width= 30,
    command=lambda:[execute()]
)
btnToken.pack(ipadx=10, ipady=10, padx = 10, pady=10)

entry = ttk.Entry (
    root,
    width= 450
)

def main():
    root.mainloop()

if __name__ == "__main__":
    main()