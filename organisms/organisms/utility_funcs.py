import organisms
from organisms.animals import cats
from organisms.plants.basil import print_basil

import re



a = "HelloWorld!!!"
b = re.sub(r'(?<!^)(?=[A-Z])', '_', a).lower()
c = re.sub(r'\W+', '', b)
print(c)


camelcase_string="HelloWorld"
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camelcase_string).lower()
alphanumeric_snake_case = re.sub(r'\W+', '', snake_case_string)
print(snake_case_string)