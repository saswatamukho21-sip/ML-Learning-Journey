lst=[1,2,3,4,5,6]

with open("input.txt","w") as file:
    for i in lst:
        file.write(f"{i}\n")

with (open("input.txt", "r") as file,
      open("odd.txt", "w") as ofile,
      open("even.txt", "w") as efile):
    for line in file:
        num = int(line.strip())
        if num % 2 == 0:
            efile.write(f"{num}\n")
        else:
            ofile.write(f"{num}\n")
           
