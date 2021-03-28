# declare and fill list
courses = ['j2ee', 'progjar', 'paal']

# iterate each element
for course in courses:
  print(course)

# get index and value with enumerate
for index, value in enumerate(courses):
  print(index, value)

# get element using index
# python uses zero-based index
print(courses[0])