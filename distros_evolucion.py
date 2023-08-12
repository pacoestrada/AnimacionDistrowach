import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

# Definimos colores para las distribuciones
colors = {
    'Slackware': '#000000',  # Negro
    'Debian': '#D70A53',     # Rojo Debian
    'Red Hat': '#CC0000',    # Rojo Red Hat
    'Mandrake': '#2D6BA1',   # Azul
    'SuSE': '#0A74DA',       # Azul SuSE
    'Gentoo': '#54487A',     # Morado Gentoo
    'Ubuntu': '#E95420',     # Naranja Ubuntu
    'LFS': '#C7A252',        # Dorado
    'FreeBSD': '#AB2D2D',    # Rojo FreeBSD
    'NetBSD': '#F57900',     # Naranja
    'Fedora': '#294172'      # Azul Fedora
}

# Preparar la figura y los ejes
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(10, 1)  # Invertimos el eje X para que 1 esté a la derecha y 10 a la izquierda
ax.set_ylim(10.5, 0.5)  # Posición de las barras
ax.set_title('Ranking de Distribuciones Linux por Año', fontsize=20)

# Función para actualizar la animación
def update(year):
    ax.clear()  # Limpiamos el lienzo para cada frame
    data_year = df_melted[df_melted['Año'] == year].copy()
    data_year.set_index('Distribución', inplace=True)
    
    # Dibujar las barras
    for distro, color in colors.items():
        if distro in data_year.index:
            position = data_year.loc[distro, 'Posición']
            ax.barh(position, position, color=color, edgecolor='white', height=0.8)
            ax.text(5, position, distro, ha='center', va='center', fontsize=12, color='white')
    
    # Configuraciones adicionales para el gráfico
    ax.set_xlim(10, 1)
    ax.set_ylim(10.5, 0.5)
    ax.set_title('Ranking de Distribuciones Linux por Año', fontsize=20)
    ax.text(5, 11.5, f'Año: {year}', ha='center', fontsize=15, fontweight='bold')
    ax.axis('off')  # Ocultamos los ejes

# Crear la animación
ani = FuncAnimation(fig, update, frames=df['Año'].unique(), repeat=False, interval=2000)

plt.show()
