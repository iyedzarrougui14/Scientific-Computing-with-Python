def arithmetic_arranger(problems, show_ans=False):
  # Initialize a string to store the arranged problems
  arranged_problems = ""
  # Initialize a variable to store the number of problems
  num_problems = len(problems)
  # Check if the number of problems is more than 5
  if num_problems > 5:
    return "Error: Too many problems."
  # Initialize a variable to store the length of the longest operand
  longest_operand = 0
  # Iterate through each problem in the list
  for problem in problems:
    # Split the problem into operands and operator
    operands = problem.split("+") if "+" in problem else problem.split("-")
    operator = "+" if "+" in problem else "-"
    # check if the operator is not '+' or '-'
    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."
    # check if the operands contain any non-digit characters
    if not problem.replace("+", "").replace("-", "").replace(" ",
                                                             "").isdigit():
      return "Error: Numbers must only contain digits."
    # check if the operands are more than 4 digits wide
    if len(operands[0]) > 4 or len(operands[1]) > 4:
      return "Error: Numbers cannot be more than four digits."
    # update the length of the longest operand
    longest_operand = max(longest_operand, len(operands[0]), len(operands[1]))
  # Iterate through each problem again
  for problem in problems:
    # Split the problem into operands and operator
    operands = problem.split("+") if "+" in problem else problem.split("-")
    operator = "+" if "+" in problem else "-"
    # Add the first operand to the arranged_problems string
    arranged_problems += operands[0].rjust(longest_operand) + "    "
    # Add the operator and the second operand to the arranged_problems string
    arranged_problems += operator + " " + operands[1].rjust(longest_operand -
                                                            1)
    if show_ans:
      # Add the result
      arranged_problems += " = " + str(eval(problem))
    # Add a new line character
    arranged_problems += "\n"
    arranged_problems += "-" * (longest_operand + len(operator) +
                                (longest_operand - 1) +
                                (3 if show_ans else 0)) + "    "
  return arranged_problems[:-4]
