import os
import openai
import tiktoken

from openai.error import APIError, RateLimitError
from gpt_witter.config import Config

CFG = Config()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def create_chat_completion(
    messages: list,
    model: str = CFG.base_llm_model,
    temperature: float = CFG.temperature,
    max_tokens: int = None
) -> tuple:
    
    response = None
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    if response is None:
        return ('Error', '')

    return (
        response.choices[0]['finish_reason'],
        response.choices[0].message['content']
    )



def count_message_tokens(
    messages: list[dict[str, str]], model: str = CFG.base_llm_model
) -> int:
    
    encoding = tiktoken.encoding_for_model(model)
    if "gpt-3.5" in model:
        tokens_per_message = 4 
        tokens_per_name = -1 

    elif "gpt-4" in model:
        tokens_per_message = 3
        tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3 
    return num_tokens



def get_embedding(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(input = [text], model=model)
    return response['data'][0]['embedding']