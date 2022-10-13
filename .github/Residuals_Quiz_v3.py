#This is a simple checkpoint statistics quiz to be administered to my high school statistics class that I teach.

question1 = """What is a residual? How do you calculate a residual?  
a : The difference between the predicted value of y and the actual value of y.
b : The difference between the actual value of y and the predicted value of y."""

print(question1)

answer1_user = input("Enter the lowercase letter of the correct answer for question 1: ")

answer1_actual = "b"

print(answer1_user)

print(answer1_actual)

if answer1_actual == answer1_user:
    print("Yes, you are correct! A residual is simply the difference between the actual and predicted value of the response variable. This is the distance between the data point on the scatter plot and the LSRL.")

if answer1_actual != answer1_user:
    print("Your answer is incorrect! Study harder and try again!")
    
  

  
question2 = """What does it mean if the residual is negative?
a: The slope of the regression line is negative.
b: The slope of the regression line is positive.
c: The actual value of y was less than the predicted value of y.
d: The predicted value of y was less than the actual value of y. """

print(question2)

answer2_user = input("Enter the lowercase letter of the correct answer for question 2: ")

answer2_actual = "c"

print(answer2_user)

print(answer2_actual)

if answer2_actual == answer2_user:
    print("Yes, you are correct! If a residual is negative, the actual data point is lower than (or less than) the predicted value on the LSRL.")

if answer2_actual != answer2_user:
    print("No, you are incorrect! Review your notes and try again next time!")





question3 = """In a residual plot, we plot the _______________ on the horizontal axis and the ______________ on the vertical axis.
a: explanatory variable, residuals
b: residuals, explanatory variable
c: residuals, response variable
d: explanatory variable, response variable"""

print(question3)

answer3_user = input("Enter the lowercase letter of the correct answer for question 3: ")
#break()
answer3_actual = "a"

print(answer3_user)

print(answer3_actual)

if answer3_actual == answer3_user:
    print("Yes, you are correct!")

if answer3_actual != answer3_user:
    print("No, you are incorrect! Please pay more attention in class next time.")
    
    

question4 = """In a residual plot, the presence of a discernible pattern means that:
a: the residual plot is appropriate because a line of best fit can be drawn.
b: the residual plot is not appropriate because only standard error should remain."""

print(question4)

answer4_user = input("Enter the lowercase letter of the correct answer for question 4: ")

answer4_actual = "b"

print(answer4_user)

print(answer4_actual)

if answer4_actual == answer4_user:
    print("Yes, you are correct! You have mastered residual plots!")

if answer4_actual != answer4_user:
    print("No, you are not correct. Consider staying after class for some helpful tutoring!")
    
    


#This code is used to calculate the cumulative quiz score.
if answer1_actual == answer1_user:
    score1 = 5
    
if answer1_actual != answer1_user:
    score1 = 0



if answer2_actual == answer2_user:
    score2 = 5
    
if answer2_actual != answer2_user:
    score2 = 0
    
    
    
if answer3_actual == answer3_user:
    score3 = 5
    
if answer3_actual != answer3_user:
    score3 = 0
    
    
    
    
if answer4_actual == answer4_user:
    score4 = 5
    
if answer4_actual != answer4_user:
    score4 = 0

cumulative_score = str(score1 + score2 + score3 + score4)

print("Your total score for this quiz is " + cumulative_score + " points out of 20 possible earned points.")

input()




