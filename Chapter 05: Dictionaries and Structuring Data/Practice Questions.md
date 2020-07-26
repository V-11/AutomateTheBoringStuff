**1- What does the code for an empty dictionary look like?**  
**Answer:** `items = {}`

**2- What does a dictionary value with a key 'foo' and a value 42 look like?**  
**Answer:** `items = {'foo': '42'}`

**3- What is the main difference between a dictionary and a list?**  
**Answer:** Unlike lists, items in dictionaries are unordered.

**4- What happens if you try to access spam['foo'] if spam is {'bar': '100'}**  
**Answer:** It will result a KeyError error message.

**5- If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?**  
**Answer:** `'cat' in spam` is a shorter version of writing `'cat' in spam.keys()`

**6- If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?**  
**Answer:** `'cat' in spam` will search the keys while `'cat' in spam.values()` will search the values.

**7- What is a shortcut for the following code?**  
```python
if 'color' not in spam:
  spam['color'] = 'black'
```  
**Answer:** `spam.setdefault('color', 'black')`

**8- What module and function can be used to “pretty print” dictionary values?**  
**Answer:** pprint and pprint.pprint(), respectively.
