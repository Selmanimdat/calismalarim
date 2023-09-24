# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:14:01 2023

@author: Selman
"""

import pyautogui

# Fare konumunu alın
x, y = pyautogui.position()

# Koordinatları yazdırın
print(f"Fare Konumu: X = {x}, Y = {y}")
