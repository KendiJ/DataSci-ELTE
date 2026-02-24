import matplotlib.pyplot as plt
import numpy as np
import random

x = np.linspace(0, 50, 11)
y = np.square(x)

plt.plot(x, y)
plt.xlabel('x-lable')
plt.ylabel('y-lable')
plt.show()
plt.savefig('01_img.png')

y2 = np.sqrt(x)

ax1 = plt.subplot(2, 3, 1)
plt.subplot(2, 3, 2)
ax2 = plt.subplot(2, 3, 3)
plt.subplot(2, 3, 4)
ax3 = plt.subplot(2, 3, 5)
plt.subplot(2, 3, 6)
# ax1.plot(x, y, 'r--')
ax1.plot(x, y, 'go-')
ax2.plot(x, x, 'r--')
ax3.plot(x, y, 'b*-')
plt.show()

plt.savefig('02_img.png')


y2 = np.sqrt(x)

plt.plot(x, y, 'ro-', label='square function')
plt.plot(x, x, 'g--', label='linea function')
plt.plot(x, y2, 'b:', label='root function')
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.legend()
plt.show()
plt.savefig('03_img.png')

fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)
plt.legend()
plt.show()

rnd_data =  random.sample(range(0, 1000), 100)
plt.hist(rnd_data, 5)
plt.show()



