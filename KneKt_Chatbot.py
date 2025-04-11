import openai


openai.api_key="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"


def chat_with_bot():
    print("Chatbot is ready to chat! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            bot_reply = response.choices[0].message.content.strip()
            print(f"Chatbot: {bot_reply}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_bot()



# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a haiku about ai"}
#   ]
# )

# print(completion.choices[0].message);
