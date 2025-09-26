import random

random_replies = ["Oh really?", "Are you sure about that?", "Perhaps…", "I don’t think so",
                  "Interesting!", "Tell me more!", "Why do you think so?", "Hmm..."]

chat_dict = {
    "happy": "I'm happy today too",
    "sad": "Be happy, life is good",
    "computer": "Computers will take over the world!",
    "school": "Learning is important!",
    "hungry": "You should eat something tasty!",
    "weather": "The weather can change quickly.",
    "love": "Love makes the world go round."
}

def dictionary_check(message):
    message = message.lower()
    user_words = message.split()
    smart_replies = []
    for word in user_words:
        if word in chat_dict:
            answer = chat_dict[word]
            smart_replies.append(answer)
    if smart_replies:
        reply_chosen = random.randint(1, len(smart_replies)) - 1
        return smart_replies[reply_chosen]
    else:
        return ""

print("What would you like to talk about?")
user_says = ""
while user_says != "bye":
    user_says = ""
    while user_says == "":
        user_says = input("Talk to me: ")
    smart_response = dictionary_check(user_says)
    if smart_response:
        print(smart_response)
    else:
        reply_chosen = random.randint(1, len(random_replies)) - 1
        print(random_replies[reply_chosen])
        random_replies[reply_chosen] = user_says
print("Goodbye. Thanks for chatting today!")
