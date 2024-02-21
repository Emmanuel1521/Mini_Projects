import re
import nltk
from nltk.chat.util import Chat, reflections

# Define reflections for pronouns replacement
reflections = {
    "I am": "you are",
    "I was": "you were",
    "I": "you",
    "I'm": "you're",
    "I'd": "you would",
    "I've": "you have",
    "I'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define symptom checking patterns and responses
symptom_patterns = [
    (r'my (.*) hurts', ["I'm sorry to hear that. Can you describe the pain in more detail?"]),
    (r'I have a fever', ["It's important to monitor your temperature. Have you taken any medication?"]),
    (r'I feel (\w+)', ["Feeling {} can indicate various health issues. It's best to consult a doctor for proper diagnosis."]),
    (r'I cough a lot', ["Persistent coughing can be a symptom of respiratory issues. It's advisable to consult a doctor for evaluation."]),
    (r'I have a headache', ["Headaches can have various causes. Have you been under a lot of stress lately?"]),
    (r'I feel dizzy', ["Dizziness can be caused by various factors such as dehydration or inner ear problems. Please sit down and rest."]),
    (r'I have a sore throat', ["Sore throat can be a symptom of a viral infection. Gargling with warm salt water may help alleviate discomfort."]),
]

# Define general health tips
health_tips = [
    "Drink plenty of water throughout the day to stay hydrated.",
    "Eat a balanced diet rich in fruits, vegetables, and whole grains.",
    "Exercise regularly to maintain a healthy body and mind.",
    "Get enough sleep each night to allow your body to rest and rejuvenate.",
    "Avoid smoking and limit alcohol consumption for better overall health.",
    "Practice good hand hygiene by washing your hands frequently, especially before eating or touching your face.",
    "Limit your intake of processed foods, sugary snacks, and beverages high in added sugars.",
    "Stay physically active by incorporating activities you enjoy into your daily routine, such as walking, cycling, or dancing.",
]

# Create a chatbot instance
chatbot = Chat(symptom_patterns, reflections)

def respond(input_text):
    response = chatbot.respond(input_text)
    if not response:
        response = "I'm sorry, I'm not sure how to respond to that."
    return response

def get_health_tips(input_text):
    return "\n".join(health_tips)

# Main interaction loop
print("Welcome to the Health Assistant Chatbot. How can I assist you today?")
while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        print("Thank you for using the Health Assistant Chatbot. Goodbye!")
        break
    elif re.search(r'health tips|tips', user_input):
        print(get_health_tips(user_input))
    else:
        print("Bot:", respond(user_input))
