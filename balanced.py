# Enter your code here. Read input from STDIN. Print output to STDOUT

#balanced
# Enter your code here. Read input from STDIN. Print output to STDOUT

inputString = str(input())
#print(inputString)
    # The stack to keep track of opening brackets.
stack = []
res = []

    #hashMap for
mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
for char in inputString:

    # If the character is an closing bracket
    if char in mapping:
        top_element = stack.pop() if stack else '#'
        if mapping[char] != top_element:
            res.append('N')
            break
    elif char == '(' or char == '{' or char =='[':
        #opening bracket, push it onto the stack.
        stack.append(char)

# if res length is 0 then didnt break from the for loop
if len(res) == 0:
    # if stack empty, matching parantheses
    if len(stack) == 0:
        res.append('Y')
    else:
        res.append('N')
res.append(' ')

for char in inputString:
    if char in mapping or char == '(' or char =='{' or char == '[':
        res.append(char)

print(''.join(res))
