def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is within the allowed limit
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize empty lists for the components of each row
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    # Iterate through each problem in the list
    for problem in problems:
        # Split the problem into operands and operator
        num1, operator, num2 = problem.split()

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are numeric
        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."

        # Determine the maximum length of the current operands for alignment
        max_len = max(len(num1), len(num2))

        # Create the formatted strings for each row
        first_line.append(num1.rjust(max_len + 2))
        second_line.append(operator + num2.rjust(max_len + 1))
        dash_line.append('-' * (max_len + 2))

        # Calculate and format the answer if needed
        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line.append(result.rjust(max_len + 2))

    # Join the formatted strings to create the final output
    arranged_problems = '\n'.join([*first_line, *second_line, *dash_line])

    # Add a new line for the answers if show_answers is True
    if show_answers:
        arranged_problems += '\n' + '\n'.join(answer_line)

    return arranged_problems
problems = ["32 + 698"]
output_with_answers = arithmetic_arranger(problems, show_answers=True)
print(output_with_answers)
