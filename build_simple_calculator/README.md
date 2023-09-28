# Simple Calculator

A Python class for evaluating mathematical expressions using a custom operator precedence order.

## Introduction

The Simple Calculator Python class allows you to evaluate mathematical expressions with support for operators such as addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (**). It takes into account operator precedence and parentheses to calculate expressions correctly.

## Features

- Parses mathematical expressions with different operators.
- Supports parentheses for grouping expressions and altering operator precedence.
- Handles unary minus for negative numbers.
- Provides a clear separation of concerns with methods for parsing and evaluating expressions.

## Installation

1. Clone the repository to your local machine:

    git clone https://github.com/tsameema/PyExpressionSolver

2. Change into the project directory:

    cd simple-calculator

3. Run the calculator using Python:

    python3 main.py

## Usage
1. Import the SimpleCalculator class from the simple_calculator module.

    from simple_calculator import SimpleCalculator

2. Create an instance of SimpleCalculator by providing a mathematical expression as a string.
    
    expression = "-[2+{9-(98/32)*2}**2]" (you can add any expression that include bracket also)
    calculator = SimpleCalculator(expression)

3. Calculate the expression using the calculate_expression method.
    
    result = calculator.calculate_expression()
    print(f'Result: {round(result, 2)}')

## Methodology
### build_operator_value_stack
1. This method builds a stack of values and operators based on operator precedence.
2. It iterates through the input expression character by character.
3. Numbers are extracted and added to the values list.
5. Operators (+, -, *, /, **) are handled based on their precedence.
6. Opening and closing brackets (, {, [, ), }, ]) are processed to maintain operator precedence.
7. The final result is a list containing both numbers and operators in the order they should be evaluated.
### build_expression
1. This method evaluates the expression using the values stack.
2. It initializes an empty stack to store intermediate results.
3. Iterates through the values stack, which contains both numbers and operators.
4. For each element in the stack:
    - If it's a number, it pushes it onto the stack.
    - If it's an operator (+, -, *, /, **):
        - If it's a unary minus ('-') and there's only one element on the stack, it performs unary negation.
        - Otherwise, it evaluates the binary operation using the top two elements and pushes the result back onto the stack.
5. After processing all values, the stack should contain the final result, which is returned.
### calculate_expression
1. This method orchestrates the calculation of the expression.
2. Calls the build_operator_value_stack method to create the values stack.
3. Calls the build_expression method to evaluate the expression.
4. Returns the final result of the expression.


## Acknowledgments
Inspired by the need for a simple and customizable calculator for evaluating expressions.
Feel free to use and extend this class for your own projects!