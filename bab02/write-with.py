# write to file using with, no need to close file explicitly
with open('submission.html', 'w') as f:
    f.write(data)