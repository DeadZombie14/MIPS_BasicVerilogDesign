# Decoder for MIPS32 Basic Verilog Implementation
# Made by DeadZombie14 (Mendoza Morelos Martin Mathier)
# Basically, translates MIPS32 assembly code to its binary representation format.
# Uses library tkinter as GUI library.

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Espaciado entre elementos
espaciado = ""
# Dividir cada linea en N caracteres
corteLinea = 8 #37 #8
# Cantidad de lineas minimas
lineasMinimas = 128 #32 #128

lastassemblyFile = "instruccionesEnsamblador.asm"
lastbinaryFile = "instruccionesBinario.bin"

class Decoder:
    def __init__(self):
        pass

    def decode(self, guiInterface):
        guiInterface.clearInstructions()
        self.leerArchivos(guiInterface, guiInterface.getAssemblyFile(), guiInterface.getBinaryFile())
        pass

    def leerArchivos(self, guiInterface, assemblyFile, binaryFile):
        ensamblador = open(assemblyFile, "r")
        codigoMaquina = open(binaryFile,"w+")
        i = 0
        for line in ensamblador:
            print(line.rstrip())
            if line.rstrip() != "":
                if line.rstrip()[0] != "#":
                    #Cortar la primer palabra de instrucción y leerla
                    binarioInstr = self.leerInstruccion(line)
                    guiInterface.insertInstruction(line.rstrip(), binarioInstr[0], binarioInstr[1])
                    print(binarioInstr)
                    # Dividir cada linea en N caracteres
                    for j in range(0, len(binarioInstr[0]), corteLinea):
                        lineaNueva = binarioInstr[0][j:j+corteLinea]
                        codigoMaquina.write(lineaNueva)
                        codigoMaquina.write("\n")
                        i = i + 1
        # Completar la memoria de instrucciones con 0
        for k in range(i,lineasMinimas,1):
            lineaVacia = "0" * corteLinea
            codigoMaquina.write(lineaVacia)
            #Evitar escribir más de las lineas minimas
            if k != lineasMinimas-1:
                codigoMaquina.write("\n")
        ensamblador.close()
        codigoMaquina.close()

    def leerInstruccion(self,linea):
        instruccion = linea.split()[0]
        op = ""
        instCode = ""
        shamt = ""
        if instruccion.upper() == "ADD":
            op = "000000"
            instructionType = "R"
            instCode = "100000"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "SUB":
            op = "000000"
            instructionType = "R"
            instCode = "100010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "MUL":
            op = "000000"
            instructionType = "R"
            instCode = "000010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "DIV":
            op = "000000"
            instructionType = "R"
            instCode = "011010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "AND":
            op = "000000"
            instructionType = "R"
            instCode = "100100"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "OR":
            op = "000000"
            instructionType = "R"
            instCode = "100101"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "NOR":
            op = "000000"
            instructionType = "R"
            instCode = "100111"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "SLL":
            op = "000000"
            instructionType = "R"
            instCode = "000000"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + shamt + espaciado  + parametros + instCode, instructionType)
        elif instruccion.upper() == "SRL":
            op = "000000"
            instructionType = "R"
            instCode = "000011"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + shamt + espaciado  + parametros + instCode, instructionType)
        elif instruccion.upper() == "SLT":
            op = "000000"
            instructionType = "R"
            instCode = "101010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)
        elif instruccion.upper() == "XOR":
            op = "000000"
            instructionType = "R"
            instCode = "100110"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return (op + espaciado + parametros + shamt + espaciado  + instCode, instructionType)

    def leerParametros(self, op, linea):
        parametros = ""
        if op == "000000":
            # Cortar parametros de la instruccion
            for palabra in linea.split():
                if palabra[0] == "$":
                    palabra = palabra[1:] # Cortar el signo $
                    if palabra[-1] == ",":
                        palabra = palabra[:-1] # Cortar el signo ,
                    parametros = parametros + f"{int(palabra):05b}" + espaciado
            return parametros

