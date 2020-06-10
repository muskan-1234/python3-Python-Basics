#Q1

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores=0
for score in scores.split():
    if int(score)>=90:
        a_scores+=1

#Q2

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=''
org_list=org.split()
print(org_list)
for c in org_list:
    if c not in stopwords and c!=',':
        first_letter=c[0]
        acro+=first_letter.upper()
        print(acro)

#Q3

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acr=''
sent_list=sent.split()
print(sent_list)
for c in sent_list:
    if c not in stopwords:
        first_two_letters=c[0:2]
        acr+=(first_two_letters.upper())+'. '
   
acro=acr[:-2]
print(acro)

#Q4

p_phrase = "was it a car or a cat I saw"
r_phrase=p_phrase[::-1]
print(r_phrase)
    
#Q5

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
lst=[]
for string in inventory:
    lst=string.split(',')
    print(("The store has{} {}, each for{} USD.").format(lst[1],lst[0],lst[2]))

