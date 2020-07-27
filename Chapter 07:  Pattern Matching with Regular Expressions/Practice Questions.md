**1- What is the function that creates Regex objects?**  
**Answer:** `re.compile()`

**2- Why are raw strings often used when creating Regex objects?**  
**Answer:** Raw strings completely ignore all escape characters and prints any backslash that appears in the string.

**3- What does the `search()` method return?**  
**Answer:** It will return a Match object of the first matched text in the searched string.

**4- How do you get the actual strings that match the pattern from a Match object?**  
**Answer:** Using `group()` method.

**5- In the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, what does group 0 cover? Group 1? Group 2?**  
**Answer:** '415-555-4242', '415' and '555-4242', respectively.

**6- How would you specify that you want a regex to match actual parentheses and period characters?**  
**Answer:** Using backslash `\`

**7- The `findall()` method returns a list of strings or a list of tuples of strings. What makes it return one or the other?**  
**Answer:** It returns a list of strings of every match in the searched string as long as there are no groups in the regular expression.

**8- What does the `|` character signify in regular expressions?**  
**Answer:** It's called a pipe and it can be used to match one of many expressions.

**9- What two things does the `?` character signify in regular expressions?**  
**Answer:** It's used to declare a non-greedy match or to flag an optional group.

**10- What is the difference between the `+` and `*` characters in regular expressions?**  
**Answer:** The star/asterisk is used to match ***zero or more*** of a pattern group (It can be completely absent or repeated over and over again).  
The plus is used to match ***one or more*** of a pattern group (It *must* appear at least once, It's not optional like the star/asterisk).

**11- What is the difference between `{3}` and `{3,5}` in regular expressions?**  
**Answer:** `{3}` will only match if the preceding group was repeated 3 times in a string, while `{3,5}` will match if it was reapted 3, 4 or 5 times.

**12- What do the `\d`, `\w`, and `\s` shorthand character classes signify in regular expressions?**  
**Answer:** Matching a digit, word, or space character, respectively.

**13- What do the `\D`, `\W`, and `\S` shorthand character classes signify in regular expressions?**  
**Answer:** Matching anything except a digit, word, or space character, respectively.

**14- What is the difference between `.*` and `.*?`?**  
**Answer:** `.*` does a greedy match but the `.*?` does a non-greedy match.

**15- What is the character class syntax to match all numbers and lowercase letters?**  
**Answer:** `[a-z0-9]`

**16- How do you make a regular expression case-insensitive?**  
**Answer:** Add `re.IGNORECASE` as a second argument to `re.compile()`.

**17- What does the `.` character normally match? What does it match if `re.DOTALL` is passed as the second argument to `re.compile()`?**  
**Answer:** `.` matches every character but a newline but it if you passed `re.DOTALL` it will also match newline.

**18- If `numRegex = re.compile(r'\d+')`, what will `numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?**  
**Answer:** 'X drummers, X pipers, five rings, X hens'

**19- What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?**  
**Answer:** It will allow you to add whitespace and comments to the input string.

**20- How would you write a regex that matches a number with commas for every three digits?**  
It must match the following: '42', '1,234' and '6,368,745'  
It must not the following: '12,34,567' (which has only two digits between the commasand) and '1234' (which lacks commas)  
**Answer:** `re.compile(r'^\d{1,3}(,\d{3})*')`

**21- How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter.**  
It must match: 'Haruto Watanabe', 'Alice Watanabe' and 'RoboCop Watanabe'  
It must not match: 'haruto Watanabe' (where the first name is not capitalized), 'Mr. Watanabe' (where the preceding word has a nonletter character), 'Watanabe' (which has no first name) and 'Haruto watanabe' (where Watanabe is not capitalized).  
**Answer:** `re.compile(r'[A-Z][a-z]+\sWatanabe')`

**22- How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive.**  
It must match the following: 'Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.' and 'BOB EATS CATS.'  
It must not match the following: 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.' and 'Carol eats 7 cats.'  
**Answer:** `re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`
