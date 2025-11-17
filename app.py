import matplotlib.pyplot as plt
import numpy as np

year = list(range(1950, 2101))
population = np.linspace(2.538, 10.85, len(year))

# Adding more data
year = [1800, 1850, 1900] + year
population = [1.0, 1.262, 1.650] + list(population)

plt.plot(year, population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()
