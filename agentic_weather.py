import gradio as gr

from llmodel import agent_response


    
    # Gradio UI 
    # https://www.gradio.app/guides/quickstart
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Agentic Weather Assistant (Hugging Face Model)")
    user_input = gr.Textbox(label="Ask something", placeholder="e.g., What's the weather in Athens?")
    output = gr.Textbox(label="Agent's reply", lines=6)
    btn = gr.Button("Ask")

    btn.click(fn=agent_response, inputs=user_input, outputs=output)

demo.launch()