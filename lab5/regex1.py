#with my samples 

#ex1
import re
def match_pattern(text):
    return bool(re.match('a*b', text))
input_string = input()
if match_pattern(input_string):
    print("The string matches")
else:
    print("The string does NOT match")

#ex2
import re
def match_pattern(text):
    pattern = r'ab{2,3}'
    return bool(re.match(pattern, text))
s= input()
if match_pattern(s):
    print("The string matches")
else:
    print("The string does NOT match")

#ex3
import re
def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)
test_text = "It_is_a_text_that_i_am_trying_to_check."
sequences = find_sequences(test_text)
print("Sequences found:", sequences)

#ex4
import re
def find_sequences(text):
    return re.findall(r'[A-Z][a-z]+', text)
test_text = "This is Text that i am Trying to Check."
sequences = find_sequences(test_text)
print("Found:", sequences)

#ex5
def match_pattern(text):
    return text.startswith('a') and text.endswith('b')
input_string = input()
if match_pattern(input_string):
    print("The string matches")
else:
    print("The string does not match")

#ex6
def colon(text):
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')
text = input()
output = colon(text)
print("Original text:", text)
print("New text:", output)

#ex7
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel= words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel

snake = str(input())
camel = snake_to_camel(snake)
print("Camel: ", camel)

#ex8
import re
def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)
input_string = input()
result = split_at_uppercase(input_string)
print("Result:", result)

#ex9
import re
def InsertSpaces(text):
    result = re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)
    return result
text = "ExampleOfInsertSpaces"
new_text= InsertSpaces(text)
print(new_text)

#ex10
def camel_to_snake(text):
    snake_case = ''
    for char in text:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case
camel_case_string = "HelloWorld"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)





