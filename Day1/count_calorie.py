# Open  a file for reding using open command f.open()

f = open("input_calorie.txt","r")
# Reading a file and after open using read command using f.read()
sentence = f.read()
# Reading file based on blank lines using command split('\n\n')
whole_string = sentence.split('\n\n')
# Reading lines based on blank lines using for loop and it will consider
# everything as string so first we have to convert that into int using eval(i) function
# Then using sum function make a sum
gettingMaxList = []
for number in whole_string:
    # Converting each string into number and save them into new list 
    res = [eval(i) for i in number.split('\n')]
    # Making sum of each line separated based on blank lines
    gettingMaxList.append(sum(res))
print(max(gettingMaxList))

gettingMaxList.sort(reverse=True)
i=0
temp = 0
while i < 3:
    print(gettingMaxList[i])
    temp=gettingMaxList[i] + temp
    i = i + 1
print(temp)