import matplotlib.pyplot as plt

plt.ion()
fig, ax = plt.subplots()
line_scores, = ax.plot([], [], label="Score")
line_mean,   = ax.plot([], [], label="Mean")
ax.set_xlabel("Number of Games")
ax.set_ylabel("Score")
ax.legend()

def plot(scores, mean_scores):
    ax.set_ylim(0, max(max(scores), max(mean_scores)) + 10)
    line_scores.set_data(range(len(scores)), scores)
    line_mean.set_data(range(len(mean_scores)), mean_scores)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()