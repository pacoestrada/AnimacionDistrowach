import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Cargar el CSV
df = pd.read_csv("DistrosTiempo.csv")

# Transformar los datos
df_melted = df.melt(id_vars=['Año'], 
                    value_vars=df.columns[1:], 
                    var_name='Posición', 
                    value_name='Distribución')
df_melted['Posición'] = df_melted['Posición'].str.extract('(\d+)').astype(int)
df_melted = df_melted.sort_values(by=['Año', 'Posición'])

# Definir los colores
colors = {
    'Slackware': '#000000',
    'Debian': '#D70A53',
    'Red Hat': '#CC0000',
    'Mandrake': '#2D6BA1',
    'SuSE': '#0A74DA',
    'Gentoo': '#54487A',
    'Ubuntu': '#E95420',
    'LFS': '#C7A252',
    'FreeBSD': '#AB2D2D',
    'NetBSD': '#F57900',
    'Fedora': '#294172'
}

# Función de actualización para la animación
def update(year):
    ax.clear()
    data_year = df_melted[df_melted['Año'] == year].copy()
    for distro, color in colors.items():
        position_data = data_year[data_year['Distribución'] == distro]
        if not position_data.empty:
            position = position_data['Posición'].values[0]
            ax.barh(position, position, color=color, edgecolor='white', height=0.8)
            if position > 4:
                ax.text(position-0.5, position, distro, ha='right', va='center', fontsize=10, color='white')
            else:
                ax.text(position+0.5, position, distro, ha='left', va='center', fontsize=10, color='black')
    ax.set_xlim(10, 1)
    ax.set_ylim(10.5, 0.5)
    ax.set_title('Ranking de Distribuciones Linux por Año', fontsize=20)
    ax.text(5.5, 11, f'Año: {year}', ha='center', fontsize=15, fontweight='bold')
    ax.axis('off')

# Preparar la figura y ejes
fig, ax = plt.subplots(figsize=(12, 8))

# Crear la animación
ani = FuncAnimation(fig, update, frames=df['Año'].unique(), repeat=False, interval=1000)

# Guardar la animación (opcional)
writer = PillowWriter(fps=1)
ani.save("barchart_race.gif", writer=writer)

plt.show()
