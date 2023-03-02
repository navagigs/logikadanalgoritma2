from abc import ABCMeta, abstractmethod

 # kelas abstrak
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
            pass
# kelas Segiempat turunan dari kelas DuaDimensi  
class Segiempat(DuaDimensi):
    def __init__ (self, p, l):
        self.panjang = p
        self.lebar = l
    # mengimplementasikan metode luas ()
    def luas(self):
        return self.panjang * self.lebar
# kelas Segitiga turunan dari kelas DuaDimensi  
class Segitiga(DuaDimensi):
    def __init__ (self, a, t):
        self.alas = a
        self.tinggi =t
    # mengimplementasikan metode luas ()
    def luas(self):
        return (self.alas * self.tinggi) / 2
# kelas Lingkaran turunan dari kelas DuaDimensi  
class Lingkaran (DuaDimensi):
    def __init__ (self, r):
        self.radius =r
    # mengimplementasikan metode luas () 
    def luas(self):
        import math
        return math.pi * (self.radius ** 2)


obj=DuaDimensi()
print(obj)

 
