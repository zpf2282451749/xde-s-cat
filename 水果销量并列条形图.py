import matplotlib.pyplot as plt
import numpy as np
saled = [200, 250, 150, 300, 100]
saled2 = [150, 270, 130, 290, 150]
labels = ['Apple', 'Pear', 'Lemon', 'Mango', 'Cheery']
plt.figure()
index = np.arange(5)
bar_width = 0.3
plt.bar(index, saled, width=bar_width, color='r', label="June")
plt.bar(index + bar_width, saled2, width=bar_width, color='b', label="July")
plt.bar(index+0.15, 0, tick_label=labels)
plt.legend()
plt.show()
