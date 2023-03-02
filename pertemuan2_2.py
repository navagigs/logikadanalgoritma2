# membuat kelas turunan dari kelas list
class StringList (list):
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    # override metode append()
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError('Objek harus bertipe string')
        self.data.append(objek)

    # override metode insert()
    def insert(self, indeks, objek):
        if indeks >= len(self.data) or \
                indeks < -len(self.data):
            raise IndexError('Indeks di luar rentang')
        if not isinstance(objek, str):
            # override metode append()
            raise TypeError('Objek harus bertipe string')
        self.data.insert(indeks, objek)


# membuat objek dari kelas StringList
slist = StringList()
# menambah data menggunakan metode append()
slist.append('Python')
slist.append('Ruby')
slist.append('PHP')
# print(slist)
#  output ['Python', 'Ruby', 'PHP']

# menambah data menggunakan metode insert()
slist.insert(2, 'Perl')
# print(slist)
#  output ['Python', 'Ruby', 'Perl', 'PHP']

slist.insert(-3, 'Java')
# print(slist)
#  output ['Python', 'Java', 'Ruby', 'Perl', 'PHP']


slist.insert(-6, 'JavaScript')
print(slist)
Traceback(most recent call last):
  File "c:\Users\navagia\Documents\python\2_pbo4_pewarisan.py", line 45, in <module >
  slist.insert(-6, 'JavaScript')
  File "c:\Users\navagia\Documents\python\2_pbo4_pewarisan.py", line 19, in insert
  raise IndexError('Indeks di luar rentang')
IndexError: Indeks di luar rentang
