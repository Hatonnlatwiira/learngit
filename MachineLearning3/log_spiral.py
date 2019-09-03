import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 12*np.pi, 10000)
#theta = np.arange(0, 10*np.pi, 0.02)
r = np.e ** (0.1*theta)

fig = plt.figure()
ax = plt.subplot(111, projection = 'polar')
ax.plot(theta, r, lw=1.5)
plt.show()
print(1)
