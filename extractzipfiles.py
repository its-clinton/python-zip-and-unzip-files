import zipfile

with zipfile.ZipFile('files.zip', 'r') as my_zip_file:
	my_zip_file.extractall('files')