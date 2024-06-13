#Creating directory using os module  
'''
import os

def create_directory(fd):
    if not os.path.exists(fd):
        os.makedirs(fd)

data_path = "D:\Projects\Python\Python-Series\Assingment\test_directory"
create_directory(data_path)

'''

#Example-2: Split directory path
'''
import os

def split_path(path):
    basepath, filename = os.path.split(path)
    basepath1, dir_name = os.path.split(basepath)
    filename, extension = os.path.splitext(filename)
    return basepath1, dir_name, basepath, filename, extension

data_path = "D:\Projects\Python\Python-Series\Assingment\test_directory\GANESH.png"
basepath1, dir_name, base_path, file, ext = split_path(data_path)
print(base_path, basepath1)
print("The class label:", dir_name)
print(file)
print(ext)

'''

#Example-3: Remove files in a directory
'''
import os
import glob
def remove_all_files(path):
    files = glob.glob('{}\*'.format(path))
    for f in files:
        os.remove(f)

data_path = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory"
remove_all_files(data_path)

'''

#Example-4: Get file name from a path
'''
def get_filename(path):
    path = os.path.realpath(path)
    print("This is path:", path)
    na_ext = os.path.split(path)[-1]    #or na_ext = os.path.basename(path)
    print("This is end_file name:", na_ext)
    na = os.path.splitext(na_ext)[0]
    return na


dir_name= "D:\Projects\Python\Python-Series\Assingment\test_directory\GANESH.png"
out = get_filename(dir_name)
print(out)
'''

#Example-5: Get all file name from a path
'''
import os

def get_all_filenames(data_split):
    
    file_paths = []  
    for root, directories, files in os.walk(data_split):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths

dir_name= "D:\\Projects\\Python\Python-Series\\Assingment\\test_directory"
output = get_all_filenames(dir_name)
print("The lis of all file is:",output)


'''


#Example-6: Make a python program to move or copy one or all files from one directory to other.
'''
import os
import shutil

def create_folder(fd):
    if not os.path.exists(fd):
        os.makedirs(fd)

base_path = "D:\\Projects\\Python\Python-Series\\Assingment\\test_directory\\"

source = base_path+"Source\\"
destination = base_path+"Destination\\"

create_folder(destination)

allfiles = os.listdir(source)
print(allfiles)

for f in allfiles:
    #shutil.move(source + f, destination + f)   #Move file
    shutil.copy(source + f, destination + f)    #Copy files

'''

##Task 1
##Write a program that can add "_Data_Plus" to the end of each file in a directory.
## Hint: use OS library and replace() function 
'''
import os
import shutil

def create_folder(fd):
    if not os.path.exists(fd):
        os.makedirs(fd)

base_path = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\"

source = base_path + "Source\\"
destination = base_path + "Destination\\"

create_folder(destination)

allfiles = os.listdir(source)
print(allfiles)

for f in allfiles:
    # shutil.move(source + f, destination + f)   # Move file
    shutil.copy(source + f, destination + f)    # Copy files

    base, ext = os.path.splitext(f)
    os.rename(destination + f, destination + base + "_Data_Plus" + ext)
    print("The file name is:", base + "_Data_Plus" + ext) '''


### Task2: Write a program to convert large number of .txt file into .csv file in a directory.

'''
import os
import pandas as pd

source_dir = "D:\\Projects\\Python\\Python-Series\Assingment\\test_directory\\Source\\"
destination_dir = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\Destination\\"

txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

for txt_file in txt_files:
    df = pd.read_csv(os.path.join(source_dir, txt_file), delimiter = "\t")
    csv_file = os.path.splitext(txt_file)[0] + ".csv"  # Change extension to .csv
    df.to_csv(os.path.join(destination_dir, csv_file), index=False)


'''



### Task3: Suppose you have a list [0.152264, 6.315308, 12.583487, 18.643744, 24.762218, 30.928, 37.19, 43.169695, 49.266612, 55.565, 61.934, 68.001842, 74.247843, 80.468893, 86.821, 93.052]. Generate 12 equal points in between each item in the list and save them in a .txt file. Make a python program with and without using “linspace” built-in function.

'''
import numpy as np
import os


numbers = [0.152264, 6.315308, 12.583487, 18.643744, 24.762218, 30.928, 37.19, 43.169695, 49.266612, 55.565, 61.934, 68.001842, 74.247843, 80.468893, 86.821, 93.052]
points = []

for i in range(len(numbers) - 1):
    points.append(np.linspace(numbers[i], numbers[i+1], 14)[1:-1])  # Exclude the start and end points

points = [item for sublist in points for item in sublist]  # Flatten the list
points.append(numbers[-1])  # Append the last number

with open('points.txt', 'w') as f:
    for point in points:
        f.write("%s\n" % point)

'''

### Task 4:#Example-13: Write a program to merge multiple .csv files into one.

'''
import os
import pandas as pd

source_dir = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\Source\\"
destination_dir = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\Destination\\"

csv_files = [f for f in os.listdir(source_dir) if f.endswith('.csv')]
print(csv_files)

df = pd.concat([pd.read_csv(os.path.join(source_dir, csv_file)) for csv_file in csv_files])
df.to_csv(os.path.join(destination_dir, 'merged.csv'), index=False)


'''


import pandas as pd

file_path = "D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\Source\\employee - employee.csv"
# Read the CSV file
data = pd.read_csv(file_path)
#convert the csv file into text file
data.to_csv("D:\\Projects\\Python\\Python-Series\\Assingment\\test_directory\\Destination\\employee - employee.txt", sep="\t", index=False)

'''
# Print the first few rows of the DataFrame
print(data.head())
print(data.shape)
print(data.dtypes)
print(data.columns)
print(data.describe())
print(data.info())
print(data.isnull().sum())  

# Print the unique values in the 'Department' column
print(data['department'].unique())

# Print the number of unique values in the 'Department' column

print(data['department'].nunique())

#isin method
print(data[data['department'].isin(['Sales', 'Finance'])])
'''


