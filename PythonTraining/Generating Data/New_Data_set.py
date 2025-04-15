# A dataset can be a small list of numbers that fits in a single line of code,
# We’ll also use a package called Plotly, which creates visualizations that work well on digital devices, to analyze the results of rolling dice.

# Lets Plot a Simple Graph
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]


fix, ax = plt.subplots()
ax.plot(squares)

plt.show()
