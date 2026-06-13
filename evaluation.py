from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(true_answers, predicted_answers):
    y_true = [1 for _ in true_answers]
    y_pred = [1 if p.strip() != "" else 0 for p in predicted_answers]

    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return {
        "accuracy": accuracy,
        "f1_score": f1
    }