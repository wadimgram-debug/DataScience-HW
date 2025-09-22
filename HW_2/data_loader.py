#data_loader
import pandas as pd

#Загрузка данных из CSV файла
def load_data_csv(file_path):
   try:
      print(f"Файл {file_path} загружен")
      return pd.read_csv(file_path)
   except Exception as e: # Catching a more general exception
      print(f"Ошибка загрузки файла: {e}")
