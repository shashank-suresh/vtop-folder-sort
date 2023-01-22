import os
import re
from datetime import datetime

def getDate(file):
    return re.search(r'\d{2}-\d{2}-\d{4}', file).group(0)

path_to_folder = input("Enter the absolute directory path: ")
file_list = os.listdir(path_to_folder)

file_date = {}
for file in file_list:
    if re.search('Reference_Material', file) is not None:
        file_date[file] = getDate(file)

sortedFiles = sorted(file_date.items(), key=lambda x: datetime.strptime(x[1], '%d-%m-%Y'))

groupedFiles = {}
for file, date in sortedFiles:
    groupedFiles.setdefault(date, []).append(file)

file_num = 1
for date, files in groupedFiles.items():
    groupedFiles[date] = sorted(files, key=lambda x: x.split('Reference_Material_')[1].split('_')[0])

    for file in groupedFiles[date]:
        # print(f'{path_to_folder}\\{file_num}_{file.split("Reference_Material_")[1]}')
        os.rename(f'{path_to_folder}\\{file}', f'{path_to_folder}\\{file_num}_{file.split("Reference_Material_")[1]}')
        file_num += 1

# for date, files in groupedFiles.items():
#     print(date)
#     for file in files:
#         print(file)