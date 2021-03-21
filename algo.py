#soal no 1
name = 'Dimas Prasetyo'
nim = '202410102083'

kalimat = 'sebuah tipe data yang memuat tentang huruf'
vokal={"a":0,"i":0,"u":0,"e":0,"o":0}

def hvokal(string):
    for i in string:
        if i=="a":
            vokal["a"]+=1
        elif i=="i":
            vokal["i"]+=1
        elif i=="u":
            vokal["u"]+=1
        elif i=="e":
            vokal["e"]+=1
        elif i=="o":
            vokal["o"]+=1
        else:
            continue
    return vokal

print(hvokal(kalimat))

#Soal 2

nama = 'Dimas Prasetyo'
a= 6
kalimat = 'sebuah tipe data yang memuat tentang huruf'
nim = '202410102083'
def hitung(kode,nim):
    return kode-(nim*((a)//2))
print(hitung(ord(max(kalimat)),int(nim[10:])))

#Soal 3 dan 4 maksimal huruf kapital 3
import random as rand
a=""
kalimat = 'sebuah tipe data yang memuat tentang huruf'
nomor = rand.randint(10,20)
for i in range(nomor) :
    a+= rand.choice(kalimat)

print (a)
print(a.capitalize())

#soal 5
name = 'Dimas Prasetyo'
nim = '202410102083'
li = name.replace(" ","")+nim
vokallist = ["a","i","u","e"]
for i in li :
    if i in vokallist :
        li = li.replace(i,"o")
print(li)