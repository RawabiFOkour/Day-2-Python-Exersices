#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:24:00 2019

@author: rawabe
"""

coin=("Bitcoin","Ether","Ripple","Litecoin")
code=("BTC","ETH","XRP","LTC")

d=dict(zip(coin,code))
print(d)


"""
output


{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

"""