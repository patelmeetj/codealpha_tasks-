print("Welcome to SimpleBot! (Type 'exit' to quit)")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello":
        print("Bot: Hi!")
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    elif user_input == "exit":
        print("Bot: Exiting. Have a great day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")