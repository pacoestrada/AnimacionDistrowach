import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Convertir los datos del CSV en un DataFrame
data = """
Año,1.ª,2.ª,3.ª,4.ª,5.ª,6.ª,7.ª,8.ª,9.ª,10.ª
1996,Slackware,Debian,Red Hat,Mandrake,SuSE,Gentoo,Slackware,LFS,FreeBSD,NetBSD
1997,Slackware,Debian,Red Hat,Mandrake,SuSE,Gentoo,Slackware,LFS,FreeBSD,NetBSD
1998,Slackware,Debian,Red Hat,Mandrake,SuSE,Gentoo,Slackware,LFS,FreeBSD,NetBSD
1999,Slackware,Debian,Red Hat,Mandrake,SuSE,Gentoo,Slackware,LFS,FreeBSD,NetBSD
2000,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,Slackware,LFS,FreeBSD,NetBSD
2001,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,Ubuntu,LFS,FreeBSD,NetBSD
2002,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,Ubuntu,LFS,FreeBSD,NetBSD
2003,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2004,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2005,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2006,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2007,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2008,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2009,Ubuntu,Red Hat,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2010,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2011,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2012,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2013,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2014,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2015,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2016,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2017,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2018,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2019,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2020,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2021,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
2022,Ubuntu,Fedora,Slackware,Debian,Mandrake,SuSE,Gentoo,LFS,FreeBSD,NetBSD
"""

# Convertir la cadena CSV en un DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Convertir el DataFrame en un formato adecuado para el gráfico de barras de carrera
df_melted = df.melt(id_vars="Año", var_name="Ranking", value_name="Distribución").set_index("Año")

# Crear una paleta de colores única para cada distribución
unique_distributions = df_melted["Distribución"].unique()
colors = plt.cm.tab20.colors  # 20 colores distintos
color_map = {dist: colors[i % 20] for i, dist in enumerate(unique_distributions)}

# Función corregida para asegurar que la longitud de las barras refleje adecuadamente el
# Función corregida para asegurar que la longitud de las barras refleje adecuadamente el ranking
def draw_barchart_final_v4(year):
    ax.clear()
    data_for_year = df_melted.loc[year].sort_values()
    y_positions = np.arange(len(data_for_year))
    
    # La longitud de las barras ahora se determina por el inverso del ranking, asegurando que el ranking más alto tenga la barra más larga
    bar_lengths = 11 - data_for_year.values
    
    ax.barh(y_positions, bar_lengths, color=[color_map[col] for col in data_for_year.index])
    
    # Configuración del gráfico
    for i, (value, name) in enumerate(zip(data_for_year, data_for_year.index)):
        ax.text(0.5, i, name, size=10, weight=600, ha='left', va='center', color='white')
        ax.text(10.5, i, f'{value:.0f}', size=10, ha='right', va='center')
    
    ax.text(1, 0.2, year, transform=ax.transAxes, color='#777777', size=40, ha='right', weight=600)
    ax.text(0, 1.06, 'Ranking', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(list(range(1, len(data_for_year) + 1)))
    ax.invert_yaxis()  # invertir el eje y para que el 1 esté en la parte superior
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.15, 'Las mejores distribuciones de Linux de 1996 a 2022',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    plt.box(False)
    ax.set_xlim(0, 10.5)

# Crear la figura y el eje nuevamente
fig, ax = plt.subplots(figsize=(15, 9))

# Crear la animación con las correcciones
animator_final_v4 = FuncAnimation(fig, draw_barchart_final_v4, frames=df_melted.index, repeat=False)

# Guardar la animación final como MP4
file_path_final_v4 = "/home/yo/race_final_v4.mp4"
animator_final_v4.save(file_path_final_v4, writer='ffmpeg', fps=0.5)

file_path_final_v4

