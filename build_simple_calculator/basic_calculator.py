from simple_calculator import SimpleCalculator


if __name__ == "__main__":
  string = "2+9-98/32*2**2"
  calculator = SimpleCalculator(string)
  value = calculator.calculate_expression()
  print(f'Expression : {string}\nSolution : {round(value, 2)}')

