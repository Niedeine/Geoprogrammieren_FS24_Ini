class Vector3: 
    def __init__(self,x=0,y=0, z=0):
        self.x=x
        self.y=y
        self.z=z

#Konversion zur Zeichenkette:
    def __str__ (self):
        return f"{self.x}, {self.y}, {self.z}"

#Addition:    
    def __add__ (self, other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x+other, self.y+other, self.z+other)
        else:
            return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)
        
    def __radd__ (self, other):
        return Vector3(self.x+other, self.y+other, self.z+other)        

#Substraktion:    
    def __sub__ (self, other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x-other, self.y-other, self.z-other)
        else:
            return Vector3(self.x-other.x, self.y-other.y, self.y-other.y)
        
    def __rsub__ (self, other):
        return Vector3(self.x-other, self.y-other, self.z-other)

#Komponentenweise Multipikation:
    def __mul__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x*other, self.y*other, self.z*other)
        else:
            return Vector3(self.x*other.x, self.y*other.y, self.z*other.z)

    def __rmul__ (self,other):
        return Vector3(self.x*other, self.y*other, self.z*other)
    
#Kreuzprodukt:
    def cross (self,other):
        newx=self.y*other.z-self.z*other.y
        newy=self.z*other.x-self.x*other.z
        newz=self.x*other.y-self.y*other.x
        return Vector3(newx,newy,newz)
    
#Skalarprodukt:
    def dot(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    
#Normalisierung:
    def normalize(self):
        v=(self.x**2+self.y**2+self.z**2)**0.5
        return (1/v)*self
    
#Länge:
    def len(self):
        return (self.x**2+self.y**2+self.z**2)**0.5


#Tests
a=Vector3 (3,4,2)
b=Vector3(2,1,0)
#Multiprikation test:
c=a*b
print(c)
#Skalarprodukt test:
d=a.dot(b)
print(d)
#Kreuzprodukt test:
e=a.cross(b)
print(e)
#Normierung test:
f=Vector3(3,4,0)
g=f.normalize()
print(g)
print(g.len())         