import tkinter as tk
import random
import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat','eating'])
    response(long.R_JOKE, ['tell', 'joke'], required_words=['joke'])
    response(long.R_WEATHER, ['what', 'weather'], required_words=['weather'])
    response(long.R_FACT, ['tell', 'fact'], required_words=['fact'])
    response(long.R_FEELINGS, ['how', 'you', 'feel','feeling'], required_words=['you', 'feel'])
    response(long.R_GREETINGS, ['hey', 'hello', 'hi', 'greetings'], single_response=True)
    response(long.R_HELP, ['help', 'assist'], required_words=['help'])
    response(long.R_THANKS, ['thank', 'thanks'], single_response=True)
    response(long.R_COLORS, ['colors','color'], required_words=['colors','color','colour'])
    response(long.R_BOOKS, ['books'], required_words=['books'])
    response(long.R_MOVIES, ['movies'], required_words=['movies'])
    response(long.R_SPORTS, ['sports'], required_words=['sports'])
    response(long.R_MUSIC, ['music'], required_words=['music'])
    response(long.R_ART, ['art'], required_words=['art'])
    response(long.R_POLITICS, ['politics','political'], required_words=['politics'])
    response(long.R_POPULATIONW, ['population'], required_words=['population','world'])
    response(long.R_POPULATIONI, ['population'], required_words=['population','india'])
    response(long.R_INDIA, ['india'], required_words=['know','india'])
    response(long.R_WHO, ['who'], required_words=['who','are','you'])
    response(long.R_CAPABLE, ['do'], required_words=['what','do','can'])
    response(long.R_INTERESTING, ['interesting'], required_words=['tell','interesting','something'])
    response(long.R_THANKS, ['good','okey','ok'], single_response=True)
    response(long.R_FINE, ['fine'], single_response=True)
    response(long.R_SLLEPING, ['sleeping'], required_words=['you','sleeping'])
    
    
    def unknown():
        response = [
            "Could you please rephrase that?",
            "I'm not sure I understand. Can you provide more context?",
            "I'm sorry, I don't have the information you're looking for.",
            "I'm still learning, so I might not have the answer. Is there anything else I can help with?",
            "I'm afraid I can't assist with that. Is there anything else you'd like to talk about?"
        ][random.randrange(5)]
        return response

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def send_message(event=None):
    user_input = entry_field.get()
    if user_input:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + user_input + "\n\n")
        chat_box.config(state=tk.DISABLED)

        bot_response = get_response(user_input)

        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Bot: " + bot_response + "\n\n")
        chat_box.config(state=tk.DISABLED)

        entry_field.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Ask Buddy")

# Create the chat history display
chat_box = tk.Text(window, height=20, width=50, bd=1, relief=tk.SOLID)
chat_box.config(state=tk.DISABLED)
chat_box.tag_configure("user", foreground="blue")
chat_box.tag_configure("bot", foreground="green")
chat_box.pack(pady=10)

# Create the user input field
entry_field = tk.Entry(window, width=50, font=("Helvetica", 15))
entry_field.bind("<Return>", send_message)
entry_field.pack(pady=10)

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message, font=("Helvetica", 15), relief=tk.RAISED, bd=2)
send_button.pack()

# Set focus on the entry field
entry_field.focus()

# Start the main event loop
window.mainloop()
