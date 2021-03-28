# read file without close, with statement will close it for us :)
with open('submission.html', 'r') as f:
    text = f.read()