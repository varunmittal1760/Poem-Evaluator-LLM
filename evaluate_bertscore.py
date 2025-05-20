# evaluate_bertscore.py
from bert_score import score

def evaluate_poem(generated_poem, reference_poem):
    P, R, F1 = score([generated_poem], [reference_poem], lang="en", verbose=True)
    return {
        "Precision": round(P.mean().item(), 3),
        "Recall": round(R.mean().item(), 3),
        "F1": round(F1.mean().item(), 3)
    }

if __name__ == "__main__":
    with open("generated_poem.txt", "r") as f:
        generated = f.read().strip()
    
    with open("data/references/autumn_reference.txt", "r") as f:
        reference = f.read().strip()
    
    metrics = evaluate_poem(generated, reference)
    print("\nBERTScore Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")