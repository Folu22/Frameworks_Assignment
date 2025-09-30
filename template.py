import os
from pathlib import Path

list_of_files = [
    "metadata.csv",
    "analysis.ipynb",
    "app.py",
    "requirements.txt",
    "images/viisualization.png",
]

for files in list_of_files:
    file_path = Path(files)
    filedir, filename = os.path.split(file_path)
    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as fp:
            pass