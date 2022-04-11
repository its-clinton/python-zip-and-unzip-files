import zipfile

#writing to  a zip file.Ensure your  files including the python file are all in the same directory

my_zip_file = zipfile.ZipFile('files.zip', 'w') #'files.zip' is the name for the zip we are creating . we also open the file here ready for writing

# writing the files or placing them into a zip file(files.zip)
my_zip_file.write('text.txt')
my_zip_file.write('thumbnail.txt')
my_zip.close() #closing the opened zip file



