"""
Lab 15 - Plot a Math Formula
Author: Hibo Jama
Purpose: This program plots a sine wave using matplotlib and saves it as an image.
Starter Code: None
Date: 05/2026
"""

import matplotlib.pyplot as plt
import math

# create data
x_values = []
y_values = []

for i in range(0, 360):
    radians = math.radians(i)
    x_values.append(i)
    y_values.append(math.sin(radians))

plt.plot(x_values, y_values)

plt.title("Sine Wave")
plt.xlabel("Degrees")
plt.ylabel("Sin Value")

plt.grid()

plt.savefig("sine_wave.png")

plt.show()