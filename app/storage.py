import os
import uuid

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_file(file_content, original_name):
    # Génère un nom unique avec un slug
    file_extension = original_name.split('.')[-1]
    slug = f"{uuid.uuid4().hex}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER, slug)

    # Sauvegarde le fichier
    with open(file_path, "wb") as f:
        f.write(file_content)
    return slug, file_path
