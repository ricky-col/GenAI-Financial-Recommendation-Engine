import os
from dotenv import load_dotenv 
#load_dotenv is the tool that knows how to read the hidden .env file you created earlier.
from langchain_google_genai import ChatGoogleGenerativeAI
#ChatGoogleGenerativeAI is the specific LangChain tool designed to communicate with Google's Gemini models.


# 1. Load the secret API key from your .env file
load_dotenv()

# It silently opens your 
# .gitignore-protected .env file, finds your GEMINI_API_KEY, and loads it into the environment.
#  Because of this, LangChain will automatically know how to authenticate you without you ever 
# having to type your key directly into the code.

# 2. Initialize the LLM (The Brain)
# We are using Gemini 2.5 Flash as it is fast and included in the free tier
print("Initializing the Brain...")
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7 # 0 is strict/factual, 1 is highly creative. 0.7 is a good balance.
)

#temperature is used to dictate how creative the AI is allowed to be.




# 3. Create a prompt and ask the Brain
question = "In short sentence ,what is difference between a stock and a bond?"
print(f"Asking: '{question}'\n")


# 4. Get the response and print it
response = llm.invoke(question)

# .invoke() is the LangChain command that says "take this input and process it."

print("---")
print("Brain says:")
print(response.content)
print("---")