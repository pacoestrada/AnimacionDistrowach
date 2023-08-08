import pandas as pd
import bar_chart_race as bcr
import warnings

# Ignorar advertencias específicas de Matplotlib
warnings.filterwarnings("ignore", category=UserWarning, module="bar_chart_race")

# Leer el archivo CSV con los datos transformados
df_transformed = pd.read_csv('ranking_distribuciones_transformado.csv', index_col=0)

# Crear el barchart race
bcr.bar_chart_race(df_transformed, 
                   title='Ranking de Distribuciones por Año', 
                   n_bars=10, 
                   sort='desc',
                   fixed_max=True,
                   cmap='dark24',
                   bar_label_size=7,
                   tick_label_size=7,
                   period_length=1000,  # 1000 milisegundos = 1 segundo por año, pero puedes ajustarlo
                   filename='barchart_race.mp4',  # Esto guardará el video en formato .mp4
                   filter_column_colors=True)  

