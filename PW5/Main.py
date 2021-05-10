from domains.Driver import Driver
from zipfile import ZipFile

# Create object driver
d = Driver()
d.run_Driver()

# Function to zip all .txt files
def compressing():
    file_paths = ['students.txt', 'courses.txt', 'marks.txt']
    with ZipFile('students.dat', 'w') as zip:
        for file in file_paths:
            zip.write(file)

compressing()

