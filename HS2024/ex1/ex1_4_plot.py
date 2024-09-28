import matplotlib.pyplot as plt

months = [1, 2, 3]
games = [4770357, 5015361, 5801234]

plt.bar(months, games)
plt.xlabel('Month')
plt.ylabel('Number of games')
plt.title('Number of games played in each month')
plt.show()

