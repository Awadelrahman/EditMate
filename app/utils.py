import streamlit as st 
from openai import OpenAI

def get_response(txt):
    prompt= """You are my writing assistant, 
            correct the grammar and spelling of this text 
            but neither you change the writing style 
            nor you add additional information: """+txt
    from dotenv import dotenv_values
    config = dotenv_values(".env")

    client = OpenAI(
            api_key=config['OPENAI_API_KEY'],
                )
            
    response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="gpt-3.5-turbo",
                )
    
    
    corrected_text=response.choices[0].message.content
    return(corrected_text)
