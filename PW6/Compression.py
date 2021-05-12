from zipfile import ZipFile

def compressing():
    file_paths = ['students.txt', 'courses.txt', 'marks.txt']
    with ZipFile('students.dat', 'w') as zip:
        for file in file_paths:
            zip.write(file)

