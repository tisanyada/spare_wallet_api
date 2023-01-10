import os
from .id_generator import avatar_id_generator


def profile_avatar_path(model, file):
    class_name = "images"
    code = "profiles"
    filename = avatar_id_generator() + "." + file.split(".")[1]
    return os.path.join(class_name, code, filename)
