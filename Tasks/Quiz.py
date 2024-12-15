def welcomeMessage():
    print("Welcome to the Python Quiz Application!")
    print("Test your knowledge by answering the following questions.\n")

def displayQuestion(question, options, correctOption):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            userAnswer = int(input("Please enter the number of your answer: "))
            if 1 <= userAnswer <= len(options):
                break
            else:
                print("Invalid option. Please choose a valid answer (1, 2, 3, or 4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    if userAnswer == correctOption:
        return 1  
    else:
        return 0  

def show_results(score, totalQuestions):
    print(f"\nYour total score is: {score}/{totalQuestions}")
    percentage = (score / totalQuestions) * 100
    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 75:
        print("Great job! You did well.")
    elif percentage >= 50:
        print("Not bad, but there's room for improvement.")
    else:
        print("Better luck next time! Keep trying.")

def thankyouMessage():
    print("\nThank you for taking the quiz! Have a great day!")

def startQuiz():

    welcomeMessage()

    questions = [
        ("What is the capital of England?", ["Manchester", "Leeds", "London", "Bristol"], 3),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
        ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
        ("Who wrote 'To Kill a Mockingbird'?", ["J.K. Rowling", "Harper Lee", "Mark Twain", "Ernest Hemingway"], 2),
        ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], 3)
    ]

    score = 0
    totalQuestions = len(questions)

    for question, options, correctOption in questions:
        score += displayQuestion(question, options, correctOption)

    show_results(score, totalQuestions)

    thankyouMessage()

if __name__ == "__main__":
    startQuiz()