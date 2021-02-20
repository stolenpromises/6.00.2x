# -*- coding: utf-8 -*-
"""
Scratch code used while reviewing plotting throughout lecture 4.

Created on Sat Feb 20 08:12:16 2021

@author: nathan.m
"""

# pylab
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

# append numeric values to the above lists
for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

# plotting overlay - no frame change specified, all will populate same figure
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# plotting individual figures in their own frames with automatic scale
plt.figure('lin')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.plot(mySamples, myExponential)

# plotting figures with titles
plt.figure('lin')  # making the frame active
plt.plot(mySamples, myLinear)  # plotting the figure

plt.figure('lin')  # making the frame active
plt.title('Linear')  # invoking labeling for the active figure


# adding axis titles
plt.figure('lin')  # set the active frame
plt.xlabel('sample points')  # set an x label
plt.ylabel('linear function')  # set a y label
plt.plot(mySamples, myLinear)  # envoke the plot


# clearing previous frame display settings to avoid labels on unrelated plots
plt.figure('lin')  # set the active figure
plt.clf()  # clear the active figure
plt.plot(mySamples, myLinear)  # plot to the active figure

plt.figure('lin')  # set the active frame
plt.title('Linear')  # set a title for the figure
plt.figure('quad')  # set the active frame
plt.title('Quadratic')  # set a title for the figure

# set explicit limits to axis plot scale in order to compare two plots
plt.figure('lin')  # set the active frame
plt.clf()  # clear it of any previous settings
plt.ylim(0, 1000)  # set the scale of the y axis
plt.plot(mySamples, myLinear)  # envoke plotting

plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')

# comparing two overlayed plots, each at automatic scale
plt.figure('lin quad')  # set the active frame for first plot
plt.clf()  # clear it of any previous settings
plt.plot(mySamples, myLinear)  # plot first line
plt.plot(mySamples, myQuadratic)  # plot second line
plt.figure('cube exp')  # set the active frame for second plot
plt.clf()
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.figure('lin quad')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.title('Cubic vs. Exponential')

# adding a legend that identifies a plot comparison
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, label='linear')  # pass a label as a parameter
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.legend(loc='upper left')  # set a location for a legend
plt.title('Linear vs. Quadratic')  # set a title in the location
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()  # let pylab place the legend location automatically
plt.title('Cubic vs. Exponential')
