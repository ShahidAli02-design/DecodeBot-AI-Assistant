import random
from datetime import datetime

# Data Storage
notes = []
tasks = []

# Quiz Questions
quiz_questions = [
    {
        "question": "What does AI stand for?",
        "answer": "a",
        "options": [
            "a) Artificial Intelligence",
            "b) Automatic Internet",
            "c) Artificial Input"
        ]
    },
    {
        "question": "Who developed Python?",
        "answer": "b",
        "options": [
            "a) Elon Musk",
            "b) Guido van Rossum",
            "c) Bill Gates"
        ]
    }
]

# Facts
facts = [
    "Honey never spoils.",
    "The Eiffel Tower can grow taller in summer.",
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts."
]

# Jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Debugging is like being a detective in a crime movie where you are also the criminal.",
    "Why was the computer cold? Because it forgot to close its Windows."
]

print("=" * 60)
print("           DECODEBOT AI ASSISTANT v2.0")
print("=" * 60)

name = input("Bot: What's your name? ")

print(f"\nBot: Welcome {name}!")
print("Bot: Type 'help' to see all commands.\n")

conversation_count = 0

while True:

    user_input = input(f"{name}: ").lower().strip()
    conversation_count += 1

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    # Name
    elif user_input == "what is my name":
        print(f"Bot: Your name is {name}.")

    # Time
    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot:", current_time)

    # Date
    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot:", current_date)

    # Calculator
    elif user_input.startswith("calc "):
        try:
            expression = user_input[5:]
            result = eval(expression)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid calculation.")

    # Joke
    elif user_input == "joke":
        print("Bot:", random.choice(jokes))

    # Fact
    elif user_input == "fact":
        print("Bot:", random.choice(facts))

    # Add Note
    elif user_input.startswith("add note "):
        note = user_input.replace("add note ", "")
        notes.append(note)
        print("Bot: Note saved successfully.")

    # Show Notes
    elif user_input == "show notes":
        if notes:
            print("Bot: Your Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
        else:
            print("Bot: No notes available.")

    # Add Task
    elif user_input.startswith("add task "):
        task = user_input.replace("add task ", "")
        tasks.append(task)
        print("Bot: Task added.")

    # Show Tasks
    elif user_input == "show tasks":
        if tasks:
            print("Bot: Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Bot: No tasks available.")

    # Quiz
    elif user_input == "quiz":

        question = random.choice(quiz_questions)

        print("\nQuestion:")
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your Answer: ").lower()

        if answer == question["answer"]:
            print("Bot: Correct Answer!")
        else:
            print("Bot: Wrong Answer.")

    # AI Info
    elif "ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It helps machines perform tasks intelligently.")

    # Python Info
    elif "python" in user_input:
        print("Bot: Python is a powerful programming language.")
        print("Bot: It is used in AI, Data Science and Web Development.")

    # Stats
    elif user_input == "stats":
        print(f"Bot: Total messages exchanged = {conversation_count}")

    # Help
    elif user_input == "help":
        print("""
================ COMMANDS ================

hello / hi / hey
what is my name
time
date

calc 10+5
calc 5*6

joke
fact

add note your_note
show notes

add task your_task
show tasks

quiz

what is ai
python

stats

bye / exit / quit

==========================================
""")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print(f"\nBot: Goodbye {name}!")
        print(f"Bot: Total interactions: {conversation_count}")
        break

    # Unknown
    else:
        print("Bot: Sorry, I don't understand that command.")
        print("Bot: Type 'help' to see available commands.")