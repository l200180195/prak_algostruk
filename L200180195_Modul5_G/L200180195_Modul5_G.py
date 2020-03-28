class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Tinggal di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Tiap Bulannya."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
Mahasiswa = [MhsTIF('Zozo', "A198", 'Jakarta', 450000),
          MhsTIF('Yoyo', "A108", 'Medan', 3000000),
          MhsTIF('Xoxo', "A234", 'Pontianak', 870000),
          MhsTIF('Wowo', "A007", 'Blora', 550000),
          MhsTIF('Vovo', "A132", 'Denpasar', 2000000),
          MhsTIF('Uouo', "A122", 'Sabang', 1500000),
          MhsTIF('Toto', "A195", 'Merauke', 765000),
          MhsTIF('Soso', "A143", 'Jogjakarta', 900000),
          MhsTIF('Roro', "A200", 'Lombok', 675000),
          MhsTIF('Mai', "A077", 'Kutai', 999000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)

#Nomer2
daftar1 = [2,4,6]
daftar2 = [1,3,5,7]

def combine(A, B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j < lb:
        c.append(B[j])
        j += 1
    return c

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
#Nomor3
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));
