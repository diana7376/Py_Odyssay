import random
# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list=[]
for n in range(1,11):
    list.append(n)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for n in list:

    if n%2==0:
        print(n)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i=1
while i<=5:
    print(i)
    i+=1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
dict={'name':'Diana',
      'age':'10',
      'city':'Chisinau'}
for key, value in dict.items():
    print(key,value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(f"{row}:")
    for i in row:
        print(i)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
secv = range(1,20,3)
for n in secv:
    print(n)
# CODUL TĂU VINE MAI SUS:1

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for i,num in enumerate(secv):
    print(f'index:{i} numar:{num}')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
secv2 = range(1,14,2)
for secv,secv2 in zip(secv,secv2):
    print(f'{secv}-{secv2}')
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
for n in range(1,11):
    print(n)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
i=1
while i<=70:
    print(i)
    i*=2
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
list=[]
for i in range(1,20):
    i**=2
    if i<=100:
        list.append(i)

print(list)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    print(i*7)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
list=[]
for i in range(1,6):
    sublist=[(i,j) for j in range(1,6)]
    list.append(sublist)
    
print(list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
result=[]
for sublist in list:
    for (i,j) in sublist:
        if i<j:
            result.append((i,j))

print(result)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
numere=[]
for i in range(0,5):
    n= random.randint(0,20)
    numere.append(n)
print(numere)

gasit=False

i=0
while i<len(numere) and not gasit:
    if numere[i]>10:
        gasit=True
        val=numere[i]
    i+=1

if gasit:
    print(f'prima valoare gasita mai mare ga 10 este {val}')
else:
    print( "Nu există valori mai mari decât 10")
        
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dimensiune=int(input('introduceti dimensiunea patratului: '))
for i in  range(dimensiune):
    print('*'*dimensiune)
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
i=1
while i<=6:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1

# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
str='54321'
for i in range(len(str)):
    print(str)
    str=str[:-1]
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
str='abcdefg'
for i in range(len(str)):
    print(str)
    str=str[1:]
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(0,6):
    if i%2==0:
        print('+',end='')
    else:
        print('-',end='')
    for j in range(1,16):
        if j % 2 == 0:
            print('+', end='')
        else:
            print('-', end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
n=1
str=[]
while n<=5:
    a=3**n
    str.append(a)
    print(*str)
    n+=1
for i in range(len(str)):
    str=str[1:]
    print(*str)
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.