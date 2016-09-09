def read_entire_file(file_name):
    with open(file_name) as my_file:
        output = my_file.read()
    return output

print read_entire_file("gabby_fav_foods.txt")
print read_entire_file("michelle_fav_foods.txt") 

def compare_faves(gabby,michelle):
    with open(gabby) as my_file:
        output1 = my_file.readline()
    with open(michelle) as my_file:
        output2 = my_file.readline() 
    if output1 == output2:
        return "Our favorite foods are the same!"
    else:
        return "Our favorite foods are different." 