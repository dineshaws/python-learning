import zipfile

file1 = open('fileone.txt', 'w+')
file1.write('FILE ONE')
file1.close()

file2 = open('filetwo.txt', 'w+')
file2.write('FILE Two')
file2.close()

# Zip files 
compressed_file = zipfile.ZipFile('compressed.zip', 'w')
compressed_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()
# Extract files
extract_obj = zipfile.ZipFile('compressed.zip', 'r')
extract_obj.extractall('ExtractedFiles')
extract_obj.close()