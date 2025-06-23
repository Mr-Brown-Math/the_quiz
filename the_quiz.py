print("Hello beutiful soul! I am happy to see you here.\n"
      "The following quiz is a personality quiz.\n"
      "It's based on the Quad Squad, so it's pretty exclusive.\n\n")



starter = input("Do you want to do this quiz? (yes/no): ").lower()

if starter == "yes":
    print("Great!\n")
    q1 = input("First question: Do you believe that you are a good person? (yes/no): ").lower()
    q2 = input("Question Two: Is your religion a big part of your life (yes/no): ").lower()
    q3 = input("Question 3: Do you have main character energy? (yes/no): ").lower()
    q4 = input("Last one: Given the chance, would you fire a rocket launcher? (yes/no): ").lower()

    if q1 == "yes" and q2 == "yes" and q3 == "yes":
        print("Whether you like it or not, you are Nathan!")
    if q1 == "yes" and q2 == "yes" and q3 == "no":
        print("You are now Erin! hope that is okay with you!")
    if q1 == "yes" and q2 == "no":
        print("That is Lilly! You are Lilly now!")
    if q1 == "no" and q2 == "yes":
        print("I recognize Erin anywhere! You are Erin!")
    if q1 == "no" and q2 == "no" and q3 == "yes":
        print("You are Benjamin!!!")
    if q1 == "no" and q2 == "no" and q3 == "no" or q4 == "no":
        print("Sorry, you're not a regular member of the Quad Squad.")

elif starter == "no":
    print("That is no problem. Have a great day!")
else:
    print("Sorry, I don't understand your answer.") 
