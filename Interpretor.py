def Get_Inputs(tokens):
    if tokens[0] == "NIN":
        Variables[int(tokens[1])] = float(input())
    elif tokens[0] == "AIN":
        Input = [ord(Chr) for Chr in input()]
        Input = [str(Chr).zfill(3) for Chr in Input]
        EncodedString = "".join(Input)
        Variables[int(Tokens[1])] = float(EncodedString)

def Print_Outputs(tokens):
    if tokens[0] == "NOUT":
        print(Variables[int(tokens[1])])
    elif tokens[0] == "AOUT":
        VariableIndex = float(tokens[1])
        EncodedString = str(Variables[VariableIndex])
        EncodedString = EncodedString.zfill(len(EncodedString) + ((3 - len(EncodedString) % 3) % 3 or 3))
        Output = [EncodedString[i:i+3] for i in range(0, len(str(EncodedString)), 3)]
        Output = [chr(int(Chr)) for Chr in Output if Chr.isdigit()]
        Output = "".join(Output)
        Output = str(Output)
        print(Output)

def Arithmetic():
    try :
        if Function == "ADD":
            Variables[Result_Address] = Variables[First_Address] + Variables[Second_Address]
        if Function == "SUB":
            Variables[Result_Address] = Variables[First_Address] - Variables[Second_Address]
        if Function == "MUL":
            Variables[Result_Address] = Variables[First_Address] * Variables[Second_Address]
        if Function == "DIV":
            Variables[Result_Address] = Variables[First_Address] / Variables[Second_Address]
        if Function == "MOD":
            Variables[Result_Address] = Variables[First_Address] % Variables[Second_Address]
        if Function == "EXP":
            Variables[Result_Address] = Variables[First_Address] ** Variables[Second_Address]
        if Function == "FLD":
            Variables[Result_Address] = Variables[First_Address] // Variables[Second_Address]
    except Exception as e:
        print("Error ",e)

def Conditional():
    if Function == "EQA":
        Variables[Result_Address] = (Variables[First_Address] == Variables[Second_Address])
    if Function == "NEQ":
        Variables[Result_Address] = (Variables[First_Address] != Variables[Second_Address])
    if Function == "GT":
        Variables[Result_Address] = (Variables[First_Address] > Variables[Second_Address])
    if Function == "LT":
        Variables[Result_Address] = (Variables[First_Address] < Variables[Second_Address])
    if Function == "GEQ":
        Variables[Result_Address] = (Variables[First_Address] >= Variables[Second_Address])
    if Function == "LEQ":
        Variables[Result_Address] = (Variables[First_Address] <= Variables[Second_Address])

def Logical():
    First_Number = Variables[First_Address]
    Second_Number = Variables[Second_Address]

    if Function == "AND":
        Variables[Result_Address] = int(First_Number and Second_Number)
    elif Function == "OR":
        Variables[Result_Address] = int(First_Number or Second_Number)
    elif Function == "XOR":
        Variables[Result_Address] = int((First_Number or Second_Number) and not (First_Number and Second_Number))
    elif Function == "XNOR":
        Variables[Result_Address] = int((First_Number and Second_Number) or (not First_Number and not Second_Number))
    elif Function == "NAND":
        Variables[Result_Address] = int(not (First_Number and Second_Number))
    elif Function == "NOR":
        Variables[Result_Address] = int(not (First_Number or Second_Number))

def Control(tokens):
    if Function == "JMP":
        Counter = int(tokens[1])
    elif Function == "JIC":
        if Variables[int(tokens[2])] == 1:
            Counter = int(tokens[1])

Program_Name = input("Enter Program Name: ")

with open(Program_Name, "r") as f:
    Program = f.readlines()

Program = [Line.replace("\n", "") for Line in Program]
Program = [Line for Line in Program if Line != ""]

Counter = 0
Variables = []  #Initialize an empty list for variables

Input_Functions = ["NIN", "AIN"]
Output_Functions = ["NOUT", "AOUT"]
Arithmetic_Functions = ["ADD", "SUB", "MUL", "DIV", "MOD", "EXP", "FLD"]
Conditional_Functions = ["EQA", "NEQ", "GT", "LT", "GEQ", "LEQ"]
Logical_Functions = ["AND", "OR", "XOR", "XNOR", "NAND", "NOR"]
Control_Functions = ["JMP", "JIC"]

while Counter < len(Program):
    if Program[Counter] == "END":
        break

    Line = Program[Counter]
    
    Tokens = Line.split(" ")

    print(Tokens)

    for token in Tokens:
        if token.isdigit():
            if not(Tokens[0] == "SET" and Tokens[2] == token):
                # Handle numeric literals as variable indices
                variable_index = int(token)
                if variable_index >= len(Variables):
                    Variables.extend([0] * (variable_index - len(Variables) + 1))
    
    while "VAR" in Tokens:
        index = Tokens.index("VAR")
        Tokens[index] = Variables[Tokens[index + 1]]
        Tokens.pop(index + 1)

    if Tokens[0] in Input_Functions:
        Get_Inputs(Tokens)
    if Tokens[0] in Output_Functions:
        Print_Outputs(Tokens)
    if Tokens[0] == "SET":
        Variables[int(Tokens[1])] = float(Tokens[2])
    if Tokens[0] == "COPY":
        Variables[int(Tokens[1])] = Variables[int(Tokens[2])]
    if Tokens[0] in Arithmetic_Functions or Tokens[0] in Conditional_Functions or Tokens[0] in Logical_Functions:
        Function = Tokens[0]
        Function = Tokens[0]
        Result_Address = float(Tokens[1])
        First_Address = float(Tokens[2])
        Second_Address = float(Tokens[3])
    if Tokens[0] in Arithmetic_Functions:
        Arithmetic()
    if Tokens[0] in Conditional_Functions:
        Conditional()
    if Tokens[0] in Logical_Functions:
        Logical()
    if Tokens[0] in Control_Functions:
        Control(Tokens)

    Counter += 1

print(Variables) 