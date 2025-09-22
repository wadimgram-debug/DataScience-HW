#data_visualisation.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

def vis_matrix_corr(data):
    sns.heatmap(data.corr(), annot=True)

def pairplot(data):
    sns.pairplot(data, hue='Total')

def boxplot(data):
  sns.set(style="whitegrid")
  plt.figure(figsize=(12, 10))

  # для числовых столбцов
  for index, column in enumerate(data.select_dtypes(include=[np.number]).columns):
    plt.subplot((len(data.columns) // 3) + 1, 3, index + 1)
    sns.boxplot(y=data[column])

  plt.tight_layout()
  plt.show()

def all_value_praph(data):
   # Create a scatter trace
   scatter_trace = go.Scatter(x=data['Precipitation'], y=data['Total'], mode='markers', name='Data Points')
   # Create a figure and add traces
   fig = go.Figure(data=[scatter_trace])
   # Update layout
   fig.update_layout(title='Precipitation graph', xaxis_title='Total', yaxis_title='Precipitation')
   # Show the figure
   fig.show()

   # Create a scatter trace
   scatter_trace = go.Scatter(x=data['High Temp (°F)'], y=data['Total'], mode='markers', name='Data Points')
   # Create a figure and add traces
   fig = go.Figure(data=[scatter_trace])
   # Update layout
   fig.update_layout(title='High Temp graph', xaxis_title='Total', yaxis_title='High Temp')
   # Show the figure
   fig.show()

   # Create a scatter trace
   scatter_trace = go.Scatter(x=data['Low Temp (°F)'], y=data['Total'], mode='markers', name='Data Points')
   # Create a figure and add traces
   fig = go.Figure(data=[scatter_trace])
   # Update layout
   fig.update_layout(title='Low Temp', xaxis_title='Total', yaxis_title='Low Temp')
   # Show the figure
   fig.show()