**1- Write an assert statement that triggers an `AssertionError` if the variable spam is an integer less than 10**  
**Answer:** `assert spam >= 10`

**2- Write an assert statement that triggers an `AssertionError` if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different.**  
**Answer:** `assert eggs.lower() != bacon.lower()`

**3- Write an assert statement that *always* triggers an `AssertionError`**  
**Answer:** `assert False`

**4- What are the two lines that your program must have in order to be able to call `logging.debug()`**  
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

**5- What are the two lines that your program must have in order to have `logging.debug()` send a logging message to a file named programLog.txt?**  
```python
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```
**6- What are the five logging levels?**  
**Answer:** DEBUG, INFO, WARNING, ERROR and CRITICAL.

**7- What line of code can you add to disable all logging messages in your program?**  
**Answer:** `logging.disable(logging.CRITICAL)`

**8- Why using logging messages is better than using `print()` to display the same message?**  
**Answer:** You can disable all logging messages using a single-line code and it provides a timestamp.

**9- What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?**  
**Answer:** Step Over will execute a function and stops right after it.  
Step In will stop on the first line of a function.  
Sep Out will continue the execution of the current function and stops on the first line after it.

**10- After you click Continue, when will the debugger stop?**  
**Answer:** It will continue the execution of the program till it ends or the next breakpoint.

**11- What is a breakpoint?**  
**Answer:** It's something we add to any line of code so the debugger pauses execution when It reaches it.

**12- How do you set a breakpoint on a line of code in Mu?**  
**Answer:** Just click the line's number and a red dot will appear.
