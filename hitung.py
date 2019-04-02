x = 0
y = 0
z = 0

__author__ = "Uh She Up"
__str__ = "Ini modul perhitungan"

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