
"""
JUPYTER NOTEBOOKS

Link to Documentation:

https://docs.jupyter.org/en/latest/

#####Setup
terminal: "jupyter notebook"

1) %matplotlib inline
2) import matplotlib.pyplot as plt
5) plt.figure()

****label plots
1) plt.figure()
plt.plot(x, y)
plt.title('my title')
plt.xlabel('x vals')
plt.ylabel(same as abnove)
legend
plt.legend()
plt.show()

*****Make plot (see JN file):

type import numpy as np
import matplotlib as plt
run= triangle or use shift+enter
kernel: circle dark when running, white when done running code
run code asssigning variables before plotting
for plot(x, y), xlable('string'), title('string') using single qupotes

*****Types of plots

plt.plot = line plot
plt.scatter scatter plot
plt.bar bar graph

plt.plot(x, y, color='red' or color=(RGB value)) red will give u color
plt.plot(x, y, linewidth = '2.5') thickness
plt.plot(x, y, marker='*') makes marker star shaped, points
plt.plot(x, y, 'r*')short hand, color and marker (red)
plt.plot(x, y, alpha=.5)opaque

plt.figure(figsize=(12, 8)) specifies size of graph
plt.plot(x, y)
plt.errorbar(x, y, yerr=y_error, fmt='o') displays error bar

Colors:
https://matplotlib.org/stable/users/explain/colors/colors.html

Markers: search up

SUBPLOTS
multiple stuff in one graph, use subplots
compare all data
******init:
axs is individual piece
fig, axs = plt.subplots(2) could also write:
fig, (ax1, ax2) = plt.subplots(2) where fig = name of plot
ax1 ax2 is 1 by 2 array of plots (2 elements)
ax3 ax4 would give u 12 plots, must put 12 in parense

#title figure
fig.suptitle('vertically stacled subplots')

##plot first
axs[0].plot(x, y)

##plot second with different input
axs[1].plot(x, -y)




"""