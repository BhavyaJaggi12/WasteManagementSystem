import openai
import gradio as gr

# Replace with your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        max_tokens=50,  # Lowering the number of tokens
        temperature=0.5  # Less variability in responses
)

        return response.choices[0].message['content'].strip()  # Extract the response content
    except openai.error.OpenAIError as e:
        print(f"OpenAI Error: {str(e)}")  # Logs the error details
        return f"An error occurred: {str(e)}"
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")  # Logs unexpected errors
        return f"Unexpected error: {str(e)}"

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="ChatGPT-powered Chatbot",
    description="Ask me anything!"
)

iface.launch()
