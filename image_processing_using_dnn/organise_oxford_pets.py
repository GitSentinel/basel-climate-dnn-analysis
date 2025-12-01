import os
import shutil

base_path = "data/oxfordpets"

for file in os.listdir(base_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        breed = file.split("_")[0]          # e.g., Abyssinian_12.jpg → Abyssinian
        breed_folder = os.path.join(base_path, breed)

        if not os.path.exists(breed_folder):
            os.makedirs(breed_folder)

        src = os.path.join(base_path, file)
        dst = os.path.join(breed_folder, file)

        shutil.move(src, dst)

print("OxfordPets dataset reorganised successfully!")
