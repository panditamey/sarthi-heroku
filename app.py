
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import streamlit as st




st.title("""
NLP Bot  
NLP Bot is an NLP conversational chatterbot. Initialize the bot by clicking the "Initialize bot" button. 
""")



bot = ChatBot(
    'Sarthi',
)

trainer = ListTrainer(bot)
trainer.train([
    "Hi there!",
    "Hello",
])


trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

#for TesTing on cmd
# while True:
#     try:
#         bot_input = bot.get_response(input('>> '))
#         print('Bot:',bot_input)
#     except(KeyboardInterrupt,EOFError,SystemExit):
#         break

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text

user_input = get_text()
if True:
    st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)