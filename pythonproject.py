import random

# List of quiz questions
questions = [
    {
        "question": "Who was the first president of kenya?",
        "choices": {
            "A": "Uhuru Kenyatta",
            "B": "Daniel Arap Moi",
            "C": "Jomo Kenyatta",
            "D": "Mwai Kibaki"
        },
        "answer": "C"
    },
    {
        "question": "When did kenya attain independence?",
        "choices": {
            "A": "1960",
            "B": "1978",
            "C": "1958",
            "D": "1963"
        },
        "answer": "D"
                },
    {
        "question": "What is 3 × 8?",
        "choices": {
            "A": "12",
            "B": "26",
            "C": "34",
            "D": "24"
        },
        "answer": "D"
    },
    {
        "question": "Which language is mainly used to style web pages?",
        "choices": {
            "A": "HTML",
            "B": "Python",
            "C": "CSS",
            "D": "Java"
        },
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean?",
        "choices": {
            "A": "Indian",
            "B": "Pacific",
            "C": "Atlantic",
            "D": "Artic"
        },
        "answer": "B"
    }
]


# Mix the order of the questions
random.shuffle(questions)

score = 0

print("WELCOME TO THE QUIZ")

# Loop through each question
for num, q in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    # Display the choices
    for letter, choice in question["choices"].items():
        print(f"{letter}. {choice}")

     # Continue asking until the user enters A, B, C or D
    while True:
        try:
            user_answer = input("Enter your answer (A, B, C or D): ").upper()

            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError

            break

        except ValueError:
            print("Invalid input. Please enter A, B, C or D.")
    
    # Check whether the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_letter = question["answer"]
        correct_choice = question["choices"][correct_letter]

        print("Incorrect.")
        print(f"The correct answer is {correct_letter}. {correct_choice}")


# Display final score
total_questions = len(questions)

print(f"Your score is {score}/{total_questions}")

#Give remarks
if score == 5:
    print("Excellent")
elif score == 4:
    print("Very Good")
elif score == 3:  
    print("Good")
elif score == 2:
    print("Nice Try")
else:
    print("Try Again")    