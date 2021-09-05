***IF ELSE STATEMENT***

**Q1**


length=5
breadth=10

area=length*breadth
peri=2*(length+breadth)

if area>peri:
  print("Area is greater",area)
else:
  print("Perimeter is greater",peri)

"""**Q2**"""

a=25
b=34
c=45

if a>b and a>c:
  print("Age of the first person",a," is greater")
elif b>c:
  print("Age pf the Second person",b," is greater")
else:
  print("Age of the Third person",c,"is greater")

"""**Q3**"""

a=int(input("Enter the age "))

if a<18:
  print("Minors who are not eligible to work")
elif a>=18 and a<60:
  print("Eligible to work")
elif a>=60:
  print("Too old to work as per govt regulation")

"""**Q4**"""

vowels=input("Enter the input ")
if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u' or vowels == 's':
  print(vowels,"is vowel")
elif vowels == 'A' or vowels == 'E' or vowels == 'I' or vowels == 'O' or vowels == 'U' or vowels == 'S':
  print(vowels,"is vowel")
else:
  print(vowels,"is consonant")

"""**Q5**"""

salary=int(input("Enter the salary "))
year=int(input("Enter the years "))


if year>=5:
  per =salary*0.05
  salary =per+salary
  print(salary)
else:
  print(salary)
