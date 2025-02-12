# name = input("What's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
"""method-1"""
names=[]                            #creating a list
with open("names.txt","r") as file: #using 'with' so you don't have to use file.close()  
    for line in file:                            
        names.append(line.rstrip()) #appending list and adding text from names.txt file;line.rstrip() for deleting extra lines 

for i in sorted(names):             #'sorted' for sorting names
    print(f"Hello, {i}")
"""method-2"""
# with open("names.csv","r") as file:
#     for line in sorted(file,reverse=True):
#         print("Hello",line.rstrip())



