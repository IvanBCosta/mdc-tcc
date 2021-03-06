import glob
import pandas as pd
import shutil
import subprocess
import os

# read filenames and image ids
PATH = "/media/slow/data/landmarks/**/*.jpg"
DESTINATION_PATH = "/media/slow/data/landmarks/selected/"
files = []

for filename in glob.iglob(PATH, recursive=True):
     files.append([filename[-20:-4], filename])

data = pd.DataFrame(files)
data.columns = ["id", "path"]
print("number of files: ", data.shape[0])

# read selected images
selected_data = pd.read_csv("./Landmarks/data/subset_landmarks_all.csv")
print("number of selected image files: ", selected_data.shape[0])

# associated selected images with local paths
merged_data = pd.merge(selected_data, data, on='id', how='inner')
print("number of selected image found: ", merged_data.shape[0])

# create folders
for item in selected_data.landmark_id.unique():
    directory_path = f"{DESTINATION_PATH}{item}"
    if not os.path.exists(directory_path):
        bashCommand = f"mkdir {directory_path}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

# Get copied files
copied_files = []
for filename in glob.iglob(f"{DESTINATION_PATH}**/*.jpg", recursive=True):
     copied_files.append(filename[-20:-4])
print("number of copied images: ", copied_files.__len__())

# move files to a central place
count = 0
for index, row in merged_data.iterrows():
    if row.id not in copied_files:
        count = count + 1
        bashCommand = f"cp {row.path} {DESTINATION_PATH}{row.landmark_id}/"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
print("number of moved images: ", count)
