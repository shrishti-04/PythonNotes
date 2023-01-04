# denoting dictionary
file_counts = {'jpg': 12, 'txt': 15, 'csv': 23, 'py': 30}
print(file_counts)

# OUTPUT
# {'jpg': 12, 'txt': 15, 'csv': 23, 'py': 30}

# to find the element through indexing
print(file_counts['txt'])

# OUTPUT
# 15

# to find the element using in function
jpg = 'jpg' in file_counts
print(jpg)
# OUTPUT
# True

html = 'html' in file_counts
print(html)
# OUTPUT
# False

# adding an element in dictionary
file_counts['png'] = 23
print(file_counts)

# OUTPUT
# {'jpg': 12, 'txt': 15, 'csv': 23, 'py': 30, 'png': 23}

# replacing an element value in dictionary
file_counts['txt'] = 10
print(file_counts)

# OUTPUT
# {'jpg': 12, 'txt': 15, 'csv': 23, 'py': 30, 'png': 23}   EARLIER VALUE
# {'jpg': 12, 'txt': 10, 'csv': 23, 'py': 30, 'png': 23}   REPLACED VALUE

# deletion of an element in dictionary
del file_counts['py']
print(file_counts)

# OUTPUT
# {'jpg': 12, 'txt': 10, 'csv': 23, 'py': 30, 'png': 23}   EARLIER VALUE
# {'jpg': 12, 'txt': 10, 'csv': 23, 'png': 23}   DELETED VALUE