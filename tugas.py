pesan = "Python Programming"
def cetak():
    print(pesan)
    print(pesan)
    print(pesan)
    print(pesan)
    print(pesan)

x = 0
y = 0
z = 0

def tambah(x,y):
    z = x + y
    return z

def kurang(x,y):
    z = x - y
    return z

def kali(x,y):
    z = x * y
    return z

def bagi(x,y):
    try:
        z = x / float(y)
    except:
        z = None
    return z

print(tambah(1,2))