#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:45:30 2021

@author: JeffersonGao
"""

import streamlit as st
import pandas as pd

RR = pd.read_excel(open('PAC_v1.3.4.xlsm', 'rb'), sheet_name='RR') 

TICKERS = RR['TICKER'].unique()

SLICE = RR[RR['TICKER'] == TICKERS[11]]


# plotting - dual axis

from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add LHS traces
element = 'LOWER'
name = element + ' (LHS)'
fig.add_trace(
    go.Scatter(x=SLICE['DATE'], y=SLICE[element], name=name),
    secondary_y=False
)
element = 'UPPER'
name = element + ' (LHS)'
fig.add_trace(
    go.Scatter(x=SLICE['DATE'], y=SLICE[element], name=name),
    secondary_y=False
)
element = 'MIDPOINT'
name = element + ' (LHS)'
fig.add_trace(
    go.Scatter(x=SLICE['DATE'], y=SLICE[element], name=name),
    secondary_y=False
)
element = 'SPOT'
name = element + ' (LHS)'
fig.add_trace(
    go.Scatter(x=SLICE['DATE'], y=SLICE[element], name=name),
    secondary_y=False
)

# Add RHS traces
element = 'CHANNEL_WIDTH'
name = element + ' (RHS)'
fig.add_trace(
    go.Scatter(x=SLICE['DATE'], y=SLICE[element], name=name),
    secondary_y=True
)

# Add figure title
fig.update_layout(
    title_text= "Ticker: " + TICKERS[11]
)

# Set x-axis title
fig.update_xaxes(title_text="Period")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Price</b> levels", secondary_y=False)
fig.update_yaxes(title_text="<b>Channel</b> width", secondary_y=True)

plot(fig)