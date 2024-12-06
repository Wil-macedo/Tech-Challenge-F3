import kagglehub
import shutil
import os

try:
    # Download latest version
    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud", force_download=True)

    files = os.listdir(path)
    destination = os.path.join(os.path.abspath(os.path.curdir),"DATASET")

    for file in files:
        if not os.path.exists(destination):  # Create directory
            os.makedirs(destination)
            
        shutil.move(os.path.join(path, file), os.path.join(destination, "base.csv"))
        
except Exception as ex:
    print("Failed to download dateset")