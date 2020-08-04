**1- Does PyInputPlus come with the Python Standard Library?**  
**Answer:** No, It's a third-party module that needs to be installed whenever in need.

**2- Why is PyInputPlus commonly imported with import pyinputplus as pyip?**  
**Answer:** To make it short and easy to write when we want to call a function from that module.

**3- What is the difference between `inputInt()` and `inputFloat()`?**  
**Answer:** Returns integer number and float number, respectively.

**4- How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?**  
**Answer:** `pyinputplus.inputInt(min = 0, max = 99)`

**5- What is passed to the allowRegexes and blockRegexes keyword arguments?**  
**Answer:** List of regexes that are either allowed or blocked.

**6- What does inputStr(limit=3) do if blank input is entered three times?**  
**Answer:** It will return `RetryLimitException`

**7- What does inputStr(limit=3, default='hello') do if blank input is entered three times?**  
**Answer:** It will return `'hello'`
