# Read in the file
with open('Lab2-ExploratoryDataAnalysis.R', 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('U+201c', '')
#U+201c
# Write the file out again
with open('Lab2-ExploratoryDataAnalysis.R', 'w') as file:
  file.write(filedata)