import BFuzzy
R_MIN=-30
R_MAX=50
A=4.0
B=7.0
C=9.0
D=11.0
fuzzy=BFuzzy.Bfuzzy(A,B,C,D)


def setup():
    size(1401,1500)
    drawCanvas()
    
def drawCanvas():
    fill(0,210,160)
    stroke(0,210,160)
    rect(400,0,1100,1500) #CANVAS
    fill(255,255,255)
    stroke(255,255,255)
    rect(0,0,400,1500)#JUEGO
    fill(100,60,200)
    stroke(100,60,200)
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    text("Biblioteca FUZZY",30,30)
    fill(255,255,255)
    stroke(0,0,0)
    rect(100,100,220,50,20)
    rect(100,200,220,50,20)
    rect(100,300,220,50,20)
    rect(100,400,220,50,20)
    rect(100,500,220,50,20)
    rect(100,600,220,50,20)
    rect(100,700,220,50,20)
    rect(100,800,220,50,20)
    fill(0,0,0)
    stroke(0,0,0)
    text("Trapecio Abierto Izq",110,125)
    text("Trapecio Abierto Der",110,225)
    text("Triangular",110,325)
    text("Trapezoidal",110,425)
    text("Curva S",110,525)
    text("Curva Z",110,625)
    text("Triangular suave",110,725)
    text("Trapezoidal suave",110, 825)
    
def draw():
    p=False

def mousePressed():
    if mouseX>=100 and mouseX<=320:
        if mouseY>=100 and mouseY<=150:
            TAI()
        if mouseY>=200 and mouseY<=250:
            TAD()
        if mouseY>=300 and mouseY<=350:
            TRIAN()
        if mouseY>=400 and mouseY<=450:
            TRAPEZ()
        if mouseY>=500 and mouseY<=550:
            CURVA_S()
        if mouseY>=600 and mouseY<=650:
            CURVA_Z()
        if mouseY>=700 and mouseY<=750:
            TRIAN_SUAVE()
        if mouseY>=800 and mouseY<=850:
            TRAPE_SUAVE()
            
def TAI():
    global R_MIN, R_MAX
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.trapecio_abierto_der(i))
    
def TAD():
    global R_MIN, R_MAX, fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.trapecio_abierto_izq(i))
        
def TRIAN():
    global R_MIN, R_MAX, fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.triangular(i))
        
def TRAPEZ():
    global R_MIN, R_MAX, fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.trapezoidal(i))
        
def CURVA_S():
    global R_MIN, R_MAX, fuzzy 
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.curva_S(i))
     
def CURVA_Z():
    global R_MIN, R_MAX,fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.curva_Z(i))
          
def TRIAN_SUAVE():
    global R_MIN, R_MAX,fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.triangular_suave(i))
     
def TRAPE_SUAVE():
    global R_MIN, R_MAX,fuzzy
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        print(fuzzy.trapezoidal_suave(i))
    
