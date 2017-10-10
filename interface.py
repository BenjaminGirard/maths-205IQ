#!/usr/bin/env python3.3
## interface.py for  in /home/tetard/EPITECH_Y2/maths/205IQ/bonus
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Thu Apr 20 11:53:24 2017 benjamin girard
## Last update Thu Apr 20 11:58:34 2017 benjamin girard
##

import plotly
from plotly.graph_objs import *

def interface(distrib):
    distrib = Scatter(
        x=[i for i in range(0, 201)],
        y=distrib,
        name="Distribution"
    )
    data = Data([distrib])
    plotly.offline.plot(
        data,
        filename='Distribution'
    )
