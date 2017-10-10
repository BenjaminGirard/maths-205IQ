#!/usr/bin/env python3.3
## calc.py for  in /home/tetard/EPITECH_Y2/maths/205IQ
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Tue Apr 11 14:28:10 2017 benjamin girard
## Last update Tue Apr 11 14:58:04 2017 benjamin girard
##

import math


def nl(av, stdev, x):
    tmp1 = (1.0 / ((stdev) * math.sqrt(2 * math.pi)))
    tmp2 = math.exp(((-1) / 2) * (((x - av) / stdev) ** 2))
    return  (tmp1 * tmp2) * 100

def sum1(n, mini, maxi, av, stdev):
    h = (maxi - mini) / n
    res = 0.0
    for i in range(1, n):
        res += nl(av, stdev, mini + (i * h))
    return res


def sum2(n, mini, maxi, av, stdev):
    h = (maxi - mini) / n
    res = 0.0
    for i in range(0, n):
        res += nl(av, stdev, mini + (i * h) + (h / 2))
    return res


def simpson(mini, maxi, n, av, stdev):
    tmp1 = ((maxi - mini) / (6 * n))
    tmp2 = (nl(av, stdev, mini) + nl(av, stdev, maxi) + (2 * sum1(maxi * 10, mini, maxi, av, stdev)))
    tmp3 = 4 * sum2(maxi * 10, mini, maxi, av, stdev)
    return (tmp1 * (tmp2 + tmp3))
