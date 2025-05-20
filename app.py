import ollama
from bert_score import score
import gradio as gr
import time

# Available lightweight models
LIGHTWEIGHT_MODELS = [
    "phi3",        # Microsoft's Phi-3-mini (3.8B)
    "gemma:2b",    # Google's Gemma (2B)
    "llama3.2",    # Meta's Llama 3 (8B) - your custom name?
    "tinyllama"    # TinyLlama (1.1B)
]

# Function to generate poems
def generate_poem(prompt, model="phi3", creativity=0.7, max_length=100):
    try:
        response = ollama.generate(
            model=model,
            prompt=f"Write a creative poem about: {prompt}. Use vivid imagery and metaphors.",
            options={
                "temperature": creativity,
                "num_predict": max_length
            }
        )
        return response["response"]
    except Exception as e:
        return f"Error generating poem: {str(e)}\nDid you install the model? Try: ollama pull {model}"

# Function to evaluate with BERTScore
def evaluate_poem(generated_poem, reference_poem):
    if not generated_poem or not reference_poem.strip():
        return {"Error": "Please generate a poem and provide a reference poem"}
    
    try:
        P, R, F1 = score([generated_poem], [reference_poem], lang="en", verbose=False)
        return {
            "Precision": round(P.mean().item(), 3),
            "Recall": round(R.mean().item(), 3),
            "F1 Score": round(F1.mean().item(), 3)
        }
    except Exception as e:
        return {"Evaluation Error": str(e)}

# Gradio interface
with gr.Blocks(title="Lightweight Poetry Generator", theme="soft") as app:
    gr.Markdown("""
    # 🖋️ Poetry Generator & Evaluator
    *Generate poems using efficient LLMs and evaluate their quality*
    """)
    
    with gr.Row():
        with gr.Column():
            # Input Section
            prompt = gr.Textbox(
                label="Poem Theme",
                placeholder="e.g., 'a lonely lighthouse at midnight'",
                lines=2
            )
            
            with gr.Row():
                model = gr.Dropdown(
                    LIGHTWEIGHT_MODELS,
                    value="phi3",
                    label="Model",
                    info="Select lightweight LLM"
                )
                creativity = gr.Slider(
                    0.1, 1.0, 
                    value=0.7, 
                    step=0.1,
                    label="Creativity",
                    info="Higher = more creative/random"
                )
                max_length = gr.Slider(
                    50, 200,
                    value=100,
                    step=10,
                    label="Max Length",
                    info="In tokens (~0.75 words per token)"
                )
            
            generate_btn = gr.Button("Generate Poem", variant="primary")
        
        with gr.Column():
            # Output Section
            generated_poem = gr.Textbox(
                label="Generated Poem",
                lines=8,
                interactive=False
            )
    
    # Evaluation Section
    with gr.Row():
        reference_poem = gr.Textbox(
            label="Reference Poem (for evaluation)",
            lines=5,
            placeholder="Paste a human-written poem here to compare...",
            info="Will auto-evaluate when pasted"
        )
        metrics = gr.JSON(
            label="Evaluation Metrics",
            show_label=True
        )
    
    # Generation action
    generate_btn.click(
        fn=generate_poem,
        inputs=[prompt, model, creativity, max_length],
        outputs=generated_poem
    )
    
    # Auto-evaluation when reference is provided
    reference_poem.change(
        fn=evaluate_poem,
        inputs=[generated_poem, reference_poem],
        outputs=metrics
    )
    
    # Examples
    gr.Examples(
        examples=[
            ["a sunset over the ocean", "phi3", 0.6, 80, 
             "Golden waves embrace the dying light,\nThe sky burns briefly, then turns to night."],
            ["forgotten childhood memories", "gemma:2b", 0.8, 100,
             "Faded like a photograph left in the rain,\nLaughter echoes I can't reclaim."]
        ],
        inputs=[prompt, model, creativity, max_length, reference_poem],
        label="Try these examples (click then Generate)"
    )
    
    # Footer
    gr.Markdown("""
    ### Tips:
    - Start with `phi3` for best balance of speed/quality
    - Use `tinyllama` for fastest generation
    - `llama3.2` may offer better quality but be slower
    """)

if __name__ == "__main__":
    # Check if models are available
    print(f"Available lightweight models: {', '.join(LIGHTWEIGHT_MODELS)}")
    app.launch(server_port=7860, share=False)