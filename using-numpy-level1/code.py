# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data_file=path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
age=np.array(census[:,:1])
print(age)
max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]
x=[]
for i in census:
    if i[2]==0:
        race_0.append(i)
    elif i[2]==1:
        race_1.append(i)
    elif i[2]==2:
        race_2.append(i)
    elif i[2]==3:
        race_3.append(i)
    elif i[2]==4:
        race_4.append(i)
race_1=np.asarray(race_1)
race_2=np.asarray(race_2)
race_3=np.asarray(race_3)
race_4=np.asarray(race_4)
race_0=np.asarray(race_0)


len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

x.append(len_0)
x.append(len_1)
x.append(len_2)
x.append(len_3)
x.append(len_4)

y=min(x)

if y==len(race_0):
    minority_race=0
elif y==len(race_1):
    minority_race=1
elif y==len(race_2):
    minority_race=2
elif y==len(race_3):
    minority_race=3
elif y==len(race_4):
    minority_race=4

print(minority_race)



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]

w=senior_citizens[:,6]

working_hours_sum=sum(w)


print(working_hours_sum)
senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
count=0
count1=0
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=(high[:,7]).mean()
print(avg_pay_high)

avg_pay_low=(low[:,7]).mean()
print(avg_pay_low)



