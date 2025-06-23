import os
import shutil
source_folder = r"C:\Users\Nehal\Downloads"
destination_folder = r"C:\Users\Nehal\Documents\OrganizedDownloads"
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Code': ['.py', '.cpp', '.java'],
}
def organize_files():
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(destination_folder, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved {filename} → {folder_name}/")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(destination_folder, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"✅ Moved {filename} → Others/")
#print(f"Would move: {file_path} → {target_folder}")

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")
