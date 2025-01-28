d={'class': {"A":34,"B":5,"C":5}  }
print(d["class"]['A'])
# https://www.cybrary.it/

jumbled_list=[ ['oongoam','angom','mmanggo'],
              ['orrrngea','rangeo','oorange' ],
              ['anabaa','baanaaa','ananab']
]
correct_list=['mango','orange','banana']

for i in range(len(correct_list)):
    correct_item=correct_list[i]
    sublist= jumbled_list[i]
    for item in sublist:
        if len(correct_item)==len(item):
            print(correct_item,item)
            break
