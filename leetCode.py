Mencari bilangan terbesar dalam sebuah integer
N = int(input())
hasil2 = 0
while N > 0:
    hasil = N%10
    if hasil > hasil2:
        hasil2 = hasil
    N = N//10
 print(hasil2)