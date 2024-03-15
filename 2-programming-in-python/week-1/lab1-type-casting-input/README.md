# Lab Instructions: Type Casting Input

In this lab you will be presented with three exercises to demonstrate how explicit type casting can be.  
used to solve data being inputted from an end user. Each exercise will ask you to solve a particular problem relating to types.

> ### Tips: Before you Begin
>
> #### To view your code and instructions side-by-side, select the following in your VSCode toolbar
>
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column.
> - Great work! You can now see instructions and code at the same time.
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
>
> #### To run your Python code
>
> - Select your Python file in the Visual Studio Code file tree
> - You can right click the file and select "Run Python File in Terminal"
>   or run the file using the smaller
    play button in the upper right-hand corner
>   of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.

## There are two exercises and objectives of this activity

- **Exercise 1:** Use explicit casting to apply the correct cast type

- **Exercise 2:** Fix the script so it correctly outputs the bill total

## Exercise 1

In this exercise, you'll use explicit casting to apply the correct cast type.

```python
# Using explicit type conversion, change the following
# inputs so the types match with the following below
#
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
name = input("What is your name? ")

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
age = int(input("What is your age? "))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input("What is your height in meters? "))

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty = bool(input("Are you part of our loyalty program? "))

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
```

### Instructions

1. Open the script exercise1.py present inside the project folder

2. To run the script, open terminal and execute the following command:

    ```bash
    python3 exercise1.py
    ```

3. Step 3: Fix the script so the variables have the correct type.

## Exercise 2

Your goal of this exercise is to fix the script so that each variable has the correct type.

```python
# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
coffee = input("1 coffee @: $ ")

# Modify the line below
sandwich = input("1 sandwich @: $ ")

# Modify the line below
cake = input("1 cake @: $ ")

bill_total = coffee + sandwich + cake

print("Your total bill is $".format(bill_total))
```

### Instructions

1. Open the script exercise2.py present inside the project folder

2. To run the script, open terminal and execute the following command.  You will be prompted to enter some values.

    ```bash
    python3 exercise2.py 
    ```

3. Fix the script so it outputs the correct bill total based on the data being entered.

## Final Step: Let's submit your code

Nice work! To complete this assessment:

- Save your file through File -> Save
- Select "Submit Assignment" in your Lab toolbar.

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
