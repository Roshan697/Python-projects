import os 
import shutil

folder_path = "C:/Users/rosha/Downloads"
folder_types = {"Images":[".jpg",".png",".gif"],
               "Documents":[".pdf",".docx",".txt"],
               "Videos":[".mp4",".mkv"],
               "Music":[".mp3",".wav"]
               }

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        for folder, extensions in folder_types.items():
            if file.endswith(tuple(extensions)):
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok = True)
                shutil.move(file_path, dest_folder)
                
print("Files organized succesfully! ")                