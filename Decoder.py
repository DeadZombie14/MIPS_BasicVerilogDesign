# Decoder for MIPS32 Basic Verilog Implementation
# Made by DeadZombie14 (Mendoza Morelos Martin Mathier)
# Basically, translates MIPS32 assembly code to its binary representation format.
# Uses library tkinter as GUI library (Python 3 tk)


import os #To get current working directory
import re #To use regex function
from tkinter import *
from tkinter import filedialog # To open file dialogs
from tkinter import messagebox # To send messages in new windows

# Default memory layout configuration
charsPerLine = 8 #37 #8
minimumLines = 128 #32 #128

cwd = os.getcwd() # Current working directory

assemblyInstructionlist = [
            {'id':'NOP' ,'op':'000000', 'funct':'000000'},
            {'id':'ADD' ,'op':'000000', 'funct':'100000'},
            {'id':'SUB' ,'op':'000000', 'funct':'100010'},
            {'id':'MUL' ,'op':'011100', 'funct':'000010'},
            {'id':'DIV' ,'op':'000000', 'funct':'011010'},
            {'id':'AND' ,'op':'000000', 'funct':'100100'},
            {'id':'OR'  ,'op':'000000', 'funct':'100101'},
            {'id':'NOR' ,'op':'000000', 'funct':'100111'},
            {'id':'XOR' ,'op':'000000', 'funct':'100110'},
            {'id':'SLT' ,'op':'000000', 'funct':'101010'},
            {'id':'SLL' ,'op':'000000', 'funct':'000000'},
            {'id':'SRL' ,'op':'000000', 'funct':'000010'},
            {'id':'LW'  ,'op':'100011', 'funct':'000000'},
            {'id':'SW'  ,'op':'101011', 'funct':'000000'},
            {'id':'J'   ,'op':'000010', 'funct':'000000'},
            {'id':'JAL' ,'op':'000011', 'funct':'000000'},
            {'id':'JR'  ,'op':'000000', 'funct':'001000'},
            {'id':'BEQ' ,'op':'000100', 'funct':'000000'},
            {'id':'SLTI','op':'001010', 'funct':'000000'},
            {'id':'ADDI','op':'001000', 'funct':'000000'},
            {'id':'ANDI','op':'001100', 'funct':'000000'},
            {'id':'ORI' ,'op':'001101', 'funct':'000000'}
        ]

