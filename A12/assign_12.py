!git clone https://github.com/gunthercox/ChatterBot.git
# %cd ChatterBot
!pip install -e .
!pip install chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

print("HealthChatBot is ready on Google Colab!")

# Create chatbot instance and train it
health_bot = ChatBot("MediGuide")

trainer = ListTrainer(health_bot)
dialogue = [
    'Hey!',
    'Hi there! This is MediGuide. How can I help you with your health today?',
    'Hello.',
    'Greetings! Do you need any medical tips or advice?',
    'I have a fever.',
    'Make sure to stay hydrated and rest. If it persists, consult a medical professional.',
    'I feel weak.',
    'Please rest, drink fluids, and avoid overexerting yourself.',
    'What helps with a sore throat?',
    'Gargle with warm salt water and stay hydrated. If needed, consult a doctor.',
    'How can I boost my immunity?',
    'Eat nutritious food, get adequate sleep, exercise, and manage stress.',
    'How should I treat a minor burn?',
    'Cool the area with running water, apply aloe vera gel, and keep it clean.',
    'How much water is good daily?',
    'Typically, 2 to 3 liters a day, depending on your body and activity.',
    'Thanks!',
    'Happy to help. Stay well!',
    'Bye!',
    'Take care! Wishing you good health.'
]

trainer.train(dialogue)

# Basic chatbot interaction
print("Talk to MediGuide (type 'exit' to quit):\n")

while True:
    msg = input("You: ")
    if msg.lower() == 'exit':
        print("MediGuide: Take care! See you soon.")
        break
    response = health_bot.get_response(msg)
    print(f"MediGuide: {response}")

# Sentiment-enhanced version using TextBlob
!pip install textblob
import nltk
nltk.download('punkt')
from textblob import TextBlob

print("Talk to MediGuide with empathy (type 'exit' to quit):\n")

while True:
    query = input("You: ")
    if query.lower() == 'exit':
        print("MediGuide: Bye! Stay positive and healthy.")
        break

    sentiment = TextBlob(query).sentiment.polarity

    if sentiment < -0.3:
        mood = "Oh no, that sounds tough. "
    elif sentiment > 0.3:
        mood = "That's awesome to hear! "
    else:
        mood = ""

    reply = health_bot.get_response(query)
    print(f"MediGuide: {mood}{reply}")