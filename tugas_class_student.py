# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 9:20:42 2021

@author: Winda Pratiwi

A class representing a student

"""

class student:

def __init__ (self,n,i,p,s,k,d):
    self.full_name = n
    self.nim = i
    self.prodi = p
    self.fakultas = s
    self.kampus = k
    self.domisili = d
    
def get_name (self):
    return self.full_name
def get_nim (self):
    return self.nim
def get_prodi (self):
    return self.prodi
def get_fakultas (self):
    return self.fakultas
def get_kampus (self):
    return self.kampus
def get_domisili (self):
    return self.domisili

f = student ("Winda Pratiwi", 1905910, "Sistem Telekomunikasi", "Kamda Purwakarta", "UPI", "Bandung")

print ("Nama lengkap: ", f.full_name)
print ("NIM: ", f.get_nim ())
print ("PRODI: ", f.get_prodi ())
print ("Fakultas: ", f.get_fakultas ())
print ("Kampus: ", f.get_kampus ())
print ("Domisili: ", f.get_domisili ())