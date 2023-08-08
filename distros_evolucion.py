import pandas as pd
import bar_chart_race as bcr
import warnings

# Ignorar advertencias específicas de Matplotlib
warnings.filterwarnings("ignore", category=UserWarning, module="bar_chart_race")

# Leer el archivo CSV con los datos transformados
df_transformed = pd.read_csv('ranking_distribuciones_transformado.csv', index_col=0)

# Para mostrar el número de ranking en el eje y en lugar de los nombres de las distribuciones, 
# transformamos los datos para que las distribuciones sean las columnas y los años las filas
df_bcr = df_transformed.T

# Crear el barchart race
bcr.bar_chart_race(df_bcr, 
                   title='Ranking de Distribuciones por Año', 
                   n_bars=10, 
                   sort='desc',
                   fixed_max=True,
                   cmap='dark24',
                   bar_label_size=7,
                   tick_label_size=7,
                   period_length=1000,  # 1000 milisegundos = 1 segundo por año, puedes ajustarlo
                   filename='barchart_race.mp4',  # Esto guardará el video en formato .mp4
                   filter_column_colors=True,
                   period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
                   period_summary_func=lambda v, r: {'x': .98, 'y': .18, 
                                                    's': f'Year: {r.index.max()}', 
                                                    'ha': 'right', 'size': 8, 'family': 'Courier New'})
