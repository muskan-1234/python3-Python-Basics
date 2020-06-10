#Q1

my_str = "MICHIGAN"
for i in my_str:
    print(i)

#Q2

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(i)
for t in several_things:
    print(type(t))
    
#Q3

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for item in str_list:
    print(len(item))
    
#Q4

original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars=0
for i in original_str:
    num_chars+=1
   
#Q5
    
addition_str = "2+5+10+20"
lst=addition_str.split('+')
sum_val=0
for i in lst:
    sum_val+=int(i)

#Q6

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
lst=week_temps_f.split(',')
sum_val=0
for i in lst:
    sum_val+=float(i)
avg_temp=sum_val/len(lst)

#Q7

nums=[]
for i in range(68):
    nums.append(i)

#Q8

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list=[]
for item in original_str.split():
    num_words_list.append(len(item))

#Q9

lett=""
for i in range(7):
    lett+='b'



