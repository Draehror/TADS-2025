from matplotlib import pyplot as plt

days = ["2025-01-04", "2025-01-05", "2025-01-06", "2025-01-07", "2025-01-08"]

prices = [729.77, 735.11, 755.98, 816.04, 880.02]

plt.plot(days, prices)

plt.title("NASDAQ: TSLA")

plt.xlabel("Date")
plt.ylabel("USD")

plt.show()
