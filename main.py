#!/usr/bin/python3
import os
import sys
import random
import time
import cmath

trying = False
def s(text: str):
    return text.split("(")
global rufc
rufc = False
var = {}
var["pi"] = cmath.pi
funcs = {}
libs = []
dirlibs = []
out = ""
def read(code):
    global rufc
    global trying
    rufc = False
    code = list(code)
    out = ""
    typel = ""
    i = 0
    while i < len(code):
        line = str(code[i])
        try:
            end = code.index("end(", i)
        except:
            end = len(code)
        if s(line)[0] == "prt":
            full = ""
            for thingie in s(line)[1].split():
                if var.get(thingie) != None:
                    full += str(var.get(thingie)) + " "
                else:
                    full += str(thingie) + " "
            print(full)
        elif s(line)[0] == "into":
            do = input()
            var.update({str(s(line)[1]): do})
        elif s(line)[0] == "get":
            if os.path.exists(s(line)[1]):
                if os.path.isdir(s(line)[1]):
                    dirlibs.append(s(line)[1])
                else:
                    libs.append(s(line)[1])
        elif s(line)[0] == "runlib":
            if libs.count(s(line)[1]) > 0:
                with open(s(line)[1]) as f:
                    rd = []
                    r = f.readlines()
                    for line in r:
                        rd.append(line.rstrip())
                    read(rd)
        elif s(line)[0] == "uselib":
                if dirlibs.count(s(line)[1]) > 0:
                    if os.path.exists(f"{s(line)[1]}/{s(line)[2]}"):
                        with open(f"{s(line)[1]}/{s(line)[2]}") as f:
                            r = f.readlines()
                            rd = []
                            for line in r:
                                rd.append(line.rstrip())
                            read(rd)
        elif s(line)[0] == "if!=":
            if var.get(s(line)[1]) == None:
                v1 = "str"
            else:
                v1 = "var"
            if var.get(s(line)[2]) == None:
                v2 = "str"
            else:
                v2 = "var"
            if v1 == "str" and v2 == "str":
                if s(line)[1] != s(line)[2]:
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "var":
                if var.get(s(line)[1]) != var.get(s(line)[2]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "str" and v2 == "var":
                if s(line)[1] != var.get(s(line)[1]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "str":
                if var.get(s(line)[1]) != s(line)[2]:
                    out = "True"
                else:
                    out = "False"
            var.update({s(line)[3]: out})
            if out == "False":
                i = end
        elif s(line)[0] == "if=":
            if var.get(s(line)[1]) == None:
                v1 = "str"
            else:
                v1 = "var"
            if var.get(s(line)[2]) == None:
                v2 = "str"
            else:
                v2 = "var"
            if v1 == "str" and v2 == "str":
                if s(line)[1] == s(line)[2]:
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "var":
                if var.get(s(line)[1]) == var.get(s(line)[2]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "str" and v2 == "var":
                if s(line)[1] == var.get(s(line)[1]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "str":
                if var.get(s(line)[1]) == s(line)[2]:
                    out = "True"
                else:
                    out = "False"
            var.update({s(line)[3]: out})
            if out == "False":
                i = end
        elif s(line)[0] == "frvr":
            start = i
            typel = "loopf"
        # elif s(line)[0] == "rpt":
        #     start = i
        #     typel = "loopr"
        #     times = s(line)[1]
        elif s(line)[0] == "brk":
            typel = "brk"
        elif s(line)[0] == "end":
            end = i
            if typel == 'loopf':
                i = start
                continue
            if rufc == True:
                i = gt + 1
                rufc = False
                continue
            if typel == 'brk':
                start = i+1
                continue
            if trying:
                trying = False
                continue
            
        elif s(line)[0] == "runpy":
            os.system(f"python3 {s(line)[1]}")
        elif line.startswith("##"):
            pass
        elif line == "" or line.lower() == "run":
            pass
        elif s(line)[0] == "func":
            funcs[s(line)[1]] = (i, end)
        elif s(line)[0] == "rfunc":
            if funcs.get(s(line)[1]) != None:
                gt = i
                i = funcs.get(s(line)[1])[0] + 1
                rufc = True
            else:
                print("No such function:",s(line)[1])
        elif s(line)[0] == "vardef":
            var[s(line)[1]] = s(line)[2]
        elif s(line)[0] == "rvar":
            try:
                var.pop(s(line)[1])
            except:
                if not trying:
                    print("KeydelError in line",str(line))
                    quit(2)
                else:
                    pass
        elif s(line)[0] == "rmfunc":
            try:
                funcs.pop(s(line)[1])
            except:
                if not trying:
                    print("KeydelError in line",str(line))
                    quit(2)
        elif s(line)[0] == "quit":
            print(s(line)[1])
            quit(int(s(line)[2]))
        elif s(line)[0] == "exit":
            exit(0)
        elif s(line)[0] == "add":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(float(op1) + float(op2))
            except:
                if not trying:
                    print("BasicMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "sub":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(float(op1) - float(op2))
            except:
                if not trying:
                    print("BasicMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "mul":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(float(op1) * float(op2))
            except:
                if not trying:
                    print("BasicMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "div":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(float(op1) / float(op2))
            except:
                if not trying:
                    print("BasicMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "pow":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(float(op1) ** float(op2))
            except:
                if not trying:
                    print("ComplexMathICanterror in line", str(line))
                    quit(2)
                    print("What? You broke the laws of Pythonics with this one.")
        elif s(line)[0] == "abs":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                var[s(line)[2]] = str(abs(float(op1)))
            except:
                if not trying:
                    print("ComplexMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "min":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(min(float(op1), float(op2)))
            except:
                if not trying:
                    print("ComplexMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "max":
            try:
                op1 = var.get(s(line)[1], s(line)[1])
                op2 = var.get(s(line)[2], s(line)[2])
                var[s(line)[3]] = str(max(float(op1), float(op2)))
            except:
                if not trying:
                    print("ComplexMathICanterror in line", str(line))
                    quit(2)
        elif s(line)[0] == "rand":
            try:
                op1 = int(var.get(s(line)[1], s(line)[1]))
                op2 = int(var.get(s(line)[2], s(line)[2]))
                var[s(line)[3]] = str(random.randint(op1, op2))
            except:
                if not trying:
                    print("RandomError in line", str(line))
                    quit(2)
        elif s(line)[0] == "wait":
            try:
                op = var.get(s(line)[1], s(line)[1])
                time.sleep(float(op))
            except:
                if not trying:
                    print("TimeError in line", str(line))
                    quit(2)
        elif s(line)[0] == "rprt":
            print(s(line)[1:])
        elif s(line)[0] == "try":
            trying = True
        elif s(line)[0] == "len":
            try:
                op = var.get(s(line)[1], s(line)[1])
                var[s(line)[2]] = len(op)
            except:
                print("LengthError in line:",str(line))
                quit(2)
        elif s(line)[0] == "choice":
            op = var.get(s(line)[1], s(line)[1])
            var[s(line)[2]] = random.choice(op)
        else:
            print("Err in line",str(i)+": Unsupported","'"+str(line)+"'")
            quit(1)
        i += 1
        
def rfl(file):
    rode = []
    with open(file,"r") as f:
        reads = f.readlines()
    for one in reads:
        one = one.rstrip()
        rode.append(one)
    read(rode)
if len(sys.argv) > 1:
    rfl(sys.argv[1])
    input("Press Enter to continue . . . ")
else:
    b = []
    print("Pur Interpreter 2.2 on " + str(os.uname()[0]), str(os.uname()[1]))
    while True:
        a = input(": ")
        if a.lower() == "run":
            read(b)
            a = ""
            del a
        else:
            b.append(a)
