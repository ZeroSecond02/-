import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Загрузка модели
model = tf.keras.models.load_model('flower_classification_model.h5')
class_names = ['astilbe', 'calendula', 'carnation', 'common_daisy', 'iris', 'magnolia', 'rose', 'sunflower', 'tulip', 'water_lily']

# Функция для предсказания
def predict(image_path):
    image = Image.open(image_path).resize((150, 150))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    predicted_class = class_names[np.argmax(predictions)]
    return predicted_class

# Функция для загрузки изображения
def load_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        prediction = predict(file_path)
        result_label.config(text=f'Prediction: {prediction}')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process the image.\nError: {e}")

# Создание главного окна
root = tk.Tk()
root.title("Flower Classification")

# Создание и размещение виджетов
image_label = tk.Label(root)
image_label.pack()

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

result_label = tk.Label(root, text="Prediction: ")
result_label.pack()

# Запуск главного цикла
root.mainloop()
