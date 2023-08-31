import organisms
from organisms.animals import cats
from organisms.plants.basil import print_basil

import re



a = "HelloWorld!!!"
b = re.sub(r'(?<!^)(?=[A-Z])', '_', a).lower()
c = re.sub(r'\W+', '', b)
print(c)
# ouput: hello_world

camelcase_string="HelloWorld!!!"
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camelcase_string).lower()
alphanumeric_snake_case = re.sub(r'\W+', '', snake_case_string)
print(alphanumeric_snake_case)
# ouput: hello_world

def remove_non_alphanumeric_characters(string):
    return re.sub(r'\W+', '', string)
    
def transform_camel_to_snake_case(string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return snake_case_string


camelcase_string = "HelloWorld!!!"
snake_case_string = transform_camel_to_snake_case(camelcase_string)
alphanumeric_snake_case = remove_non_alphanumeric_characters(snake_case_string)
print(alphanumeric_snake_case)
# ouput: hello_world


# bad
def transform_camel_to_snake_case(string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    alphanumeric_snake_case = re.sub(r'\W+', '', snake_case_string)
    return alphanumeric_snake_case


# Hello, I am a comment



def transorm_int_to_str(integer:int) -> str:
    return str(integer)




def calculate_volume(length:float=1, width:float=1, height:float=1) -> float:
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("height = " + str(height))
    return length * width * height