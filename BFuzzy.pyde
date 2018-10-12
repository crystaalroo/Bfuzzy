import BFuzzy
R_MIN=0
R_MAX=100
A=11.0
B=29.0
C=69.0
D=41.0
fuzzy=BFuzzy.Bfuzzy(A,B,C,D)
limpio=True
dibujar=False
lista=[[None,None]]
iter=1

def setup():
    size(1401,1500)
    drawCanvas()
    
def drawCanvas():
    fill(0,210,160)
    stroke(0,210,160)
    rect(400,0,1100,1500) #CANVAS
    stroke(0,0,0)
    rect(1100,800,220,50,20)
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
    text("Limpiar",1120,820)
    
def draw():
    global limpio,dibujar,iter,lista
    if not limpio and dibujar:
        fill(200,0,125)
        stroke(200,0,125)
        if iter!=len(lista):
            ellipse(500+(8*lista[iter][0]),500-(400*lista[iter][1]),2,2)
            print(lista[iter])
            iter+=1
        else:
            dibujar=False
            iter=1
        

def mousePressed():
    global limpio
    if mouseX>=100 and mouseX<=320 and limpio:
        limpio=False
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
        
    if mouseX>=1100 and mouseX<=1320 and mouseY>=800 and mouseY<=850:
        LIMPIAR()
            
def TAI():
    global R_MIN, R_MAX,limpio,lista,dibujar,fuzzy
    plano()
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.trapecio_abierto_izq(i)])
    limpio=False
    dibujar=True
    
    
def TAD():
    global R_MIN, R_MAX, fuzzy, limpio,lista,dibujar
    plano()
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.trapecio_abierto_der(i)])
    limpio=False
    dibujar=True
        
def TRIAN():
    global R_MIN, R_MAX, fuzzy, limpio,lista,dibujar
    plano()
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.triangular(i)])
    limpio=False
    dibujar=True
        
def TRAPEZ():
    plano()
    global R_MIN, R_MAX, fuzzy, limpio,lista,dibujar
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.trapezoidal(i)])
    limpio=False
    dibujar=True
        
def CURVA_S():
    plano()
    global R_MIN, R_MAX, fuzzy, limpio,lista,dibujar
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.curva_S(i)])
    limpio=False
    dibujar=True
     
def CURVA_Z():
    plano()
    global R_MIN, R_MAX,fuzzy, limpio,lista,dibujar
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.curva_Z(i)])
    limpio=False
    dibujar=True
          
def TRIAN_SUAVE():
    plano()
    global R_MIN, R_MAX,fuzzy, limpio,lista,dibujar
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.triangular_suave(i)])
    limpio=False
    dibujar=True
     
def TRAPE_SUAVE():
    plano()
    global R_MIN, R_MAX,fuzzy,limpio,lista,dibujar
    for i in range(R_MIN,R_MAX+1):
        i=float(i)
        lista.append([i,fuzzy.trapezoidal_suave(i)])
    limpio=False
    dibujar=True
    
def LIMPIAR():
    global A,B,C,D,limpio
    A=random(100)
    B=random(100)
    C=random(100)
    D=random(100)
    fuzzy.set_valores(A,B,C,D)
    drawCanvas()
    limpio=True
    
def plano():
    global lista,A,B,C,D
    lista=[[None,None]]
    f=createFont("AmericanTypewriter",10)
    textFont(f)
    line(500,500,1300,500)
    line(500,500,500,100)
    for i in range(0,21):
        text(str(i*5),500+(40*i),520)
    for i in range(0,21):
        text(str(i*.05),480,500-(20*i))
    fill(255,0,0)
    stroke(255,0,0)
    text("A",500+(8*A),540)
    text("B",500+(8*B),540)
    text("C",500+(8*C),540)
    text("D",500+(8*D),540)
