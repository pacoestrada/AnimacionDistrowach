import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# Leemos el archivo CSV
df = pd.read_csv("DistrosTiempo.csv")

n_observations = 10

fig, ax = plt.subplots(figsize=(10, 5))

font = {
    'weight': 'normal',
    'size': 15,
    'color': 'lightgray'
}

years = df['Año'].unique()

label = ax.text(0.95, 0.20, years[0],
                horizontalalignment='left',
                verticalalignment='top',
                transform=ax.transAxes,
                fontdict=font)

colors = plt.cm.tab20c(np.linspace(0, 1, n_observations))

def update_barchart_race(i):
    year = years[i]
    data_temp = df[df['Año'] == year].drop(columns='Año').T
    data_temp.columns = ['Value']
    data_temp['Ranking'] = data_temp['Value'].rank(ascending=False)
    data_temp = data_temp.sort_values('Ranking').head(n_observations)

    ax.clear()
    ax.barh(y=data_temp['Ranking'],
            width=data_temp['Value'],
            tick_label=data_temp.index,
            color=colors)

    ax.text(0.95, 0.20, year,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes,
            fontdict=font)
    
    ax.set_ylim(ax.get_ylim()[::-1])  # Revert axis

anim = animation.FuncAnimation(fig, update_barchart_race, frames=len(years), repeat=False)
anim.save('distros_barchart_race.gif', writer="pillow", fps=1)
plt.show()
