import math
class Punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__ (self):
        return f"({self.x},{self.y})"
    
    def Seitenlaenge (self, other):
        l= ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        return l


class Figur:
    def __init__ (self,name):
        self.name=name

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name


class Kreis(Figur):
    def __init__ (self, mittelpunkt,radius):
        super().__init__("Kreis")
        self.M=mittelpunkt
        self.r=radius

    def Umfang(self):
        return 2*math.pi*self.r
    
    def __str__(self):
        return f"Kreis M={self.M} r={self.r}"


class Dreieck(Figur):
    def __init__ (self, P1, P2, P3):
        super().__init__("Dreieck")
        self.A=P1
        self.B=P2
        self.C=P3

    def Umfang(self):
        u=self.A.Seitenlaenge(self.B)+self.B.Seitenlaenge(self.C)+self.C.Seitenlaenge(self.A)
        return u
    
    def __str__(self):
        return f"Dreieck A={self.A}, B={self.B}, C={self.C}"


class Rechteck(Figur):
    def __init__(self, x, y):
        super().__init__("Rechteck")
        self.x=x
        self.y=y

    def Umfang(self):
        return self.x*2+self.y*2
    
    def __str__(self):
        return f"Rechteck (0,0) - ({self.x},{self.y})"
    

class Polygon(Figur):
    def __init__(self, list):
        super().__init__("Polygon")
        self.list=list

    def Umfang(self):
        u=0
        P1=0
        P2=0
        for i in range (len(self.list)):
            P1=self.list[i]

            if i==len(self.list)-1:
                P2=self.list[0]

            else:
                P2=self.list[i+1]

            u+=P1.Seitenlaenge(P2)

        return u
    
    def __str__ (self):
        ausgabe=[]
        for i in range (len(self.list)):
            ausgabe.append(str(self.list[i]))

        return f"Polygon {', '.join(ausgabe)}"
        

k1=Kreis(Punkt(4,5),5)
print(k1.Umfang())
print (k1)

d1=Dreieck(Punkt(5,5),Punkt(1,7),Punkt(3,2))
print(d1.Umfang())
print(d1)

r1=Rechteck(10,25)
print(r1.Umfang())
print(r1)

L=[Punkt(5,5),Punkt(1,7),Punkt(3,2), Punkt(5,6),Punkt(3,5)]
p1=Polygon(L)
print (p1.Umfang())
print(p1)