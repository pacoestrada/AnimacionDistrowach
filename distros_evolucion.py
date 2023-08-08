import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar datos
df = pd.read_csv("DistrosTiempo.csv")

# Preparar figura y eje
fig, ax = plt.subplots(figsize=(10, 8))
colors = plt.cm.Paired(range(len(df.columns)-1))

def update(num):
    ax.clear()
    year = df['Año'].iloc[num]
    data = df.iloc[num, 1:].reset_index()
    data.columns = ["Rank", "Distro"]
    
    # Ordenamos por posición y reseteamos el índice
    data = data.sort_values("Rank").reset_index(drop=True)
    
    # Usamos barras verticales
    ax.bar(data.index, range(1, len(data)+1), color=colors, width=0.8)
    
    # Añadir el nombre de las distribuciones como etiquetas en el eje x
    ax.set_xticks(data.index)
    ax.set_xticklabels(data["Distro"], rotation=45, ha='right')
    
    ax.set_title(f'Distribuciones de Linux en el año {year}')
    ax.set_ylabel("Ranking")
    
    # Ajustamos el rango del eje y
    ax.set_ylim(0, len(df.columns))
    
    plt.tight_layout()

# La duración del intervalo determina la velocidad de la animación: un valor más alto la ralentizará
ani = animation.FuncAnimation(fig, update, frames=len(df), repeat=False, interval=1500)
plt.show()


