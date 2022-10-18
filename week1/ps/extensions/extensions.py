#get a file name from user
file1 = input("File name: ")

#remove spaces and capitals
filename = file1.lower()

#check the file type:
if '.gif' in filename:
    print("image/gif")

elif '.jpg' in filename:
    print("image/jpeg")

elif '.jpeg' in filename:
    print("image/jpeg")

elif '.png' in filename:
    print("image/png")

elif '.pdf' in filename:
    print("application/pdf")

elif '.txt' in filename:
    print("text/plain")

elif '.zip' in filename:
    print("application/zip")

else:
    print("application/octet-stream")
