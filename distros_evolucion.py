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
    data = data.sort_values("Rank", ascending=True)
    
    # Usamos el índice como valor para las barras y añadimos etiquetas
    ax.barh(data["Distro"], range(1, len(data)+1), color=colors, height=0.8)
    ax.set_title(f'Distribuciones de Linux en el año {year}')
    
    # Ajustamos el rango del eje x
    ax.set_xlim(0, len(df.columns))
    ax.set_xlabel("Ranking")
    
    # Aseguramos que las distribuciones estén etiquetadas en el eje y
    ax.set_yticks(range(1, len(data)+1))
    ax.set_yticklabels(data["Distro"].values)
    
    plt.tight_layout()

ani = animation.FuncAnimation(fig, update, frames=len(df), repeat=False)
plt.show()


