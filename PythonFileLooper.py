   
import os

root_directory = '.'
for dirname, subdir, filegroup in os.walk(root_directory):
    print('Found directory: %s' % dirname)
    for fname in filegroup:
        print('\t%s' % fname)