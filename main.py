#!/usr/bin/python3
import os
import sys
def s(text: str):
    return text.split("(")
global rufc
rufc = False
var = {}
funcs = {}
libs = []
dirlibs = []
out = ""
def read(code):
    global rufc
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
            if var.get(s(line)[1]) == None:
                print(s(line)[1])
            else:
                print(var.get(s(line)[1]))
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
        elif s(line)[0] == "end":
            end = i
            if typel == 'loopf':
                i = start
            if rufc == True:
                i = gt + 1
                rufc = False
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
    a = ""
    b = []
    print("Pur Interpreter 1.6 on " + str(os.uname()[0]), str(os.uname()[1]))
    while True:
        if a.lower() == "run":
            read(b)
            a = ""
        
        else:
            a = input(": ")
            b.append(a)
