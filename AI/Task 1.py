# CHATBOT WITH RULE-BASED RESPONSES
import re
def simple_chatbot(user_input):
    rules = [
        {"pattern": r"hello|hi|hey", "response": "Hello! How can I help you?"},
        {"pattern": r"how are you", "response": "I'm just a computer program, but thanks for asking!"},
        {"pattern": r"what is your name", "response": "I'm a chatbot."},
        {"pattern": r"bye|goodbye", "response": "Goodbye! Have a great day."},
        {"pattern": r"(.*)", "response": "I'm sorry, I don't understand that."},
    ]
    for rule in rules:
        pattern = re.compile(rule["pattern"], re.IGNORECASE)
        if pattern.match(user_input):
            return rule["response"]
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    if re.match(r"bye|goodbye", user_input, re.IGNORECASE):
        print("Simple Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Simple Chatbot:", response)

