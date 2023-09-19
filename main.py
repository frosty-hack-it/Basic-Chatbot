import random
import nltk
from nltk.tokenize import word_tokenize

# Define greetings and responses
greetings = ["hello", "hi", "hey", "howdy"]
responses = ["Hello!", "Hi there!", "Hey!", "How can I help you today?"]

def basic_chatbot(user_input):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())

    # Check for greetings in the user input
    if any(word in tokens for word in greetings):
        return random.choice(responses)
    else:
        return "I'm sorry, I don't understand that. Please try again."

if __name__ == "__main__":
    print("Basic Chatbot: Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Basic Chatbot: Goodbye!")
            break
        response = basic_chatbot(user_input)
        print("Basic Chatbot:", response)