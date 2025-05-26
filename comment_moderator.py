# Prediction function for future use
import joblib
def classify_comments(comments):
    model = joblib.load("Toxicity_classifier_v1.pkl")
    predictions = model.predict(comments)
    return predictions