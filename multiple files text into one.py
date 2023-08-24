file1= input("enter the name of the file:")
file2= input("enter the name of the file:")
destination=input("enter the destinated file name:")

def merge(filename1,filename2,newfilename):
    file1=open(filename1)
    file2=open(filename2)

    new_file=open("new_filename","w")

    file1_contents = file1.read()
    print(file1_contents)
    file2_contents = file2.read()
    print(file2_contents)

    new_file.write(file1_contents)
    new_file.write(file1_contents)
    print(new_file)

    file1.close()
    file2.close()
    new_file.close()

merge("file1.txt","file2.txt","newfile.txt")
