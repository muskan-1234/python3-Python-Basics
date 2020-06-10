#Q1

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall=rainfall_mi.split(',')
num_rainy_months=0
for mon in rainfall:
    if float(mon)>3:
        num_rainy_months+=1
        
#Q2

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count=0
sent=sentence.split(' ')
for s in sent:
    if s[-1]==s[0]:
        same_letter_count+=1

#Q3

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for item in items:
    if 'w' in item:
        acc_num+=1

#Q4

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e=0
sent=sentence.split(' ')
for s in sent:
    if ('a' in s or 'e' in s):
        num_a_or_e+=1

#Q5

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels=0
for vowel in s:
    if vowel in vowels:
        num_vowels+=1

