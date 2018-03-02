
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random as rn

#------------------------------------------------------------------------------

size = 12
rn.seed(4321)
no_colors = 6

#------------------------------------------------------------------------------

# Build matrix
board = np.zeros((size, size))
for i in range(0, size):
    for j in range(0, size):
        board[i, j] = rn.randint(1, no_colors)

#------------------------------------------------------------------------------
    
navy   = [0  , 0  , 128]; navy_norm   = [x/255 for x in navy]
blue   = [30 , 144, 255]; blue_norm   = [x/255 for x in blue]
green  = [ 0 , 128,   0]; green_norm  = [x/255 for x in green]
red    = [255,  10,  10]; red_norm    = [x/255 for x in red]
orange = [255, 140,   0]; orange_norm = [x/255 for x in orange]
yellow = [255, 255,   0]; yellow_norm = [x/255 for x in yellow]

colors = [navy_norm, 
          blue_norm, 
          green_norm, 
          red_norm, 
          orange_norm, 
          yellow_norm]

color_map = cm.jet.from_list('game_colors', colors, N=no_colors)

#------------------------------------------------------------------------------

fig, ax = plt.subplots(1) # Create Figure and Axes instances
ax.matshow(board, cmap=color_map) # Display matrix in figure window
ax.set_yticklabels([]) # Turn off tick labels
ax.set_xticklabels([])
plt.show()
