# write to file using with, no need to close file explicitly
data = 'A test to write to a file'
with open('submission.html', 'w') as f:
    f.write(data)
