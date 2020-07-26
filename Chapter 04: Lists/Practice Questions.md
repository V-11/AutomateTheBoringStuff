**1- What is []?**  
**Answer:** It's an empty list that contains no values.

**2- How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Spam contains [2, 4, 6, 8, 10])**  
**Answer:** spam[2] = 'hello'

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd']  
**3- What does spam[int(int('3' * 2) // 11)] evaluate to?**  
**Answer:** d

**4- What does spam[-1] evaluate to?**  
**Answer:** d

**5- What does spam[:2] evaluate to?**  
**Answer:** ['a', 'b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True]  
**6- What does bacon.index('cat') evaluate to?**  
**Answer:** 1

**7- What does bacon.append(99) make the list value in bacon look like?**  
**Answer:** [3.14, 'cat', 11, 'cat', True, 99]

**8- What does bacon.remove('cat') make the list value in bacon look like?**  
**Answer:** [3.14, 11, 'cat', True]

**9- What are the operators for list concatenation and list replication?**  
**Answer:** '+' for concatenation and '*' for replication.

**10- What is the difference between the append() and insert() list methods?**  
**Answer:** The append() method adds the argument to the end of the list while the insert() method can insert a value at any index in the list.

**11- What are two ways to remove values from a list?**  
**Answer:** Using the remove() and del() methods.  
The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you know the value you want to remove from the list.

**12- Name a few ways that list values are similar to string values.**  
**Answer:**  
1- They both hold values.  
2- String values are typed with quote characters to mark where the string begins/ends while a list begins with an opening square bracket and ends with a closing square bracket.  
3- They both share a common set of operations (Indexing, Length, Loops, Slicing, .....).  
4- They both are objects so they share built-in methods.  

**13- What is the difference between lists and tuples?**  
**Answer:** Tuples, like strings, are immutable (They cannot have their values modified, appended, or removed).

**14- How do you type the tuple value that has just the integer value 42 in it?**  
**Answer:** tuple = ('42')

**15- How can you get the tuple form of a list value? How can you get the list form of a tuple value?**  
**Answer:** Using tuple() and list() functions, respectively.

**16- Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?**  
**Answer:** References to the lists.

**17- What is the difference between copy.copy() and copy.deepcopy()**  
**Answer:** *copy.copy()* function can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.  
If the list you need to copy contains lists then *copy.deepcopy()* function will copy these inner lists as well.
