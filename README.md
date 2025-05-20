# ✍️ AI Poetry Generator & Evaluator

**Generate beautiful poems using lightweight LLMs (like Phi-3, Gemma, TinyLlama) and evaluate their quality with BERTScore.**

![Demo GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW0yY2hqM2RjOGV1dXJtY3JtM3B6Y2VlZzR6eHp2eGJ6YzZ5dW9xZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMHxhOfscxPfIfm/giphy.gif)  


## 🌟 Features

- **Lightweight Model Support**:  
  - `phi3` (3.8B) | `gemma:2b` | `tinyllama` (1.1B) | `llama3.2`  
  - Optimized for speed and low resource usage

- **Customizable Generation**:  
  - Adjust creativity (`temperature`)  
  - Control poem length (`max_tokens`)  

- **Quality Evaluation**:  
  - BERTScore (Precision, Recall, F1) against reference poems  
  - Auto-evaluation when reference is pasted  

- **User-Friendly Interface**:  
  - Gradio web app  
  - Example prompts & real-time feedback  

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed ([Installation Guide](https://ollama.com/))

### Installation
```bash
git clone https://github.com/yourusername/ai-poetry-generator.git
cd ai-poetry-generator

# Install dependencies
pip install -r requirements.txt

# Download models (choose at least one)
ollama pull phi3       # Recommended (best balance)
ollama pull gemma:2b   # Google's lightweight
ollama pull tinyllama  # Fastest option
```

### Usage
**Command Line:**
```bash
python generate_poem_ollama.py --prompt "a sunset over mountains" --model phi3
```

**Web Interface:**
```bash
python app.py
```
➡️ Open `http://localhost:7860` in your browser  

## 🛠️ Files
| File | Description |
|------|-------------|
| `app.py` | Gradio web interface (main application) |
| `generate_poem_ollama.py` | CLI version for poem generation |
| `evaluate_bertscore.py` | Standalone evaluation script |
| `requirements.txt` | Python dependencies |

## 📊 Example Output
```text
Generated Poem (phi3, temperature=0.7):

"The mountain wears the sunset
like a crown of molten gold,
while shadows stretch their fingers
across the valleys cold."

BERTScore Metrics:
- Precision: 0.872
- Recall: 0.845 
- F1: 0.858
```

## 🤖 Models Comparison
| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| Phi-3 | 3.8B | ⚡⚡⚡ | ★★★★☆ | Balanced use |
| Gemma-2B | 2B | ⚡⚡⚡⚡ | ★★★☆☆ | Fast drafts |
| TinyLlama | 1.1B | ⚡⚡⚡⚡⚡ | ★★☆☆☆ | Quick testing |
| Llama3.2 | 8B | ⚡⚡ | ★★★★☆ | Higher quality |


