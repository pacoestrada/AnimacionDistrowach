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
    data = data.sort_values("Rank", ascending=False).reset_index(drop=True)
    
    # Usamos el índice como valor para las barras y añadimos etiquetas
    ax.barh(data.index, range(1, len(data)+1), color=colors, height=0.8)
    
    # Añadir el nombre de las distribuciones como etiquetas en el eje y
    ax.set_yticks(data.index)
    ax.set_yticklabels(data["Distro"])
    
    ax.set_title(f'Distribuciones de Linux en el año {year}')
    ax.set_xlabel("Ranking")
    
    # Ajustamos el rango del eje x
    ax.set_xlim(0, len(df.columns))
    
    plt.tight_layout()

ani = animation.FuncAnimation(fig, update, frames=len(df), repeat=False)
plt.show()



