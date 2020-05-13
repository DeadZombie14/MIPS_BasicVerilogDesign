# Decoder for MIPS32 Basic Verilog Implementation
# Made by DeadZombie14 (Mendoza Morelos Martin Mathier)
# Basically, translates MIPS32 assembly code to its binary representation format.
# Uses library tkinter as GUI library.

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class FileDecoder:
    def __init__(self):
        self.createScreen()

        self.startGUI()
        pass

    def createScreen(self):
        self.mainScreen = Tk()
        self.mainScreen.title('MIPS32 Assembly Decoder')
        #self.mainScreen.iconbitmap(r'src/icon.ico')
        self.width = 800
        self.height = 600
        self.mainScreen.geometry(str(self.width)+"x"+str(self.height))

        # Create menu toolbar
        menubar = Menu(self.mainScreen)
        self.mainScreen.config(menu=menubar,bg="gray")
        
        # Entry 1: File manager
        fileMButton = Menu(menubar, tearoff=0) # Tearoff removes dashed lines
        menubar.add_cascade(label='File',menu=fileMButton)
        fileMButton.add_command(label="Open file",command=lambda: self.openFile())
        fileMButton.add_command(label="Save as...",command=lambda: print('save'))
        fileMButton.add_command(label="Exit",command=lambda: quit())

        # Entry 2: Help
        helpMButton = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help',menu=helpMButton)
        helpMButton.add_command(label="About",command=lambda: messagebox.showinfo('About','MIPS32 Decoder, 2020'))

        editors = Frame(self.mainScreen)
        editors.pack()
        
        # Assembly editor
        leftEditor = Frame(editors)
        leftEditor.pack(side=LEFT,fill=BOTH,padx=5, pady=5, expand=True)

        codeEditorLabel = Label(leftEditor,text="Assembly code editor")
        codeEditorLabel.pack(side=TOP)

        codeDirectory = Frame(leftEditor)
        codeDirectory.pack(fill=X)
        self.codeDirectoryVar = StringVar()
        inputCD = Entry(codeDirectory,width=52,textvariable=self.codeDirectoryVar,bg="white",fg="black")
        inputCD.pack(side=LEFT)
        buttonCD = Button(codeDirectory,text='...',command=lambda: self.openCodeFile())
        buttonCD.pack(side=RIGHT)

        scrollbarCPx = Scrollbar(leftEditor, orient=HORIZONTAL)
        scrollbarCPx.pack(side=BOTTOM,fill=X)
        scrollbarCPy = Scrollbar(leftEditor, orient=VERTICAL)
        scrollbarCPy.pack(side=RIGHT,fill=Y)
        self.codePreview = Text(leftEditor,bg="white",width=40,fg="black",xscrollcommand=scrollbarCPx.set,yscrollcommand=scrollbarCPy.set,wrap=NONE) 
        self.codePreview.pack(fill=Y)
        scrollbarCPx.config(command=self.codePreview.xview)
        scrollbarCPy.config(command=self.codePreview.yview)

        # Switching arrows
        switchingArrows = Frame(editors)
        switchingArrows.pack(side=LEFT)
        toBinaryButton = Button(switchingArrows,text="=>")
        toBinaryButton.pack(side=TOP)
        toAssemblyButton = Button(switchingArrows,text="<=")
        toAssemblyButton.pack(side=TOP)


        # Binary editor
        rightEditor = Frame(editors)
        rightEditor.pack(side=RIGHT,fill=BOTH,padx=5, pady=5, expand=True)

        binaryEditorLabel = Label(rightEditor,text="Binary editor")
        binaryEditorLabel.pack(side=TOP)

        binaryDirectory = Frame(rightEditor)
        binaryDirectory.pack(fill=X)
        self.binaryDirectoryVar = StringVar()
        inputBD = Entry(binaryDirectory,textvariable=self.binaryDirectoryVar,width=52,bg="white",fg="black")
        inputBD.pack(side=LEFT)
        buttonBD = Button(binaryDirectory,text='...',command=lambda: self.openBinaryFile())
        buttonBD.pack(side=RIGHT)

        scrollbarBPx = Scrollbar(rightEditor, orient=HORIZONTAL)
        scrollbarBPx.pack(side=BOTTOM,fill=X)
        scrollbarBPy = Scrollbar(rightEditor, orient=VERTICAL)
        scrollbarBPy.pack(side=RIGHT,fill=Y)
        self.binaryPreview = Text(rightEditor,bg="white",width=40,fg="black",xscrollcommand=scrollbarBPx.set,yscrollcommand=scrollbarBPy.set,wrap=NONE)
        self.binaryPreview.pack(fill=Y)
        scrollbarBPx.config(command=self.binaryPreview.xview)
        scrollbarBPy.config(command=self.binaryPreview.yview)


        statusBar = Label(self.mainScreen, text = 'Please load a MIPS assembly file.',relief=RAISED,anchor=W)
        statusBar.pack(side=BOTTOM,fill=X)

        pass

    def openCodeFile(self):
        # Open file browser
        assemblyFile = filedialog.askopenfilename()
        assemblyCode = open(assemblyFile, "r")
        print(assemblyFile)
        self.codeDirectoryVar.set(str(assemblyFile))
        self.codePreview.delete(1.0,END)
        self.codePreview.insert(1.0,assemblyCode.read())
        assemblyCode.close()
        pass
    
    def openBinaryFile(self):
        # Open file browser
        assemblyFile = filedialog.askopenfilename()
        assemblyCode = open(assemblyFile, "r")
        print(assemblyFile)
        self.binaryDirectoryVar.set(str(assemblyFile))
        self.binaryPreview.delete(1.0,END)
        self.binaryPreview.insert(1.0,assemblyCode.read())
        assemblyCode.close()
        pass

    def startGUI(self):
        self.mainScreen.mainloop()
        pass
# Start main app
app = FileDecoder()