# MEE 03/23/22

my_file = open("alma_mater.txt")
contents = my_file.readlines() 
for x in contents:
    print(x)
my_file.close()