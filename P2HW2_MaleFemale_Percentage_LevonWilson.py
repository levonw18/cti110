# male to female percentage program 
# 9/11/18
# CTI-110 P2HW2 - Male Female Percentage
# Levon Wilson
#
males=int(input("enter the number of males in class"))
females=int(input("enter the number of females in class"))
totalstudents=males+females
malepercentage=(males/totalstudents)*100
femalepercentage=(females/totalstudents)*100
print("male percentage:"+str(malepercentage))
print("female percentage:"+str(femalepercentage))
