# LLM-ChatBot
ChatBot made using groq, langchain and streamlit. The AI model used is Llama-3.1-70b-versatile.

# Set-Up
- To get started we first need to get an API_KEY from here: [https://console.groq.com/keys].
- Create a file named `secrets.toml` in your .streamlit folder (Make sure you have streamlit installed, if not, run ```pip install streamlit```)
- Save the API key in the `secrets.toml` file using the following line:
        ```GROQ_API_KEY = '<YOUR API KEY>'```
- Replace <YOUR API KEY> with the key you got earlier.
- **To get started, first install the dependencies using:**

 ```pip install -r requirements.txt```
 
- **Run the streamlit app:**

```streamlit run my_llm_chatbot.py```
