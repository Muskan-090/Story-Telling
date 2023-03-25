import streamlit as st
import numpy as np

import openai as ai
ai.api_key = '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' 
def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=3,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)
    
    # Return the first choice's text
    return completions.choices[0].text

st.header('Story Telling')

prompt = st.text_input("Please Give the Story Name Here",key="ms")
response = generate_gpt3_response(prompt)



# s = ['An unexpected visitor',"A time travel adventure","A haunted house"]
# st.selectbox("Please Give the Story Name",s )

    

if st.button("Submit"):
    if response.startswith(')'):
        st.text("Please Give Proper Story name")

    elif "{" in response :
        st.text("Please Give Proper Story name")

    else:
        st.markdown(response)
    
