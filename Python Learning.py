import spacy

regions=['Asia','Africa']
print(regions[0])
print('Assignment 1 Completed!!')
my_list=[]
my_list.append('Pay Bills')
my_list.append('Tidy Up')
my_list.append('Walk the dog')
my_list.append('Go to the pharmacy')
my_list.append('Cook Dinner')
from collections import deque
queue=deque(my_list)
queue.append('Wash the Car')
print(queue.popleft(),'- Done!')
my_list_upd=queue
i=0
while i<my_list_upd.__len__():
    print(my_list_upd[i])
    i=i+1
print('Assignment 2 Completed!!')

my_list=[]
my_list.append('Pay Bills')
my_list.append('Tidy Up')
my_list.append('Walk the dog')
my_list.append('Go to the pharmacy')
my_list.append('Cook Dinner')

stack=[]
for task in my_list:
    stack.append(task)
while stack:
    print(stack.pop(),'- Done!')
print('\n Stack is empty')
print('\n Assignment 3 completed!!')

txt='List is a Ubiquitious data structure in the python programming language'

nlp=spacy.load('en_core_web_sm')
doc=nlp(txt)

stk=[]
count=0
i=0
for w in doc:
    #print(w)
    count=count+1
    if w.pos_=='NOUN' or w.pos_=='PROPN':
        stk.append(w.text)
        
    elif (w.head.pos_=='NOUN' or w.head.pos_=='PROPN') and (w in w.head.lefts):
        stk.append(w.text)
        
chunk=''
while stk:
    i=i+1
    chunk=stk.pop()+' '+chunk
print(chunk.strip())
#print(w.text)


    # print(chunk.strip())
print('Assignment 4 Completed!!!')

txt=''' Python is one of the most promising programming languages today. Due to the simplicity of Python Syntax, many researchers and scientists prefer Python over many other languages.'''
txt=txt.replace('.','').replace(',','')
lst=txt.split()
print(lst)
dct={}
for w in lst:
    c=dct.setdefault(w,0)
    dct[w]+=1
print(dct)
dct_sorted=dict(sorted(dct.items(),key=lambda x: x[1],reverse=True))
print(dct_sorted)