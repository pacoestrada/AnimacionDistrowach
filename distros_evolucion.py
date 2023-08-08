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
    data.columns = ["Distro", "Rank"]
    data = data.sort_values("Rank").reset_index(drop=True)
    
    # Usamos barras horizontales
    bars = ax.barh(data.index, data["Rank"], color=colors, height=0.8)
    
    # Añadir el nombre de las distribuciones dentro de las barras
    for bar, distro in zip(bars, data["Distro"]):
        ax.text(bar.get_width() - 0.5, bar.get_y() + bar.get_height()/2, 
                distro, va='center', ha='right', color='white', fontsize=10)
    
    # Ajustamos el rango del eje y y x
    ax.set_ylim(-1, len(df.columns)-1)
    ax.set_xlim(10, 0)  # Las posiciones son del 1 al 10, invertimos para que el 1 esté a la izquierda
    
    ax.set_title(f'Distribuciones de Linux en el año {year}')
    ax.set_xlabel("Ranking")
    ax.set_yticks(range(10))
    ax.set_yticklabels([f"{i+1}º" for i in range(10)])

    plt.tight_layout()

# La duración del intervalo determina la velocidad de la animación: un valor más alto la ralentizará
ani = animation.FuncAnimation(fig, update, frames=len(df), repeat=False, interval=1500)
plt.show()


