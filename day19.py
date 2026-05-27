# class student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
    
#     def display(self):
#         print(self.name,self.roll)

# s1=student('tejas',23)
# s1.display()

# class student:
#     def diplay(self,name,roll):
#         print(name,roll)

# s2=student()
# s2.diplay('tejas',13)


# class company:
#     company_name='Infosys'   # this is a class variable 
#     def __init__(self,a):
#         self.name=a          # this is a instance variable.
#     def show(self):
#         print(self.company_name,self.name)

# e1=company("roju")
# e1.show()

# e2=company("suraj")
# e2.company_name="Cognizant"
# e2.show()

# class demo:

#     def show(cls):
#         print("helllo")

# demo.show()


# class mathutils:
#     def add(self, *numbers):
#         print(sum(numbers))

# m=MathUtils()

# m.add(10,20)
# m.add(10,20,30)
# m.add(10,20,30,40)


# 
# from datetime import datetime,timedelta
# # date_str="2026-04-01"
# date_str=input("Enter date(yyyy-mm-dd):")
# date_obj=datetime.strptime(date_str,"%Y-%m-%d")
# new_date=date_obj + timedelta(days=3)

# print(new_date.date())


# from datetime import datetime,timedelta
# date_str=input("inte date(yyyy-mm-dd):")
# date_obj=datetime.strptime(date_str,"%Y-%m-%d")
# new_date=date_obj + timedelta(days=7)
# print(new_date.date())


# date printing with adding three days with day also....

from datetime import datetime,timedelta

datestr="2026-04-01"
dateobj=datetime.strptime(datestr,"%Y-%m-%d")
newdate=dateobj+ timedelta(days=3)
day_name=newdate.strftime("%A")
print(day_name)
print(newdate.date())


# finding remaining days in a year........

# from datetime import datetime

# today=datetime.today()

# newy=datetime(today.year + 1,1,1)

# diff=newy-today
# print(diff.days)

# 🔹 Q3

# 👉 Input a date → print:

# Is it weekend or weekday?

# 💡 Hint:

# Saturday/Sunday → weekend

# from datetime import datetime

# datestr="2026-04-05"

# dateobj=datetime.strptime(datestr,"%Y-%m-%d")

# newdate=dateobj.strftime("%A")
# a=['Saturday','Sunday']
# b=['Monday','Tuesday','Wednesday','Thursday','Friday']
# if newdate in a:
#     print("this is a weekend")
# else:
#     print("this is weekday")



# from datetime import datetime
# datestr="2026-04-02"
# dateobj=datetime.strptime(datestr,"%Y-%m-%d")
# day=dateobj.weekday()
# if day>=5:
#     print("weekend")
# else:
#     print("weekday")

# Find the difference in days

# from datetime import datetime
# date1="2026-09-02"
# date2="2026-05-02"
# dateobj1=datetime.strptime(date1,"%Y-%m-%d")
# dateobj2=datetime.strptime(date2,"%Y-%m-%d")
# diff=abs((dateobj2-dateobj1).days)
# print(diff)


# finding the next sunday

# from datetime import datetime,timedelta
# d="2026-05-04"
# dobj=datetime.strptime(d,"%Y-%m-%d")
# dad=6-dobj.weekday()
# print(dad)
# next_sunday = dobj + timedelta(days=dad)
# print(next_sunday)
# print(next_sunday.date())

