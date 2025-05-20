import ollama
import argparse

# List of available models
AVAILABLE_MODELS = [
    "phi3",      # Mistral 7B
    "gemma:2b",        # Google's Gemma
    "llama3.2",
    "tinyllama"        # Meta's Llama 2
]

def generate_poem(prompt, model="llama3", temperature=0.8, max_length=50):
    try:
        response = ollama.generate(
            model=model,
            prompt=f"Write a poem about: {prompt}. Use creative language and metaphors.",
            options={
                "temperature": temperature,
                "num_predict": max_length
            }
        )
        return response["response"]
    except Exception as e:
        return f"Error generating poem: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate poems using different LLM models")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt for the poem")
    parser.add_argument("--model", type=str, choices=AVAILABLE_MODELS, default="llama3",
                       help="Model to use for generation")
    parser.add_argument("--temperature", type=float, default=0.8,
                       help="Creativity level (0.1-1.0)")
    parser.add_argument("--max_length", type=int, default=50,
                       help="Maximum length of the poem in tokens")
    
    args = parser.parse_args()
    
    poem = generate_poem(
        args.prompt,
        model=args.model,
        temperature=args.temperature,
        max_length=args.max_length
    )
    
    print(f"Generated Poem (using {args.model}):\n{poem}")