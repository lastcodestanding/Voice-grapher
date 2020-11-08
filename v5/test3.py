import matplotlib.pyplot as plt
import numpy as np
import operator
x = np.arange(-0,10,0.01)
plt.plot(x,operator.pow(x,2))
plt.show()
