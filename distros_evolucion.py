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
    
    # Ordenamos por posición
    data = data.sort_values("Rank").reset_index(drop=True)
    
    # Usamos barras horizontales
    bars = ax.barh(data["Rank"], data["Rank"], color=colors, height=0.6)
    
    # Añadir el nombre de las distribuciones dentro de las barras
    for bar, distro in zip(bars, data["Distro"]):
        ax.text(bar.get_width() - 0.5, bar.get_y() + bar.get_height()/2, 
                distro, va='center', ha='right', color='white', fontsize=10)
    
    ax.set_title(f'Distribuciones de Linux en el año {year}')
    
    # Ajustamos el rango del eje y y x
    ax.set_xlim(0, 10.5)  # Las posiciones son del 1 al 10
    ax.set_ylim(10.5, 0.5)  # Las posiciones son del 1 al 10, invertimos para que el 1 esté arriba
    ax.set_xlabel("Ranking")
    ax.set_ylabel("Ranking Actual")
    ax.set_xticks(range(1, 11))
    ax.set_xticklabels([f"{i}º" for i in range(1, 11)])
    ax.set_yticks(range(1, 11))
    ax.set_yticklabels([f"{i}º" for i in range(1, 11)])

    plt.tight_layout()

# La duración del intervalo determina la velocidad de la animación
ani = animation.FuncAnimation(fig, update, frames=len(df), repeat=False, interval=1500)
plt.show()
