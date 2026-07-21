import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the secret API key from your hidden .env file
load_dotenv()

# Quick safety check: stop the program if the key is missing
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Error: OPENAI_API_KEY is missing from your .env file!")

# 2. Initialize the official OpenAI client
client = OpenAI()

def start_chatbot():
    print("==========================================================")
    print("🚀 Welcome to Ramir's Personal Portfolio Assistant! 🚀")
    print("Ask me about Ramir's skills, coursework, or projects.")
    print("Type 'exit', 'quit', or 'bye' to leave the chat.")
    print("==========================================================")

    # 3. Personalized System Prompt & Portfolio Data
    messages = [
        {
            "role": "system",
            "content": (
                "You are 'Ramir's Portfolio Agent', a professional AI representative for Ramir (RJ) Moses, "
                "a Computer Science student at East Carolina University (ECU).\n\n"
                
                "Your job is to answer questions from tech recruiters or peers using only the following facts:\n"
                "- Education: Pursuing a BS in Computer Science at East Carolina University. Upper-level coursework includes Operating Systems, Systems Programming, and Computer Networking.\n"
                "- Core Technical Skills: Java, Rust, Python, C, backend systems programming, network protocol analysis, and database management.\n"
                "- Featured Projects:\n"
                "  1. Single-Threaded Java Web Server: Built a lightweight HTTP/1.0-style web server from scratch that handles individual client connections.\n"
                "  2. Rust Database CRUD System: Developed a user management engine using Rust, Diesel ORM, and SQLite.\n"
                "  3. Task Management API: Engineered a high-performance web API using the Rocket framework in Rust.\n"
                "  4. This Portfolio Chatbot: A Python application utilizing the OpenAI API, featuring context management, full conversation history, and secure environment configuration.\n"
                "- Interests: Backend systems development, network security, educational policy equity, and theatre arts.\n\n"
                
                "CRITICAL INSTRUCTIONS:\n"
                "- Maintain a professional, polite, and enthusiastically helpful tech persona.\n"
                "- Speak about Ramir in the third person (e.g., 'Ramir built...' or 'He is currently studying...').\n"
                "- If asked an interview question outside of these facts, politely mention that you represent Ramir's tech portfolio and encourage them to connect with him on GitHub/LinkedIn for deeper inquiries."
            )
        }
    ]

    # 4. The Live Conversation Loop
    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n🚀 Assistant: Thank you for inquiring about Ramir's portfolio! Feel free to review his codebase. Have a great day! 👋")
                break

            messages.append({"role": "user", "content": user_input})

            print("\nThinking...")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            assistant_reply = response.choices[0].message.content
            print(f"\n🚀 Assistant: {assistant_reply}")

            messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    start_chatbot()