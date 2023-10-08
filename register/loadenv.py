import os

def load_env(dotenv_path):
    result = {}
    with open(dotenv_path) as file_obj:
        lines = file_obj.read().splitlines() 

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if "#" in line:
            line = line.split("#")[0].strip()
        key, value = line.split("=", maxsplit=1)
        result[key] = value
    return result