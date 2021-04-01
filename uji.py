import library as lib

CG1 = 420/500
CG2 = -420/250

D1 = lib.Delay(0, "D1")

INP = lib.Input("INP")

G1 = lib.Gain(CG1, "G1")
G2 = lib.Gain(CG2, "G2")

GM1 = lib.Gain(-1, "GM1")
GM2 = lib.Gain(-1, "GM2")
GM1.setLastObject(lib.Input("InGM1"))
GM2.setLastObject(lib.Input("InGM2"))

def Adder(x,y):
    if(not x):
        return y
    elif(not y):
        return x
    else:
        return x + y

F1 = lib.FeedbackCascade(0, "F1")
F1.setTopSM(GM1)

F2 = lib.FeedbackCascade(0, "F2")
F2.setTopSM(GM2)

P1 = lib.Parallel(Adder, "P1")
P2 = lib.Parallel(Adder, "P2")

P1.appendLast(INP, F2)

G1.setLastObject(P1)

P2.appendLast(G1, F1)
G2.setLastObject(P2)

D1.setLastObject(G2)

CMAIN = lib.Cascade("CMAIN")
CMAIN.setTopSM(D1)
CMAIN.appendFeedback(F1, F2)