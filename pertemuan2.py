# Mendefinisikan kelas
class PersegiPanjang:
    # attribut statis
    counter = 0

    def __init__(self, p, l):
        # menaikan nilai attribut statis
        PersegiPanjang.counter += 1
        # atribut-atribut non-statis
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


# Membuat tiga objek dari kelas PersegiPanjang
obj1 = PersegiPanjang(20, 15)
obj2 = PersegiPanjang(10, 8)
obj3 = PersegiPanjang(7, 5)
# memanggil atribut counter melalui kealas
# print(PersegiPanjang.counter)
# # output 3

# print(obj1.counter)
# # output 3

# print(obj2.counter)
# # output 3

# print(obj3.counter)
# output 3

# Membuat objek baru dari kelas PersegiPanjang
obj4 = PersegiPanjang(12, 9)
print(PersegiPanjang.counter)
# output 4
print(obj1.counter, obj2.counter, obj3.counter, obj4.counter)
# output 4 4 4 4
