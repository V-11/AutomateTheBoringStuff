import random, pyinputplus, time

CorrectAnswers = 0
randomlist1 = []
randomlist2 = []

for i in range(1,11):
    randomlist1.append(random.randint(0, 9))
    randomlist2.append(random.randint(0, 9))

    print("Question " + str(i) + ":", end=' ')
    print("What is " + str(randomlist1[i-1]) + "x" + str(randomlist2[i-1]) + "?")

    try:
        answer = pyinputplus.inputInt("Answer: ", limit=3, timeout=8)
    except pyinputplus.TimeoutException:
        print("Exceeded Allowed Time")
        continue

    if answer == (randomlist1[i-1]*randomlist2[i-1]):
        CorrectAnswers += 1
        print("Correct!")
        time.sleep(1)
    else:
        print("Incorrect")

print("Number of Correct Answers = " + str(CorrectAnswers))
print("Number of Incorrect Answers = " + str(10-CorrectAnswers))
