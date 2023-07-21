import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_JOKE = "Why don't scientists trust atoms? Because they make up everything!"
R_WEATHER = "The weather is unpredictable, but you can check a reliable weather website or app for the latest forecast."
R_FACT = "Did you know that the world's population is over 7.9 billion people?"
R_FEELINGS = "I'm just a bot, so I don't have feelings. But I'm here to chat with you!"
R_GREETINGS = "Hey there! How can I assist you today?"
R_HELP = "Sure, I'd be happy to help. What do you need assistance with?"
R_THANKS = "You're welcome! If you have any more questions, feel free to ask."
R_COLORS = "I don't see colors since I'm a bot, but I can help you with any questions you have!"
R_BOOKS = "I'm a bot, so I don't read books. But I can provide information on various topics!"
R_MOVIES = "As a bot, I don't watch movies. However, I can answer questions or recommend films to you!"
R_SPORTS = "I'm not into sports as I'm a bot, but I can provide information or discuss sports topics with you!"
R_MUSIC = "I may not have ears to enjoy music, but I can certainly talk about music genres and artists!"
R_ART = "Art's are certainly a good thing do you know picasso?"
R_POLITICS = "I certaily know thigs about politics but it's a sensitive topic everyone has their own point of view on this.Do you have something else to ask ?"
R_POPULATIONI = "The poplation of India is 140 crore it's pretty high isn't it?"
R_POPULATIONW = "The population of the world is 788.84 crores,it seems that it will grow more in the coming years"
R_INDIA = "India is a culturally diverse country with a rich history, vibrant traditions, and a growing economy, known for its iconic landmarks, religious diversity, and abundant wildlife."
R_WHO = "I am a chatbot simply i answer your question as my developer has feeded me."
R_CAPABLE = "i can reply with your simple query tell me how can i assist you?"
R_RELIGION = "i don't have any religion i am a simple bot made to answer simple queres of users, tell me if there is something on which i can assist you?"
R_INTERESTING = "DO you know know Antarctica has enough snow that it can submerge 5 Burj Khalifa?"
R_Thanks = "Is there something else where i can assist you?"
R_FINE = "Good to see.Is there something else where i can assist you"
R_SLLEPING = "haha! I Don't Sleep i am a machined trained on data!"

def unknown():
    response = [
        "Could you please rephrase that?",
        "I'm not sure I understand. Can you provide more context?",
        "I'm sorry, I don't have the information you're looking for.",
        "I'm still learning, so I might not have the answer. Is there anything else I can help with?",
        "I'm afraid I can't assist with that. Is there anything else you'd like to talk about?"

    ][random.randrange(5)]
    return response
