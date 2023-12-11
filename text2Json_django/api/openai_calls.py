import os
from openai import OpenAI
import openai
import yaml

# '''
#     This function returns how many tokens are calculated by openai's tokenizer
# '''
# def calculate_openai_token_length(text):
#     return len(openai.Tokenizer().encode(text))

def setup_openai_api():
    """
    Configure the OpenAI API key from an environment variable
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("No OpenAI API key found in environment variables")
    client = OpenAI(
        api_key=api_key,
    )

    return client

def ask_chatgpt(prompt, model="gpt-3.5-turbo", max_tokens=100):
    """
    Send a prompt to ChatGPT and return the text response.
    """
    client = setup_openai_api()
    # print("prompt gone : ", prompt)
    try:
        response = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant."}, #play around with this
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
        return str(response.choices[0].message.content)
    except Exception as e:
        print("I am inside the openai exception")
        print(str(e))
        return str(e)

# # Example usage
# if __name__ == "__main__":
#     setup_openai_api()

#     prompt = "Tell me a joke"
#     response = ask_chatgpt(prompt)
#     print(response)
