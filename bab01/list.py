# declaration without elements
courses = []

# declaration with elements
languages = ['python', 'java', 'c']
print(languages)

# fill the list
courses.append('progjar')
courses.append('j2ee')
courses.append(2013)
print(courses)

# remove specific element by element
courses.remove('j2ee')
print(courses)

# remove specific element by index
del courses[0]
print(courses)