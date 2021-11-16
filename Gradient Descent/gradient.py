import numpy as np
import math as m
import array

def f(x,y):
    return  8*x*x + 12*y*y - 12*x*y - 8*x - 10*y + 36

def fpx(x,y):
    return 16*x - 12*y - 8

def fpy(x,y):
    return 24*y - 12*x - 10

def GD(nheta=0.002, x0=2, y0=2, n=5):
    dhx = 1000
    dhy = 1000
    x1 = 0
    y1 = 0
    i = 0
    while i < n:
        print("\n",i, x0, y0)
        dhx = fpx(x0,y0)
        dhy = fpy(x0,y0)
        x1 = x0 - nheta * dhx
        y1 = y0 - nheta * dhy
        i += 1
        x0 = x1
        y0 = y1
    return x0, y0, f(x0,y0)

if __name__== '__main__':
    x0, y0, f_optimal = GD()
    print("gia tri cuc tieu cua ham la: ", f_optimal, "\ntai diem: ", x0, y0)