class GUIDecoder:
    def __init__(self):
        self.instructionsArray = {}
        self.assemblyFile = lastassemblyFile
        self.binaryFile = lastbinaryFile
        
        self.decoder = Decoder()
        self.createScreen()
        
        self.openCodeFile()
        self.openBinaryFile()

        self.startGUI()
        pass

    def decode(self):
        self.decoder.decode(self)
        self.updateLog("Instructions decoded.")
        pass

    def printInstruction(self, event):
        print(event)
        instruction = self.instructions.get(self.instructions.curselection()[0])
        print(instruction)
        print(self.instructionsArray[instruction])

        self.instructionType = self.instructionsArray[instruction]['type']
        # print(self.instructionsArray)
        self.loadInstructionPreview(self.instructionsArray[instruction]['binary'])
        pass

    def insertInstruction(self, instructionCode, instructionBinary, instructionType):
        self.instructionsArray[instructionCode] = {'binary':instructionBinary,'type':instructionType}
        self.instructions.insert(END, instructionCode)
        pass

    def clearInstructions(self):
        self.instructionsArray = {}
        self.instructions.delete(1, END)
        pass

    def loadInstructionPreview(self, instructionBinary=""):
        print("IB: " + instructionBinary)
        for widget in self.instructionPreview.winfo_children():
            widget.destroy()
        
        instructionPreviewLabel = Label(self.instructionPreview, text="Instruction Analysis")
        instructionPreviewLabel.pack(pady=5)
        instructionPreviewBinary = Frame(self.instructionPreview)
        instructionPreviewBinary.pack()
        if(self.instructionType == 'R'):

            op = StringVar()
            op.set(instructionBinary[0:5])
            instPar1 = Frame(instructionPreviewBinary)
            instPar1.pack(side=LEFT)
            instPar1Label = Label(instPar1,text="OP")
            instPar1Label.pack()
            instPar1Input = Entry(instPar1, width=6)
            instPar1Input.pack(padx=2)
            instPar1Input.config(textvariable=op)

            rs = StringVar()
            rs.set(instructionBinary[6:10])
            instPar2 = Frame(instructionPreviewBinary)
            instPar2.pack(side=LEFT)
            instPar2Label = Label(instPar2,text="RS")
            instPar2Label.pack()
            instPar2Input = Entry(instPar2, width=5)
            instPar2Input.pack(padx=2)
            instPar2Input.config(textvariable=rs)

            rt = StringVar()
            rt.set(instructionBinary[11:15])
            instPar3 = Frame(instructionPreviewBinary)
            instPar3.pack(side=LEFT)
            instPar3Label = Label(instPar3,text="RT")
            instPar3Label.pack()
            instPar3Input = Entry(instPar3, width=5)
            instPar3Input.pack(padx=2)
            instPar3Input.config(textvariable=rt)

            rd = StringVar()
            rd.set(instructionBinary[16:20])
            instPar4 = Frame(instructionPreviewBinary)
            instPar4.pack(side=LEFT)
            instPar4Label = Label(instPar4,text="RD")
            instPar4Label.pack()
            instPar4Input = Entry(instPar4, width=5)
            instPar4Input.pack(padx=2)
            instPar4Input.config(textvariable=rd)

            shamt = StringVar()
            shamt.set(instructionBinary[21:25])
            instPar5 = Frame(instructionPreviewBinary)
            instPar5.pack(side=LEFT)
            instPar5Label = Label(instPar5,text="SHAMT")
            instPar5Label.pack()
            instPar5Input = Entry(instPar5, width=5)
            instPar5Input.pack(padx=2)
            instPar5Input.config(textvariable=shamt)

            funct = StringVar()
            funct.set(instructionBinary[26:31])
            instPar6 = Frame(instructionPreviewBinary)
            instPar6.pack(side=LEFT)
            instPar6Label = Label(instPar6,text="FUNCT")
            instPar6Label.pack()
            instPar6Input = Entry(instPar6, width=6)
            instPar6Input.pack(padx=2)
            instPar6Input.config(textvariable=funct)
        elif self.instructionType == 'I':
            instPar1 = Frame(instructionPreviewBinary)
            instPar1.pack(side=LEFT)
            instPar1Label = Label(instPar1,text="OP")
            instPar1Label.pack()
            instPar1Input = Entry(instPar1, width=6)
            instPar1Input.pack(padx=2)

            instPar2 = Frame(instructionPreviewBinary)
            instPar2.pack(side=LEFT)
            instPar2Label = Label(instPar2,text="RS")
            instPar2Label.pack()
            instPar2Input = Entry(instPar2, width=5)
            instPar2Input.pack(padx=2)

            instPar3 = Frame(instructionPreviewBinary)
            instPar3.pack(side=LEFT)
            instPar3Label = Label(instPar3,text="RT")
            instPar3Label.pack()
            instPar3Input = Entry(instPar3, width=5)
            instPar3Input.pack(padx=2)

            instPar4 = Frame(instructionPreviewBinary)
            instPar4.pack(side=LEFT)
            instPar4Label = Label(instPar4,text="ADDRESS")
            instPar4Label.pack()
            instPar4Input = Entry(instPar4, width=16)
            instPar4Input.pack(padx=2)
        elif self.instructionType == 'J':
            instPar1 = Frame(instructionPreviewBinary)
            instPar1.pack(side=LEFT)
            instPar1Label = Label(instPar1,text="OP")
            instPar1Label.pack()
            instPar1Input = Entry(instPar1, width=6)
            instPar1Input.pack(padx=2)

            instPar2 = Frame(instructionPreviewBinary)
            instPar2.pack(side=LEFT)
            instPar2Label = Label(instPar2,text="ADDRESS")
            instPar2Label.pack()
            instPar2Input = Entry(instPar2, width=26)
            instPar2Input.pack(padx=2)
        else:
            instMessage = Label(instructionPreviewBinary,text="- No instruction detected. Please click on one to continue. -")
            instMessage.pack()

    def getAssemblyFile(self):
        return self.codeDirectoryVar.get()
    
    def getBinaryFile(self):
        return self.binaryDirectoryVar.get()

    def createScreen(self):
        self.mainScreen = Tk()
        self.mainScreen.title('MIPS32 Assembly Decoder')
        #self.mainScreen.iconbitmap(r'src/icon.ico')
        self.width = 800
        self.height = 600
        self.mainScreen.geometry(str(self.width)+"x"+str(self.height))

        self.instructionType = ''

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
        helpMButton.add_command(label="About",command=lambda: messagebox.showinfo('About','MIPS32 Decoder, 2020'))

        # Instructions Preview

        instructionsPreview = Frame(self.mainScreen)
        instructionsPreview.pack()

        instructionsList = Frame(instructionsPreview)
        instructionsList.pack(side=LEFT,padx=50)

        instructionsListLabel = Label(instructionsList, text="Instructions")
        instructionsListLabel.pack()
        scrollbarInstructionsList = Scrollbar(instructionsList)
        scrollbarInstructionsList.pack( side = RIGHT, fill = Y )

        self.instructions = Listbox(instructionsList,yscrollcommand=scrollbarInstructionsList.set, height=5, selectmode=SINGLE)
        self.instructions.bind('<Double-Button-1>', self.printInstruction)
        self.instructions.pack(side=LEFT,fill=BOTH)
        scrollbarInstructionsList.config(command=self.instructions.yview)

        self.instructionPreview = Frame(instructionsPreview)
        self.instructionPreview.pack(side=LEFT)

        self.loadInstructionPreview()
        
        compileButton = Button(instructionsPreview, text="Compile!", width=20, command=lambda: self.decode())
        compileButton.pack(side=LEFT, padx=50)

        editors = Frame(self.mainScreen)
        editors.pack()
        
        # Assembly editor
        leftEditor = Frame(editors)
        leftEditor.pack(side=LEFT,fill=BOTH,padx=10, pady=5, expand=True)

        codeEditorLabel = Label(leftEditor,text="Assembly code editor")
        codeEditorLabel.pack(side=TOP)

        codeDirectory = Frame(leftEditor)
        codeDirectory.pack(fill=X)
        self.codeDirectoryVar = StringVar()
        inputCD = Entry(codeDirectory,width=52,textvariable=self.codeDirectoryVar,bg="white",fg="black")
        inputCD.pack(side=LEFT)
        buttonCD = Button(codeDirectory,text='...',command=lambda: self.openCodeFileGUI())
        buttonCD.pack(side=RIGHT)

        scrollbarCPx = Scrollbar(leftEditor, orient=HORIZONTAL)
        scrollbarCPx.pack(side=BOTTOM,fill=X)
        scrollbarCPy = Scrollbar(leftEditor, orient=VERTICAL)
        scrollbarCPy.pack(side=RIGHT,fill=Y)
        self.codePreview = Text(leftEditor,bg="white",width=40,fg="black",xscrollcommand=scrollbarCPx.set,yscrollcommand=scrollbarCPy.set,wrap=NONE) 
        self.codePreview.pack(fill=Y)
        scrollbarCPx.config(command=self.codePreview.xview)
        scrollbarCPy.config(command=self.codePreview.yview)

        # Binary editor
        rightEditor = Frame(editors)
        rightEditor.pack(side=RIGHT,fill=BOTH,padx=10, pady=5, expand=True)

        binaryEditorLabel = Label(rightEditor,text="Binary editor")
        binaryEditorLabel.pack(side=TOP)

        binaryDirectory = Frame(rightEditor)
        binaryDirectory.pack(fill=X)
        self.binaryDirectoryVar = StringVar()
        inputBD = Entry(binaryDirectory,textvariable=self.binaryDirectoryVar,width=52,bg="white",fg="black")
        inputBD.pack(side=LEFT)
        buttonBD = Button(binaryDirectory,text='...',command=lambda: self.openBinaryFileGUI())
        buttonBD.pack(side=RIGHT)

        scrollbarBPx = Scrollbar(rightEditor, orient=HORIZONTAL)
        scrollbarBPx.pack(side=BOTTOM,fill=X)
        scrollbarBPy = Scrollbar(rightEditor, orient=VERTICAL)
        scrollbarBPy.pack(side=RIGHT,fill=Y)
        self.binaryPreview = Text(rightEditor,bg="white",width=40,fg="black",xscrollcommand=scrollbarBPx.set,yscrollcommand=scrollbarBPy.set,wrap=NONE)
        self.binaryPreview.pack(fill=Y)
        scrollbarBPx.config(command=self.binaryPreview.xview)
        scrollbarBPy.config(command=self.binaryPreview.yview)

        self.statusBar = Label(self.mainScreen,relief=RAISED,anchor=W)
        self.statusBar.pack(side=BOTTOM,fill=X)

        pass

    def openCodeFileGUI(self):
        # Open file browser
        self.assemblyFile = filedialog.askopenfilename()
        self.openCodeFile()
        pass
    
    def openBinaryFileGUI(self):
        # Open file browser
        self.binaryFile = filedialog.askopenfilename()
        self.openBinaryFile()
        pass

    def openCodeFile(self):
        assemblyCode = open(self.assemblyFile, "r")
        print(self.assemblyFile)
        self.codeDirectoryVar.set(str(self.assemblyFile))
        self.codePreview.delete(1.0,END)
        self.codePreview.insert(1.0,assemblyCode.read())
        assemblyCode.close()
        self.updateLog("Assembly code file loaded.")
        pass
    
    def openBinaryFile(self):
        binaryCode = open(self.binaryFile, "r")
        print(self.binaryFile)
        self.binaryDirectoryVar.set(str(self.binaryFile))
        self.binaryPreview.delete(1.0,END)
        self.binaryPreview.insert(1.0,binaryCode.read())
        binaryCode.close()
        self.updateLog("Binary code file loaded.")
        pass

    def updateLog(self, message):
        self.statusBar.config(text=message)
        pass

    def startGUI(self):
        self.mainScreen.mainloop()
        pass
# Start main app
app = GUIDecoder()