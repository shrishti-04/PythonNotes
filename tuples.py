def calc_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes*60
    
    return hours, minutes, remaining_seconds
    
result = calc_seconds(5000)

print(type(result))
print(result)

# to remove tuples
hours, minutes, seconds=result
print(hours, minutes, seconds)

# Q2 Let's use tuples to store information about a file: its name, its type and its size
# in bytes. Fill in the gaps in this code to return the size in kilobytes
# (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
    file_name, file_type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21