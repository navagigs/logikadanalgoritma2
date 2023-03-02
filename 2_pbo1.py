# Mendefinisikan kelas
class PersegiPanjang:

    def __init__(self, p, l):
        # mendefinisikan atribut-atribut kelas
        self.panjang = p
        self.lebar = l

    def ubahPanjang(self, p):
        self.panjang = p

    def ubahLebar(self, l):
        self.lebar = l

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print('Luas persegi panjang = %.2f' % self.hitungLuas())

    def cetakkeliling(self):
        print('Keliling persegi panjang=% .2f' % self.hitungKeliling())


# Membuat objek dari kelas PersegiPanjang
obj1 = PersegiPanjang(10, 8)
# memanggil objek dari kelas PersegiPanjang
obj1.cetakLuas()
print(obj1)

# memanggil objek dari kelas PersegiPanjang
obj1.cetakkeliling()
print(obj1)

# Output Luas persegi panjang = 80.00
# Output Keliling persegi panjang= 36.00


# Membuat objek dari kelas PersegiPanjang
obj2 = PersegiPanjang(8, 6)
# memanggil objek dari kelas PersegiPanjang
obj2.cetakLuas()
print(obj2)

# memanggil objek dari kelas PersegiPanjang
obj2.cetakkeliling()
print(obj2)

# Output Luas persegi panjang = 48.00
# Output Keliling persegi panjang= 28.00
