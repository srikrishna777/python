eng=float(input("Enter English marks:"))
math=float(input("Enter Math marks:"))
comp=float(input("Enter Computer Science marks:"))
phy=float(input("Enter Physics marks:"))
chem=float(input("enter Chemistry marks:"))

total=eng+math+comp+phy+chem
average=total/5
percentage=(total/500)*100

print("Total Mark=",total)
print("Average Marks=",average)
print("Marks Percentage=",percentage)

