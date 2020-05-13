# Decoder for MIPS32 Basic Verilog Implementation
# Basically, translates MIPS32 assembly code to its binary representation format.
# Uses library tkinter as GUI library.

# Main Icon made by Nhor Phai (https://www.flaticon.com/authors/nhor-phai)
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

class FileDecoder:
    def __init__(self):
        self.createScreen()

        self.startGUI()
        pass

    def createScreen(self):
        self.mainScreen = Tk()
        self.mainScreen.title('MIPS32 Assembly Decoder')
        self.mainScreen.iconbitmap(r'src/icon.ico')
        self.mainScreen.geometry('800x600')

        # Create menu toolbar
        menubar = Menu(self.mainScreen)
        self.mainScreen.config(menu=menubar)
        
        # Entry 1: File manager
        fileMButton = Menu(menubar, tearoff=0) # Tearoff removes dashed lines
        menubar.add_cascade(label='File',menu=fileMButton)
        fileMButton.add_command(label="Open file",command=lambda: self.openFile())
        fileMButton.add_command(label="Save as...",command=lambda: print('save'))
        fileMButton.add_command(label="Exit",command=lambda: quit())

        # Entry 2: Help
        helpMButton = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help',menu=helpMButton)
        helpMButton.add_command(label="About",command=lambda: tkinter.messagebox.showinfo('About','MIPS32 Decoder, 2020'))

        text = Label(self.mainScreen, text = 'Lets go!')
        text.pack()

        loadFile = Button(self.mainScreen,text='Load assembly file',command=lambda: self.openFile())
        loadFile.pack()

        saveFile = Button(self.mainScreen,text='Save memory file',command=lambda: print('save'))
        saveFile.pack()

        self.filePreview = Label(self.mainScreen, bg="white", width=64,height=30)
        self.filePreview.pack()

        pass

    def openFile(self):
        # Open file browser
        assemblyFile = filedialog.askopenfilename()
        assemblyCode = open(assemblyFile, "r")
        print(assemblyFile)
        print(assemblyCode.readlines())
        self.filePreview.insert('hola')
        assemblyCode.close()
        pass

    def startGUI(self):
        self.mainScreen.mainloop()
        pass
# Start main app
app = FileDecoder()