import os
import concurrent.futures

def rename_file(file_info):
    directory, filename = file_info
    new_filename = filename.replace('_img', '')
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

def rename_files_in_directory(directory):
    with os.scandir(directory) as entries:
        files_to_rename = [(directory, entry.name) for entry in entries if entry.is_file() and '_img' in entry.name]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(rename_file, files_to_rename)

if __name__ == "__main__":
    directory = '/scratch/rmandal/large_files/Datasets/Synth43k/images/'
    rename_files_in_directory(directory)
    print("Renaming completed.")
