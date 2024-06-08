import os
import shutil
import random
# Укажи путь к основной директории с исходными данными
base_dir = 'dataset'

# Директории для хранения разделенных данных
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')

# Создадим новые директории
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Категории цветов
categories = ['astilbe', 'calendula', 'carnation', 'common_daisy', 'iris', 'magnolia', 'rose', 'sunflower', 'tulip', 'water_lily']
for category in categories:
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(val_dir, category), exist_ok=True)
    os.makedirs(os.path.join(test_dir, category), exist_ok=True)
# Функция для разделения данных
def split_data(base_dir, train_dir, val_dir, test_dir, categories, train_split=0.8, val_split=0.1, test_split=0.1):
    for category in categories:
        category_dir = os.path.join(base_dir, category)
        images = os.listdir(category_dir)
        random.shuffle(images)
        
        # Определим количество изображений для каждого набора
        train_size = int(train_split * len(images))
        val_size = int(val_split * len(images))
        test_size = len(images) - train_size - val_size
        
        train_images = images[:train_size]
        val_images = images[train_size:train_size + val_size]
        test_images = images[train_size + val_size:]
        
        # Копируем изображения в соответствующие директории
        for img in train_images:
            shutil.copy(os.path.join(category_dir, img), os.path.join(train_dir, category, img))
        for img in val_images:
            shutil.copy(os.path.join(category_dir, img), os.path.join(val_dir, category, img))
        for img in test_images:
            shutil.copy(os.path.join(category_dir, img), os.path.join(test_dir, category, img))

# Запускаем функцию для разделения данных
split_data(base_dir, train_dir, val_dir, test_dir, categories)
