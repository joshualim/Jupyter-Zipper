#!/usr/bin/env python
# coding: utf-8

# # Zipper
# ***user beware: only run this code if you understand what it does***

# In[ ]:


# Run this cell to zip just .ipynb in a workspace and subdirectories

from datetime import datetime
prefix = "myNoteableWorkspace"
filename = prefix + "_" + datetime.now().strftime("%Y_%m_%d_%H%M")
get_ipython().system('zip -r {filename}.zip ~/*.ipynb    ## zip only .ipynb files')
get_ipython().system('zip -r {filename}.zip ~/*          ## zip **everything** (probably not a good idea, if run recursively it will zip the zip file...)')


# A better idea below:
# - this creates a "backups" folder to store backups and exclude this from the archive
# - it's also easy to add other filters for what to include exclude

# In[ ]:


import os
import zipfile
from datetime import datetime

prefix = "myNoteableHomeFolder"
zipFilename = prefix + "_" + datetime.now().strftime("%Y_%m_%d_%H%M") + ".zip"

# get the path of the home directory
home_path = os.path.expanduser("~")

# name of the backups folder for storage
backup_folderName = 'backups'

# get the path of the backups folder
backups_path = os.path.join(home_path, backup_folderName)

# If no backups folder exists, create one
if not os.path.exists(backups_path):
    os.makedirs(backups_path)

# create an empty zip file in the backups folder
zip_file = zipfile.ZipFile(os.path.join(backups_path, zipFilename), "w")

# walk through the home directory and its subdirectories
for root, dirs, files in os.walk(home_path):
    
    dirs[:] = [d for d in dirs if not d[0] == '.']        # exclude hidden directories
    dirs[:] = [d for d in dirs if d != backup_folderName] # exclude backups folder (important to avoid recursion)
    # dirs[:] = [d for d in dirs if d != 'test']            # exclude "test" folder (edit as needed)
    files = [f for f in files if not f[0] == '.']         # exclude hidden files
    # files = [f for f in files if f.endswith('.ipynb')]             # include only files with ".ipynb" extension
            
    # loop through the files
    for file in files:
        # get the full path of the file
        file_path = os.path.join(root, file)
        
        # get the relative path of the file from the home directory
        #file_rel = os.path.relpath(file_path, home_path)
        #print(file_rel)
        
        # add the file to the zip file
        zip_file.write(file_path)
        # print(file_path)

# close the zip file
zip_file.close()


# # Unzipper
# Run this code to unzip the files. This uses zip rather than tar, as most students will be more familiar with this method.

# In[ ]:


# Run this cell to unzip all zip files in the current directory 
get_ipython().system("unzip '*.zip'")

