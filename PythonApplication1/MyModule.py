from math import *
from random import *
from re import T

import string

login=[]
password=[]
def salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    return sala