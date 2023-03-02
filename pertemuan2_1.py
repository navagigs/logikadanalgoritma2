class Aritmetika:
    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b

    @staticmethod
    def kali(a, b):
        return a * b

    @staticmethod
    def bagi(a, b):
        return a / b

    @staticmethod
    def bagi_int(a, b):
        return a // b

    @staticmethod
    def sisabagi(a, b):
        return a % b

    @staticmethod
    def pangkat(a, b):
        return a ** b


print(Aritmetika.kali(10, 3))
# # output 13

# print(Aritmetika.kurang(10, 3))
# # output 7

# print(Aritmetika.kali(10, 3))
# # output 30

# print(Aritmetika.bagi_int(10, 3))
# # output 3

# print(Aritmetika.sisabagi(10, 3))
# # output 1

# print(Aritmetika.pangkat(10, 3))
# # output 1000

# membuat objek dari kelas Artimatika
obj = Aritmetika()
print(obj.tambah(10, 3))
# output 13
print(obj.pangkat(10, 3))
# output 1000
