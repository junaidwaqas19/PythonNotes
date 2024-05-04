name="Abdullah"
age =25
job="Software Developer"
person_string="The name is {}. {} is {} years old and a {}!"

print(person_string.format(name, name,age,job))

#string position with format

name="Abdullah"
age =25
job="Software Developer"
person_string="The name is {2}. {2} is {0} years old and a {1}!"

print(person_string.format(age,job,name))

#string using with pi

pi=3.141592
string_pi=f"The Value of Pi is approximately {pi:0.2}"
print(string_pi)

#string using with space

pi=3.141592
string_pi=f"The Value of Pi is approximately {pi:>20}"
print(string_pi)