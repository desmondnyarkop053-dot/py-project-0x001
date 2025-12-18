try:
    age=int(input('Age:'))
    print(age)
except ValueError:
    print('Invalid value')

print("hello world")


name=input('Name:')
age=int(input('Age:'))
score=float(input('Score:'))
subject=input('Subject:')
school=input('School:')
country=input('Country:')
print(f'Hello {name}, you are {age} years old, your score in {subject} is {score}, you study at {school} in {country}.')
