# Simple Quiz Game

# List of questions and answers
quiz = [
    {"question": "What is the capital of France? ", "answer": "Paris"},
    {"question": "What is 5 + 7? ", "answer": "12"},
    {"question": "What color do you get when you mix red and white? ", "answer": "Pink"},
    {"question": "What is the largest planet in our solar system? ", "answer": "Jupiter"},
]

score = 0

print("Welcome to the Quiz Game!")
print("Answer the following questions:\n")

# Loop through questions
for q in quiz:
    user_answer = input(q["question"])
    if user_answer.strip().lower() == q["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

# Final score
print(f"You got {score} out of {len(quiz)} questions correct!")
