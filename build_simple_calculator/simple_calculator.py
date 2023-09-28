from typing import List, Union

class SimpleCalculator:
  def __init__(self, string:str):
    self.string = string
    self.operator_prec = {'+':1, '-':1, '*':2, '/':2, '**':3}

  def build_operator_value_stack(self) -> List[Union[float, str]]:
    '''
        This function calculates the operator and values stack.
        # Explanation:
        - It iterates through the input expression character by character.
        - For each character, it determines whether it's a number, operator, or bracket.
        - If it's a number, it extracts and converts it to a float, adding it to the values list.
        - If it's an operator (+, -, *, /, **), it handles its precedence and adds it to the operators list.
        - If it's an opening bracket (, {, [), it adds it to the operators list.
        - If it's a closing bracket ), }, ], it processes operators until it matches the corresponding opening bracket.
        - After processing the entire expression, it ensures that any remaining operators are added to the values list.
        - The final result is a list (values) containing both numbers and operators in the order they should be evaluated.
        
        Args:
            None

        Returns:
            values (List[Union[float, str]]): It contains both values and operators.
    '''
    operators, values = [], []
    idx = 0
    while idx < len(self.string):
      char = self.string[idx]
      if char != ' ':
        if char in "0123456789.":
          # Extract and convert numbers
          num = ""
          while idx < len(self.string) and self.string[idx] in "0123456789.":
            num += self.string[idx]
            idx += 1
          values.append(float(num))
        elif char in "+-*/":
          if char=='*' and self.string[idx+1] == '*':
                char = "**"
                idx += 1
          # Handle operators and their precedence
          while operators and (self.operator_prec[char] <= self.operator_prec.get(operators[-1], 0)):
              values.append(operators.pop())
          operators.append(char)
          idx += 1
        elif char in "({[": # Handle opening brackets
          operators.append(char)
          idx += 1
        elif char in ")}]": # Handle closing brackets
          brac_val = '(' if char == ')' else '{' if char == '}' else '['
          while operators and operators[-1] != brac_val:
            values.append(operators.pop())
          if operators and operators[-1] == brac_val:
            operators.pop()
          idx += 1
      else:
        idx += 1
    # Pop any remaining operators
    while operators:
      values.append(operators.pop())
    return values

  def build_expression(self, values: List[Union[float, str]]) -> float:
    '''
      Build and evaluate the expression using the values stack.

      # Explanation:
      - It initializes an empty stack to store intermediate results.
      - Iterates through the values stack, which contains both numbers and operators.
      - For each element in the stack:
          - If it's a number (float), it pushes it onto the stack.
          - If it's an operator (+, -, *, /, **):
              - If it's a unary minus ('-') and there's only one element on the stack, it performs unary negation.
              - Otherwise, it evaluates the binary operation using the top two elements and pushes the result back onto the stack.
      - After processing all values, the stack should contain the final result, which is returned.

      Args:
          values (List[Union[float, str]]): The list of values and operators.

      Returns:
          float: The result of evaluating the expression.
    '''
    stack = []
    for val in values:
      if isinstance(val, float):
        stack.append(val)
      elif val in "+-**/":
        if val == '-' and len(stack)==1: # Handle unary minus
          unary_operand = stack.pop()
          stack.append(-unary_operand)
        else: # Evaluate binary operations
          sec_val = stack.pop()
          first_val = stack.pop()
          stack.append(eval(f'{first_val}{val}{sec_val}'))
    return stack[0]

  def calculate_expression(self) -> float:
    '''
      Calculate the expression using the operator and values stack.

      # Explanation:
      - Calls the 'build_operator_value_stack' method to create the values stack.
      - Prints the values stack for debugging purposes.
      - Calls the 'build_expression' method to evaluate the expression.
      - Returns the final result of the expression.

      Returns:
          float: The result of evaluating the expression.
    '''
    value = self.build_operator_value_stack()
    return self.build_expression(value)