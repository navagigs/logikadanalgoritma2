from abc import ABCMeta, abstractmethod 

    # kelas abstrak
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

# kelas Segiempat turunan dari kelas Dua Dimensi 
class Segiempat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    # mengimplementasikan metode luas ()
    def luas(self):
        return self.panjang * self.lebar

# kelas Segitiga turunan dari kelas DuaDimensi 
class Segitiga(DuaDimensi):
    def __init__ (self, a, t):
        self.alas = a
        self.tinggi = t
        #mengimplementasikan metode luas ()
    def luas (self):
        return (self.alas * self.tinggi) / 2

# kelas Lingkaran turunan dari kelas DuaDimensi 
class Lingkaran(DuaDimensi):
    def __init__ (self, r):
        self.radius = r
        # mengimplementasikan metode luas ()
    def luas(self):
        import math
        return math.pi* (self.radius ** 2)

# membuat list kosong
mylist = []
print(mylist)

# menambahkan objek Segiempat ke dalam mylist 
mylist.append(Segiempat(10, 8))
print(mylist)

# menambahkan objek Segitiga ke dalam mylist 
mylist.append(Segitiga(3, 5))
print(mylist)

# menambahkan objek Lingkaran ke dalam mylist 
mylist.append(Lingkaran(4))
print(mylist)

# menelusuri seluruh elemen mylist, 
# kemudian memanggil metode luas () 
# dari setiap objek yang ditelusuri 
for obj in mylist:
    if not issubclass (obj.__class__, DuaDimensi):
        raise TypeError('Objek harus turunan dari Dua Dimensi')
    if isinstance (obj, Segiempat):
        print ('Luas segiempat = ', end='')
    elif isinstance (obj, Segitiga):
        print ('Luas segiempat = ', end='')
    else: 
        print ('Luas lingkaran = ', end='')
    print(obj.luas())