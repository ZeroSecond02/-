import os
import shutil
import random

# Укажи путь к основной директории с исходными данными
base_dir = 'dataset'

def save_flows(directory, save_path):
    """
    directory (str): Путь к директории с поддиректориями
    save_path (str): Путь к файлу
    """
    # Получаем список поддиректорий в указанной директории
    flows = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    flows.sort()  # Опционально, сортировка списка
    
    # Сохраняем список в файл
    with open(save_path, 'w') as file:
        for flow in flows:
            file.write(flow + '\n')

# Использование функции
directory_path = os.path.join(base_dir, 'test')  # Путь к папке
save_path = 'flows_list.txt'  # Путь к файлу для сохранения списка
save_flows(directory_path, save_path)
