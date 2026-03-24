import gradio as gr
import requests

def ask_veteran_assistant(question):
    if not question.strip():
        return "Please as a questin about veteran's resources in Chicago."
    
    try:
        response = requests.get(
            "http://localhost:8000/ask",
            params={"question": question}, 
            timeout=30
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error connecting to the assistant: {str(e)}"
    
demo = gr.Interface(
        fn=ask_veteran_assistant, 
        inputs=gr.Textbox(
            label="Ask a Question", 
            placeholder="Example question: Where can I find housing for veterans in Chicago?", 
            lines=3
        
    ), 
    outputs=gr.Textbox(
        label="Response", 
        lines=10
    ),
    title="🎖️ Chicago VetConnect AI",
    description="""
    Welcome to Chicago VetConnect AI, your resource assistant for military veterans in Chicago. 
    Ask a question about housing, mental health services, employment opportunities, VA benefits and more.
    Please note that this assistant provides information based on the most up-to-date resources available, but always verify details with official sources.
    If you are in crisis or need immediate assistance, please call 911, 988 (press 1), or 311 in Chicago
    """, 
    examples=[
        ["Where can I find housing for veterans in Chicago?"],
        ["What mental health resources are available for veterans in Chicago?"],
        ["How can I apply for VA benefits in Chicago?"],
        ["Are there any employment programs for veterans in Chicago?"],
        ["What organizations provide support for homeless veterans in Chicago?"]
    ], 
    theme=gr.themes.Soft()
    )

if __name__ == "__main__":
        demo.launch(server_port=7860, server_name="0.0.0.0")
