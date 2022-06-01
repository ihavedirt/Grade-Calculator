#calculates current grade based on evaluations currently in effect
#IDEAS: give highest possible grade scenarios?
#     : calc grade based on target final grade

# enter category and weight
# enter marks with same denoms
    # input denom
    # input individual marks
    # automatically adjust grade based on weight(percent and out of category weight)
# enter marks with different denoms
    # input num and denom
    # 

#ask if user wants to add another category

# def commonDenom():

#     return

# def uncommonDenom():

#     return

# ask = 'y'

# grade = {}

# #main

# while ask == 'y':
#     category = input('Enter name of category: ')
#     grade.update({category: ''})
#     denom = str(input('Do the grades have common denominators?(y/n): '))
#     if denom == 'y'

#     else:



#     ask = str(input('Add another category?(y/n):'))


# print(grade)


total = { 'assignment' : { 'weight' : 40,
                            'grades' : [[19,20],
                                        [26,31],
                                        [16,16],
                                        [34,34],
                                        [23,23],
                                        [25,25],
                                        [16,20],
                                        [26,28]
                                        ]},
         'lab' : { 'weight' : 10,
                    'grades' : [[100,100],
                                [100,100],
                                [100,100],
                                [100,100],
                                [100,100],
                                [100,100],
                                [100,100],
                                [87.5,100],
                                [100,100],
                                [100,100]
                                ]},
         'quiz' : { 'weight' : 24,
                    'grades' : [[9,10],
                                [10,10],
                                [10,10],
                                [10,10],
                                [9,10],
                                [10,10],
                                [10,10],
                                [10,10],
                                [10,10],
                                [9,10]
                                ]}
}

# sum marks, sum denoms, multiply by weight
# add all together, divide by sum of weight
category = ['assignment', 'lab', 'quiz']
numSum = 0
denomSum = 0
totGrade = 0
weightSum = 0

#goes through each category added to the dict
for j in category:
    #for each category, look at each grade and sum mark and sum denominator
    for i in total[j]['grades']:
        numSum += i[0]
        denomSum += i[1]
    #calc grade for category, returns a mark based on the weight of category
    catGrade = numSum/denomSum*total[j]['weight']
    #return total summed grade for all considered categories
    totGrade += catGrade
    #return sum of all category's weights
    weightSum += total[j]['weight']

mark = totGrade/weightSum * 100

print(mark)


