#Example-1: Create directory if not available
import os

def create_folder(fd):
    if not os.path.exists(fd):
        os.makedirs(fd)


#Example-2: Split directory path
import os

def split_path(path):
    '''
    Split path to basename, filename and extension. For example, 'a/b/c.wav' => ('a/b', 'c', 'wav')
    :param path: filepath = 'a/b/c.wav'
    :return: basename, filename, and extension = ('a/b', 'c', 'wav')
    '''
    basepath, filename = os.path.split(path)
    filename, extension = os.path.splitext(filename)
    return basepath, filename, extension


#Example-3: Remove files in a directory
import os
import glob
def remove_all_files(path):
    files = glob.glob('{}/*'.format(path))
    for f in files:
        os.remove(f)



#Example-4: Get all data paths from a directory
import os

def get_path_dir(data_dir, dataset, **_):
    path = os.path.join(data_dir, dataset)
    if os.path.islink(path):    ##C://animal_DB/Cat/Cat.jpg
        path = os.readlink(path)
    return path

#Example-5: Get file name from a path
import os
def get_filename(path):
    path = os.path.realpath(path)
    print("This is path:", path)
    na_ext = os.path.split(path)[-1]    #or na_ext = os.path.basename(path)
    print("This is end_file name:", na_ext)
    na = os.path.splitext(na_ext)[0]
    return na

dirt = "G:\\KU_BE_AI_PROJECTS\\CHAPTER-1_PythonBasic\\OS_Operation\Hello_OS.txt"
out = get_filename(dirt)
print(out)


#Example-6: Get file name from a path
import os

def get_all_filenames(data_split):
    
    dirname = 'F:/SPEECH_DB_TOTAL/LibriSpeech_CPC_DB/LibriSpeech/dev-clean/'
    
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths


#Example-7: Get file name from a path (Trickey)
import pandas as pd

meta_path = "/root_dir/"
extension = "*.csv"

all_csv_files = [file
                     for path_dir, subdir, files in os.walk(meta_path)
                     for file in glob(os.path.join(path_dir, extension))] # Get all the cvs file paths

#Read one by one file from the list
for file in all_csv_files:
    print("The whole path of individual file:", file)
    
    split_list = file.split('/')    #Separate last file name only
    
    name = str(split_list[-1].split('.')[0])    #The filename without extension
    feat_name = name + '.h5' 
    
    #Read datafrome
    df = pd.read_csv(file, header=0, index_col=False)
    df_pos = df[(df == 'POS').any(axis=1)] # Find any row that contains POS
    
    cls_list = [df_pos.columns[(df_pos == 'POS').loc[index]].values for index, row in df_pos.iterrows()] #Make a class list
    
    audio_path = file.replace('csv', 'wav') #Move to respective audio file location from CSV file


#Example-8: Make a python program to move or copy one or all files from one directory to other.
import os
import shutil

base_path = "G:/KU_BE_AI_PROJECTS/CHAPTER-1_PythonBasic/"

source = base_path+"Class_Jan9/"
destination = base_path+"Class_Jan9__/"

allfiles = os.listdir(source)
print(allfiles)

for f in allfiles:
    #shutil.move(source + f, destination + f)   #Move file
    shutil.copy(source + f, destination + f)    #Copy files



#Example-9: Remove space and rename all files in a directory.

import os

path = "D:/MUSIC_VIDEO_DB_ALL/MV_5M_DB/video_train9/"

for filename in os.listdir(path):
    filename_without_ext = os.path.splitext(filename)[0]
    #print(filename_without_ext)
    #filename_without_ext = filename_without_ext.replace(" ","")
    #filename_without_ext = filename_without_ext.replace("_RT","")
    
    extension = os.path.splitext(filename)[1]
    
    #no_space = filename_without_ext.split('space')
    
    #print(extension)
    new_file_name = filename_without_ext+"_SET9"
    #new_file_name = no_space+"_2RT"
    new_file_name_with_ext = new_file_name+extension
    print(new_file_name_with_ext)
    os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))


#Example-11: Convert .csv file data into .txt file.

import os
import pandas as pd

#Write only two column of csv into txt file
base_path = '../CSV_Operations/'

train_df = pd.read_csv(os.path.join(base_path, 'sample_one.csv'))

# For Audio
f= open(base_path + "/sample_one.txt","w+")

for idx, row in train_df.iterrows():   
    filename = row[0]
    event= str(row[1])
    
    f.write(filename + '\t' + event + '\n')
f.close()


#Example-12: Convert .txt to .csv
import pandas as pd
df = pd.read_fwf('../Outcome/sample_one_test.txt')
df.to_csv('../Outcome/sample_one_test_NN.csv')


#Example-13: Merge multiple .csv files into one (useful for data error handling)
import os
import glob
import pandas as pd
os.chdir("./Input_dirs/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

combined_csv = []
for filename in all_filenames:
    df = pd.read_csv(filename) 
    df["filename"] = filename
    #print(df)
    #combined_csv = pd.concat([pd.read_csv(filename)])
    combined_csv.append(df)

df_concat = pd.concat(combined_csv)

df_concat.to_excel("./Out/VAL_FEW_SHOT_output.xlsx")    #Output in excel






