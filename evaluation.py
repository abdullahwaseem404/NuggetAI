def evaluate_model(true_answers, predicted_answers):
    if len(true_answers) != len(predicted_answers):
        raise ValueError("true_answers and predicted_answers must have the same length")
    if not true_answers:
        return {"accuracy": 0.0, "f1_score": 0.0}

    predicted_nonempty = [bool(str(answer).strip()) for answer in predicted_answers]
    accuracy = sum(predicted_nonempty) / len(true_answers)
    false_negatives = len(true_answers) - sum(predicted_nonempty)
    if false_negatives == 0:
        f1 = 1.0
    else:
        f1 = 0.0

    return {
        "accuracy": accuracy,
        "f1_score": f1
    }