"""# SpiralData"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class SpiralData():

  def __init__(self, coordinates):
    if not (type(coordinates) is list or type(coordinates) is range):
      raise Exception("The parameter for SpiralData needs be a list of coordinates")
    if (len(coordinates) < 2):
      raise Exception("Too few coordinates to plot")

    self.x = []
    self.y = []
    
    for coord in coordinates:
      self.x.append(coord[0])
      self.y.append(coord[1])

    if (len(self.x) != len(self.y)):
      raise Exception("for every x in the input there must be a y")
  
  def coordinates(self):
    coordinates = []
    for i in range(len(self.x)):
      coordinates.append( [self.x[i], self.y[i]] )
    return coordinates

  def show(self, laps = 3):
    x_max = max(self.x)
    x_min = min(self.x)
    y_max = max(self.y)
    y_min = min(self.y)
    coordinates = self.coordinates()

    theta = []
    thetaMax = 2 * np.pi * laps
    
    r = []
    colors = []
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    for coord in coordinates:
      x = coord[0]
      y = coord[1]
      
      thetaEl = thetaMax * ((x - x_min)/(x_max - x_min))
      theta.append(thetaEl)

      rEl = (thetaEl / thetaMax)
      r.append(rEl)

      R = hex(int(255 * ((y - y_min) / (y_max - y_min)))).replace("0x", "")
      B = hex(int(255 - int(R, 16))).replace("0x", "")

      if (len(R) < 2):
        R = "0" + R
      if (len(B) < 2):
        B = "0" + B
      colorRGB = '#' + R + "00" + B
      colors.append(colorRGB) 
    
    ax.scatter(theta, r, c=colors, zorder=2, cmap='hsv')
    ax.plot(theta, r, 'k-', zorder=1)
    ax.grid(True)
    plt.show()

"""# Test SpiralData"""

Dat = open('aerogerador.dat', 'r')
coord = []
for line in Dat.readlines():
  arr = line.split("\t")
  arr.remove("\n")
  for i in range(len(arr)):
    arr[i] = float(arr[i])
  coord.append(arr)

chart = SpiralData(coord)
chart.show()
