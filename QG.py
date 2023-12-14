def ask_question(question, answer, score):
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    return score

print("Welcome to my computer quiz!!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Okay! Let's Play :)")
questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("Which animal is known as the 'Ship of the Desert'? ", "camel"),
    ("How many days are there in a week? ", "7"),
    ("How many vowels are there in the English alphabet and name them? ", "5"),
    ("Which animal is known as the king of the jungle? ", "lion"),
    ("Name the National animal of India? ", "tiger"),
    ("Who designed the National Flag of India? ", "pingali venkayya"),
    ("Name the National fruit of India? ", "mango"),
    ("Name the National river of India? ", "ganga")
]

score = 0
for question, answer in questions:
    score = ask_question(question, answer, score)

print("You got", score, "questions correct!")
percentage = (score / len(questions)) * 100
print(f"You got {percentage}%.")
