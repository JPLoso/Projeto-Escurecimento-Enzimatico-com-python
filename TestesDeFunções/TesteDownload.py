import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

print( cv.__version__ )
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()