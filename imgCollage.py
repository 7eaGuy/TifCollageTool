from PIL import Image, ImageOps
import os

def create_image_from_folders(base_folder,folder_list, spacing):
    images = []
    max_width = 0
    max_height = 0

    for folder_name in folder_list:
        folder_path = os.path.join(base_folder, folder_name)
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img = Image.open(os.path.join(folder_path, filename))
                images.append(img)
                max_width = max(max_width, img.width)
                max_height = max(max_height, img.height)

    columns = len(images) // 2
    rows = (len(images) + 1) // columns

    total_width = columns * max_width + (columns - 1) * spacing
    total_height = rows * max_height + (rows - 1) * spacing

    result = Image.new("RGB", (total_width, total_height), "white")

    x_offset = 0
    y_offset = 0

    for i, img in enumerate(images):
        if i % columns == 0 and i != 0:
            x_offset = 0
            y_offset += max_height + spacing
        result.paste(img, (x_offset, y_offset))
        x_offset += max_width + spacing

    result = ImageOps.expand(result, spacing*2, "white")

    result.save("Результат.tif")

# Пример использования
base_folder = ""
folder_list = ['TEST1', 'TEST2']  # Список папок
spacing = 60

create_image_from_folders(base_folder,folder_list, spacing)