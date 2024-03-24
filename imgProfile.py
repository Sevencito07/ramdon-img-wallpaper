import ctypes
import os
import random
import time

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def get_random_image_from_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return os.path.join(folder_path, random.choice(image_files))

if __name__ == "__main__":
    # Ruta de la carpeta que contiene las imágenes
    folder_path = "C:\\Users\\gerso\\OneDrive\\Pictures\\some"

    # Intervalo de cambio de fondo de pantalla (en segundos)
    change_interval = 2 * 60  # 10 minutos

    while True:
        # Obtener una imagen aleatoria de la carpeta
        random_image = get_random_image_from_folder(folder_path)

        # Cambiar el fondo de pantalla
        change_wallpaper(random_image)

        # Esperar hasta el siguiente cambio
        time.sleep(change_interval)
