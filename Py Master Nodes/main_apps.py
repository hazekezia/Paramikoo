import paramiko
import os
from manualcall import manualcall
from allcall import allcall

ip_list = ["192.168.43.234","192.168.43.153","192.168.43.247","192.168.43.249"]

os.system("title Main Menu")

def confirm():
    print("Exit? (y/n)", end=" ")
    y = str(input())
    if (y=="y" or y=="Y" or y=="yes"):
        print()
    elif (y=="n" or y=="N" or y=="no"):
        menu()
        
def menu():
    os.system('cls')
    
    #Menu
    print("MENU APPS (Menghitung Luas & Keliling Segitiga, Lingkaran, dan Persegi)")
    
    #Print list ip dan mesin
    x=0;
    for ipaddr in ip_list:
        x=x+1
        print("Mesin", x,":", ipaddr)
        
    print("\n1. Pilih Manual 2. Ambil Semua")
    x = str(input("Pilihan : "))
    if (x=="1"):
        manualcall()
    elif (x=="2"):
        allcall()
    else:
        print("Tidak tersedia. Silahkan ulangi kembali.")
    
    confirm()

menu()