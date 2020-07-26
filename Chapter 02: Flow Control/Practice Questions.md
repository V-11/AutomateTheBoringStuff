**1- What are the two values of the Boolean data type? How do you write them?**  
**Answer:** True and False.

**2- What are the three Boolean operators?**  
**Answer:** and, or, not.

**3- Write out the truth tables of each Boolean operator.**  
**Answer:** You can find them [here](https://www.youtube.com/watch?v=hIIWS_q8V4g&feature=emb_logo).

**4- What do the following expressions evaluate to?**  
`(5 > 4) and (3 == 5)`  
False  
`not (5 > 4)`  
False  
`(5 > 4) or (3 == 5)`  
True  
`not ((5 > 4) or (3 == 5))`  
False  
`(True and True) and (True == False)`  
False  
`(not False) or (not True)`  
True

**5- What are the six comparison operators?**  
**Answer:** ==, !=, <, <=, >, >=

**6- What is the difference between the equal to operator and the assignment operator?**  
**Answer:** Equal Operater ==, Assignment Operator =

**7- Explain what a condition is and where you would use one.**  
**Answer:** A condition is a flow-control statement which will always evaluate to a Boolean value.

**9- Write code that prints Hello if 1 is stored in spam, Howdy if 2 is stored in spam, and Greetings! if anything else is stored in spam.**  
```python
spam = int(input())
if (spam == 1):
  print('Hello')
elif (spam == 2):
  print('Howdy')
else:
  print('Greetings!')
```

**10- What keys can you press if your program is stuck in an infinite loop?**  
**Answer:** ctrl + c

**11- What is the difference between *break* and *continue?***  
**Answer:** The execution immediately exits the loop’s clause when it reaches a *break* statement but jumps back to the start of the loop and reevaluates the loop’s condition when it reaches a *continue* statement.

**12- What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?**  
**Answer:** They all are the same in these cases.

**13- Write a program that prints the numbers 1 to 10 using a for loop then write an equivalent program using a while loop.**  
```python
for i in range(1, 11):
  print(i)
```
```python
i = 1
while i<11:
  print(i)
  i+=1
```

**14- If you had a function named bacon() inside a module named spam, how would you call it after importing spam?**  
**Answer:** spam.bacon()
