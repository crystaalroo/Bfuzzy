import math
class Bfuzzy:
    def __init__(self,a,b,c=1.0,d=1.0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d


    def trapecio_abierto_der(self,u):
        l=[self.a,self.b]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        if self.a==self.b: return -1
        if u>self.b: return 1.0
        if u<self.a: return 0.0
        if self.a<=u and u<=self.b: return (u-self.a)/(self.b-self.a)

    def trapecio_abierto_izq(self,u):
        l=[self.a,self.b]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        if self.a==self.b: return -1
        if u>self.b: return 0.0
        if u<self.a: return 1.0
        if self.a<=u and u<=self.b: return (self.b-u)/(self.b-self.a)

    def triangular(self,u):
        l=[self.a,self.b,self.c]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        self.c=l[2]
        if self.a==self.b: return -1
        if self.c==self.d: return -1
        if u<self.a or u>self.c: return 0.0
        if self.a<=u and u<self.b: return (u-self.a)/(self.b-self.a)
        if self.b<=u and u<=self.c: return (self.c-u)/(self.c-self.b)

    def trapezoidal(self,u):
        l=[self.a,self.b,self.c,self.d]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        self.c=l[2]
        self.d=l[3]
        if self.a==self.b:return -1
        if self.d==self.c: return -1
        if u<self.a or u>self.d: return 0.0
        if self.b<=u and u<=self.c: return 1.0
        if self.a<=u and u<self.b: return (u-self.a)/(self.b-self.a)
        if self.c<u and u<=self.d: return (self.d-u)/(self.d-self.c)

    def curva_S(self,u):
        l=[self.a,self.b]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        if u>self.b: return 1.0
        if u<self.a: return 0.0
        if self.a<=u and u<=self.b: return (1+math.cos(((u-self.b)/(self.b-self.a))*math.pi))/2.0

    def curva_Z(self,u):
        l=[self.a,self.b]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        if u>self.b: return 0.0
        if u<self.a: return 1.0
        if self.a<=u and u<=self.b: return (1+math.cos(((u-self.a)/(self.b-self.a))*math.pi))/2.0

    def triangular_suave(self,u):
        l=[self.a,self.b,self.c]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        self.c=l[2]
        if u<self.a or u>self.c: return 0.0
        if self.a<=u and u<self.b: return (1+math.cos(((u-self.b)/(self.b-self.a))*math.pi))/2.0
        if self.b<=u and u<=self.c: return (1+math.cos(((self.b-u)/(self.c-self.b))*math.pi))/2.0

    def trapezoidal_suave(self,u):
        l=[self.a,self.b,self.c,self.d]
        l.sort()
        self.a=l[0]
        self.b=l[1]
        self.c=l[2]
        self.d=l[3]
        if u<self.a or u>self.d: return 0.0
        if self.b<=u and u<=self.c: return 1.0
        if self.a<=u and u<self.b: return (1+math.cos(((u-self.b)/(self.b-self.a))*math.pi))/2.0
        if self.c<u and u<=self.d: return (1+math.cos(((self.c-u)/(self.d-self.c))*math.pi))/2.0

    def min(self,a,b):
        if a>b: return b
        return a

    def max(self,a,b):
        if a>b: return a
        return b

    def AND(self,a,b):
        return self.min(a,b)

    def OR(self,a,b):
        return self.max(a,b)

    def NOT(self,a):
        return 1.0-a

    def implicaZadeh(self,a,b):
        return max(self.NOT(a),self.min(a,b))

    def implicaMamdani(self,a,b):
        return self.min(a,b)

    def implicaGodel(self,a,b):
        if a<=b: return 1.0
        return b
    
    def set_valores(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
