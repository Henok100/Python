import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a boxplot
fig, ax = plt.subplots()
ax.boxplot(data)

# Overlay the summary statistics on the boxplot
for i, d in enumerate(data):
    pos = [i+1]*5
    stats = [np.min(d), np.percentile(d, 25), np.median(d), np.percentile(d, 75), np.max(d)]
    ax.text(pos[2], stats[0]-0.05*(stats[4]-stats[0]), f'{stats[0]:.2f}', ha='center', va='top')
    ax.text(pos[2], stats[1]-0.05*(stats[4]-stats[0]), f'{stats[1]:.2f}', ha='center', va='top')
    ax.text(pos[2], stats[2]+0.05*(stats[4]-stats[0]), f'{stats[2]:.2f}', ha='center', va='bottom')
    ax.text(pos[2], stats[3]+0.05*(stats[4]-stats[0]), f'{stats[3]:.2f}', ha='center', va='bottom')
    ax.text(pos[2], stats[4]+0.05*(stats[4]-stats[0]), f'{stats[4]:.2f}', ha='center', va='bottom')

# Show the plot
plt.show()