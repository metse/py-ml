import numpy as np
import matplotlib.pyplot as plt

#creating fictitious data
mileage = np.random.randint(100, size=10)
time = np.random.randint(100, size=10)

#using Numpy's mean and median methods
mileage_mean = np.mean(mileage)
mileage_median = np.median(mileage)

#plt.hist(mileage)
#plt.clf()

#scatter plot
plt.scatter(time, mileage)

#labels
plt.xlabel("Over Time")
plt.ylabel("Mileage")

#grid
plt.grid()

plt.show()
