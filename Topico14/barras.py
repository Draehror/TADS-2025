import matplotlib.pyplot as plt

regions = ['New England', 'Mid-Atlantic', 'Midwest']

sales = [882703, 532648, 714406]

plt.bar(regions, sales, color=['blue', 'orange', 'green'])

plt.xlabel('Regions')
plt.ylabel('Sales')

plt.title('Sales by Region')

plt.show()