class Decoder:
    def __init__(self):
        self.functionProgramList = [] # This keeps all functions labels and values
        self.instructionList = [] # This keeps all instructions in the program in its text format, binary format and stores its instruction type
        self.functCounter = 1 # This keeps the amount of funct we have in this program
        self.instCounter = 1 # This keeps the amount of inst we have in this program
        pass

    def decode(self, guiInterface):
        guiInterface.clearInstructions()
        guiInterface.clearFunctions()
        self.readAssembly(guiInterface, guiInterface.getAssemblyFile(), guiInterface.getBinaryFile())
        pass

    def readAssembly(self, guiInterface, assemblyFile, binaryFile):
        assemblyFile = open(assemblyFile, "r")
        instMemoryFile = open(binaryFile,"w+")
        i = 0
        ### For each line in file
        for line in assemblyFile:
            ### If line isn't blank
            if line.rstrip() != "":
                ### If it isn't a commentary
                if line.rstrip()[0] != "#":
                    ### If it is a function label
                    if line.rstrip()[-1] == ":":
                        functionLabel = line.rstrip()
                        functionLabel = functionLabel[:-1]
                        newFunction = {"functID":self.functCounter,"label":functionLabel,"instAddress":((self.instCounter)*4)-4}
                        self.functionProgramList.append(newFunction)
                        self.functCounter = self.functCounter+1
                    else:
                        ### It contains instructions, read all of them
                        self.readInstructionsPerLine(line)
        # For each function in general
        for function in self.functionProgramList:
            print(function)
            guiInterface.insertFunction(function)
        # For each instruction in general
        for instruction in self.instructionList:
            guiInterface.insertInstruction(instruction)
            # Split binary in 8 digits format (file only)
            for j in range(0, len(instruction["binary"]), charsPerLine):
                lineaNueva = instruction["binary"][j:j+charsPerLine]
                instMemoryFile.write(lineaNueva)
                instMemoryFile.write("\n")
                i = i + 1
        # Fill the rest with instructions NOP (00000000000000000000000000000000)
        for k in range(i,minimumLines,1):
            nopFunction = "0" * charsPerLine
            instMemoryFile.write(nopFunction)
            #Avoid writing more than maximum inst memory size
            if k != minimumLines-1:
                instMemoryFile.write("\n")
        assemblyFile.close()
        instMemoryFile.close()

    def readInstructionsPerLine(self,line):
        ### Ignore any comment after the instructions
        cut = line.find("#")
        if cut:
            line = line[:cut] # cut the rest of the line

        ### Read instruction by instruction from the line given
        ### NOTE: At the end I decided to just handle 1 instruction per line ###
        returnedData = self.readInstruction(line)
        newInst = {"instID":self.instCounter,"text":line.strip(),"binary":returnedData[0],"type":returnedData[1]}
        self.instCounter = self.instCounter + 1
        print(newInst)
        self.instructionList.append(newInst)
        pass

    def readInstruction(self,instructionText):
        for instruction in assemblyInstructionlist:
            if instructionText.split()[0].upper() == instruction["id"]:
                if instruction["op"] == "000000" and instruction["id"] != "SLL" and instruction["id"] != "SRL":
                    instructionType = "R"
                    parameters = self.readParametersR(instructionText)
                    return (instruction["op"] + parameters + instruction["funct"], instructionType)
                elif instruction["op"] == "000000" and (instruction["id"] == "SLL" or instruction["id"] == "SRL")  : # R: Special
                    instructionType = "R"
                    parameters = self.readParametersRSA(instructionText)
                    return (instruction["op"] + parameters + instruction["funct"], instructionType)
                elif instruction["op"] == "000100": # I: BEQ
                    instructionType = "I"
                    parameters = self.readParametersI(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "100011": # I: LW
                    instructionType = "IS"
                    parameters = self.readParametersISWLW(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "101011": # I: SW
                    instructionType = "IS"
                    parameters = self.readParametersISWLW(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "001010": # I: SLTI
                    instructionType = "I"
                    parameters = self.readParametersI(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "001100": # I: ANDI
                    instructionType = "I"
                    parameters = self.readParametersI(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "001000": # I: ADDI
                    instructionType = "I"
                    parameters = self.readParametersI(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "001101": # I: ORI
                    instructionType = "I"
                    parameters = self.readParametersI(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "000010": # J: J
                    instructionType = "J"
                    parameters = self.readParametersJ(instructionText)
                    return (instruction["op"] + parameters, instructionType)
                elif instruction["op"] == "000011": # J: JAL
                    instructionType = "J"
                    parameters = self.readParametersJ(instructionText)
                    return (instruction["op"] + parameters, instructionType)

    # Parameters for instruction type R
    def readParametersR(self, line):
        # Split 3 parameters from instruction
        parameters = ""
        for i in range(1,4):
            word = line.split()[i]
            word = word[1:] # Cut $ sign
            if word[-1] == ",":
                word = word[:-1] # Cut , sign if exists
            parameters = parameters + f"{int(word):05b}"
        return parameters + "00000" # now shamt is 0
    
    # Parameters for instruction type R SPECIAL
    def readParametersRSA(self, line):
        # Split 2 parameters from instruction
        parameters = ""
        for i in range(1,3):
            word = line.split()[i]
            word = word[1:] # Cut $ sign
            if word[-1] == ",":
                word = word[:-1] # Cut , sign if exists
            parameters = parameters + f"{int(word):05b}"
        word = line.split()[3]
        parameters = parameters + f"{int(word):05b}" # Include the shamt value
        return "00000" + parameters # now rs is 0

    # Parameters for instruction type I
    def readParametersI(self, line):
        # Split 3 parameters from instruction
        parameters = ""
        for i in range(1,3):
            word = line.split()[i]
            word = word[1:] # Cut $ sign
            if word[-1] == ",":
                word = word[:-1] # Cut , sign if exists
            parameters = parameters + f"{int(word):05b}"
        # Get lower 16 bits from instruction
        word = line.split()[3]
        if word[1] == "#":
            word = word[1:] # Cut hashtag sign if exists
        parameters = parameters + f"{int(word):016b}"
        return parameters

    # Parameters for instruction type I SW/LW
    def readParametersISWLW(self, line):
        # Split 3 parameters from instruction
        
        # First parameter: rt value
        parameters = ""
        word = line.split()[1]
        word = word[1:] # Cut $ sign
        if word[-1] == ",":
            word = word[:-1] # Cut , sign if exists
        parameters = parameters + f"{int(word):05b}"

        word = line.split()[2]

        # Third parameter: base value
        baseValue = re.search('\(([^)]+)', word).group(1)
        parameters = parameters + f"{int(baseValue):05b}" # Extract content inside parenthesis

        # Second parameter: offset value
        offsetValue = word[:word.find("(")] # Erase everything after the first parenthesis
        parameters = parameters + f"{int(offsetValue):016b}"
        return parameters

    # Parameters for instruction type J
    def readParametersJ(self, line):
        parameters = ""
        word = line.split()[1]
        # If instAddress was specified
        if re.search('^[0-9]', word):
            print("WORD: "+word)
            parameters = f"{int(word):026b}"
            print("PARAMETERS: "+parameters)
            return parameters
        else:
            # Find function in functList and replace its label to its instAddress
            for function in self.functionProgramList:
                if word == function['label']:
                    parameters = f"{int(function['instAddress']):026b}"
            return parameters

class GUIDecoder:
    def __init__(self):
        self.instructionsArray = {}

        self.decoder = Decoder()
        self.createScreen()

        self.startGUI()
        pass

    def decode(self):
        self.decoder.decode(self)
        self.functions.selection_set(0,0)
        self.updateLog("Instructions decoded.")
        self.openCodeFile()
        self.openBinaryFile()
        pass

    def printInstruction(self, event):
        instructionID = self.instructions.curselection()[0]
        # print(instructionID)
        self.instructionType = self.decoder.instructionList[instructionID]['type']
        self.loadInstructionPreview(self.decoder.instructionList[instructionID])
        pass

    def insertInstruction(self, instruction):
        self.instructions.insert(instruction["instID"], instruction["text"])
        pass

    def clearInstructions(self):
        self.decoder.instructionList = []
        self.instructions.delete(0, END)
        self.decoder.instCounter = 1
        pass

    def printFunction(self, event):
        functionID = self.functions.curselection()[0]
        self.instructions.delete(0, END)
        if functionID == 0:
            for instruction in self.decoder.instructionList:
                self.insertInstruction(instruction)
        # print(functionID)
        pass

    def insertFunction(self, function):
        self.functions.insert(function["functID"], function["label"]+" (instID: "+str(function["instAddress"])+")")
        pass

    def clearFunctions(self):
        self.decoder.functionProgramList = []
        self.functions.delete(1, END)
        self.decoder.functCounter = 1
        pass

    def loadInstructionPreview(self, instruction={}):
        for widget in self.instructionPreview.winfo_children():
            widget.destroy()
        
        instructionPreviewLabel = Label(self.instructionPreview, text="Instruction Analysis")
        instructionPreviewLabel.pack(pady=5)
        instructionPreviewBinary = Frame(self.instructionPreview)
        instructionPreviewBinary.pack()

        if instruction:
            instructionID= instruction["instID"]*4
            instructionBinary= instruction["binary"]

            op = StringVar()
            op.set(instructionBinary[1:6])
            rs = StringVar()
            rs.set(instructionBinary[6:11])
            rt = StringVar()
            rt.set(instructionBinary[11:16])
            rd = StringVar()
            rd.set(instructionBinary[16:21])
            shamt = StringVar()
            shamt.set(instructionBinary[21:26])
            funct = StringVar()
            funct.set(instructionBinary[26:32])
            rdshft = StringVar()
            rdshft.set(instructionBinary[16:32])
            address = StringVar()
            address.set(instructionBinary[6:32])

            instID = Frame(instructionPreviewBinary)
            instID.pack(side=TOP)
            instIDLabel = Label(instID,text="Instruction ID")
            instIDLabel.pack()
            instIDInput = Label(instID, width=6, text = instructionID, relief=SUNKEN, bg="white")
            instIDInput.pack(padx=2)

            if(self.instructionType == 'R'):

                instPar1 = Frame(instructionPreviewBinary)
                instPar1.pack(side=LEFT)
                instPar1Label = Label(instPar1,text="OP")
                instPar1Label.pack()
                instPar1Input = Entry(instPar1, width=6)
                instPar1Input.pack(padx=2)
                instPar1Input.config(textvariable=op)

                instPar2 = Frame(instructionPreviewBinary)
                instPar2.pack(side=LEFT)
                instPar2Label = Label(instPar2,text="RS")
                instPar2Label.pack()
                instPar2Input = Entry(instPar2, width=5)
                instPar2Input.pack(padx=2)
                instPar2Input.config(textvariable=rs)

                instPar3 = Frame(instructionPreviewBinary)
                instPar3.pack(side=LEFT)
                instPar3Label = Label(instPar3,text="RT")
                instPar3Label.pack()
                instPar3Input = Entry(instPar3, width=5)
                instPar3Input.pack(padx=2)
                instPar3Input.config(textvariable=rt)

                instPar4 = Frame(instructionPreviewBinary)
                instPar4.pack(side=LEFT)
                instPar4Label = Label(instPar4,text="RD")
                instPar4Label.pack()
                instPar4Input = Entry(instPar4, width=5)
                instPar4Input.pack(padx=2)
                instPar4Input.config(textvariable=rd)

                instPar5 = Frame(instructionPreviewBinary)
                instPar5.pack(side=LEFT)
                instPar5Label = Label(instPar5,text="SHAMT")
                instPar5Label.pack()
                instPar5Input = Entry(instPar5, width=5)
                instPar5Input.pack(padx=2)
                instPar5Input.config(textvariable=shamt)

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
                instPar1Input.config(textvariable=op)

                instPar2 = Frame(instructionPreviewBinary)
                instPar2.pack(side=LEFT)
                instPar2Label = Label(instPar2,text="RS")
                instPar2Label.pack()
                instPar2Input = Entry(instPar2, width=5)
                instPar2Input.pack(padx=2)
                instPar2Input.config(textvariable=rs)

                instPar3 = Frame(instructionPreviewBinary)
                instPar3.pack(side=LEFT)
                instPar3Label = Label(instPar3,text="RT")
                instPar3Label.pack()
                instPar3Input = Entry(instPar3, width=5)
                instPar3Input.pack(padx=2)
                instPar3Input.config(textvariable=rt)

                instPar4 = Frame(instructionPreviewBinary)
                instPar4.pack(side=LEFT)
                instPar4Label = Label(instPar4,text="ADDRESS")
                instPar4Label.pack()
                instPar4Input = Entry(instPar4, width=16)
                instPar4Input.pack(padx=2)
                instPar4Input.config(textvariable=rdshft)
            elif self.instructionType == 'IS': # IS is for LW/SW
                instPar1 = Frame(instructionPreviewBinary)
                instPar1.pack(side=LEFT)
                instPar1Label = Label(instPar1,text="OP")
                instPar1Label.pack()
                instPar1Input = Entry(instPar1, width=6)
                instPar1Input.pack(padx=2)
                instPar1Input.config(textvariable=op)

                instPar2 = Frame(instructionPreviewBinary)
                instPar2.pack(side=LEFT)
                instPar2Label = Label(instPar2,text="BASE")
                instPar2Label.pack()
                instPar2Input = Entry(instPar2, width=5)
                instPar2Input.pack(padx=2)
                instPar2Input.config(textvariable=rt)

                instPar3 = Frame(instructionPreviewBinary)
                instPar3.pack(side=LEFT)
                instPar3Label = Label(instPar3,text="RT")
                instPar3Label.pack()
                instPar3Input = Entry(instPar3, width=5)
                instPar3Input.pack(padx=2)
                instPar3Input.config(textvariable=rs)

                instPar4 = Frame(instructionPreviewBinary)
                instPar4.pack(side=LEFT)
                instPar4Label = Label(instPar4,text="OFFSET")
                instPar4Label.pack()
                instPar4Input = Entry(instPar4, width=16)
                instPar4Input.pack(padx=2)
                instPar4Input.config(textvariable=rdshft)
            elif self.instructionType == 'J':
                instPar1 = Frame(instructionPreviewBinary)
                instPar1.pack(side=LEFT)
                instPar1Label = Label(instPar1,text="OP")
                instPar1Label.pack()
                instPar1Input = Entry(instPar1, width=6)
                instPar1Input.pack(padx=2)
                instPar1Input.config(textvariable=op)

                instPar2 = Frame(instructionPreviewBinary)
                instPar2.pack(side=LEFT)
                instPar2Label = Label(instPar2,text="ADDRESS")
                instPar2Label.pack()
                instPar2Input = Entry(instPar2, width=26)
                instPar2Input.pack(padx=2)
                instPar2Input.config(textvariable=address)
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
        self.width = 1000
        self.height = 600
        self.mainScreen.geometry(str(self.width)+"x"+str(self.height))
        self.mainScreen.minsize(self.width,self.height)
        self.mainScreen.maxsize(self.width,self.height)

        self.instructionType = ''

        # Create menu toolbar
        menubar = Menu(self.mainScreen)
        self.mainScreen.config(menu=menubar)
        
        # Entry 1: File manager
        fileMButton = Menu(menubar, tearoff=0) # Tearoff removes dashed lines
        menubar.add_cascade(label='File',menu=fileMButton)
        fileMButton.add_command(label="Exit",command=lambda: quit())

        # Entry 2: Help
        helpMButton = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help',menu=helpMButton)
        helpMButton.add_command(label="About",command=lambda: messagebox.showinfo('About','MIPS32 Decoder, 2020'))

        # Instructions Preview

        instructionsPreview = Frame(self.mainScreen)
        instructionsPreview.pack()

        # Function Preview List
        functionsList = Frame(instructionsPreview)
        functionsList.pack(side=LEFT,padx=5)
        functionsListLabel = Label(functionsList, text="Function List")
        functionsListLabel.pack()
        scrollbarfunctionsList = Scrollbar(functionsList)
        scrollbarfunctionsList.pack( side = RIGHT, fill = Y )
        self.functions = Listbox(functionsList,yscrollcommand=scrollbarfunctionsList.set, height=5, selectmode=SINGLE)
        self.functions.bind('<Double-Button-1>', self.printFunction)
        self.functions.pack(side=LEFT,fill=BOTH)
        scrollbarfunctionsList.config(command=self.functions.yview)
        self.functions.insert(0, "(none)")

        # Instruction Preview List
        instructionsList = Frame(instructionsPreview)
        instructionsList.pack(side=LEFT,padx=10)
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
        
        editButtons = Frame(instructionsPreview)
        editButtons.pack(side=LEFT, padx=50)
        compileButton = Button(editButtons, text="Compile!", width=20, command=lambda: self.decode())
        compileButton.pack()
        self.saveButton = Button(editButtons, text="Save all", width=20, command=lambda: self.saveAll(), state=DISABLED)
        self.saveButton.pack(pady=10)

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
        self.codePreview.bind("<Key>", self.detectChanges)  
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
        self.binaryPreview.bind("<Key>", self.detectChanges)
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
        self.binaryFile = filedialog.asksaveasfilename(initialdir = "/",title = "Save file as..",
        filetypes = (("MIPS memory file","*.mem"),("Binary file","*.file"),("All files","*.*")))
        assemblyCode = open(self.binaryFile, "w+")
        assemblyCode.close()        
        self.openBinaryFile()
        pass

    def openCodeFile(self):
        assemblyCode = open(self.assemblyFile, "r")
        self.codeDirectoryVar.set(str(self.assemblyFile))
        self.codePreview.delete(1.0,END)
        self.codePreview.insert(1.0,assemblyCode.read())
        assemblyCode.close()
        self.updateLog("Assembly code file loaded.")
        pass
    
    def openBinaryFile(self):
        binaryCode = open(self.binaryFile, "r")
        self.binaryDirectoryVar.set(str(self.binaryFile))
        self.binaryPreview.delete(1.0,END)
        self.binaryPreview.insert(1.0,binaryCode.read())
        binaryCode.close()
        self.updateLog("Binary code file loaded.")
        pass

    def detectChanges(self, event):
        self.saveButton.config(state=NORMAL)
        self.updateLog("Changes unsaved. Please click on save changes","red")
        pass
    
    def saveAll(self):
        assemblyFile = open(self.codeDirectoryVar.get(), "w")
        binaryFile = open(self.binaryDirectoryVar.get(), "w")
        assemblyFile.write(self.codePreview.get(1.0,END))
        binaryFile.write(self.binaryPreview.get(1.0,END))
        assemblyFile.close()
        binaryFile.close()

        self.saveButton.config(state=DISABLED)
        self.updateLog("Changes saved.","green")
        pass

    def updateLog(self, message, fgcolor="black"):
        self.statusBar.config(text=message)
        self.statusBar.config(fg=fgcolor)
        pass

    def startGUI(self):
        self.mainScreen.mainloop()
        pass
# Start main app
app = GUIDecoder()