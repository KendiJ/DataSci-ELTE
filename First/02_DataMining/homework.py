## draw a plot with two line that have sin, cos from [0, 2] pi range with different colors
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 5))

plt.plot(x, y_sin, label='Sin', color='blue', linewidth=2)

plt.plot(x, y_cos, label='Cos', color='red', linestyle='--', linewidth=2)

plt.title('Sin and Coz Waves (0 to 2$\pi$)')
plt.xlabel('Angel (radians)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()