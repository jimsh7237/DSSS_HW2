import random

def generate_integer(min_value, max_value):
    """Returns a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

def random_operator():
    """Returns a randomly selected operator ('+', '-', '*')."""
    return random.choice(['+', '-', '*'])

def create_problem(num1, num2, operator):
    """
    Creates a math problem and calculates the answer.
    
    Returns:
        tuple: (problem as string, correct answer)
    """
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    return f"{num1} {operator} {num2}", answer

def math_quiz():
    """Runs a simple math quiz with random problems."""
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("Solve the math problems to earn points.")

    for _ in range(total_questions):
        n1 = generate_integer(1, 10)
        n2 = generate_integer(1, 5)
        op = random_operator()

        problem, correct_answer = create_problem(n1, n2, op)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
