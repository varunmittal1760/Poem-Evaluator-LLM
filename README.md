✍️ AI Poetry Generator & Evaluator
Generate beautiful poems using lightweight LLMs (like Phi-3, Gemma, TinyLlama) and evaluate their quality with BERTScore.

🚀 Quick Start

Prerequisites

Python 3.8+
Ollama installed 

Installation
git clone https://github.com/yourusername/ai-poetry-generator.git
cd ai-poetry-generator

Install Dependencies
pip install -r requirements.txt

Download models (choose at least one)
ollama pull phi3       # Recommended (best balance)
ollama pull gemma:2b   # Google's lightweight
ollama pull tinyllama  # Fastest option

Usage

Command Line:
python generate_poem_ollama.py --prompt "a sunset over mountains" --model phi3

Web Interface:
python app.py

➡️ Open http://localhost:7860 in your browser

🛠️ Files

File	Description
app.py	Gradio web interface (main application)
generate_poem_ollama.py	CLI version for poem generation
evaluate_bertscore.py	Standalone evaluation script
requirements.txt	Python dependencies

📊 Example Output
Generated Poem (phi3, temperature=0.7):

"The mountain wears the sunset
like a crown of molten gold,
while shadows stretch their fingers
across the valleys cold."

BERTScore Metrics:
- Precision: 0.872
- Recall: 0.845 
- F1: 0.858

🤖 Models Comparison

Model	Size	Speed	Quality	Best For
Phi-3	3.8B	⚡⚡⚡	★★★★☆	Balanced use
Gemma-2B	2B	⚡⚡⚡⚡	★★★☆☆	Fast drafts
TinyLlama	1.1B	⚡⚡⚡⚡⚡	★★☆☆☆	Quick testing
Llama3.2	8B	⚡⚡	★★★★☆	Higher quality
