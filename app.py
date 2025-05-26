from flask import Flask, render_template, request, session, redirect, url_for
import joblib
from auth import auth_bp, get_authenticated_service
from utils.youtube_utils import get_user_videos, get_video_comments, delete_comment
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = "kkjhrjr77447gr5fks"
app.register_blueprint(auth_bp)

# Load trained model
model = joblib.load("Toxicity_classifier_v1.pkl")

# Route: Login Page
@app.route('/')
def index():
    return render_template("login.html") 

# Route: Dashboard Page (after login)
@app.route('/dashboard')
def dashboard():
    youtube = get_authenticated_service()
    if not youtube:
        return redirect(url_for("auth.login"))

    videos = get_user_videos(youtube)
    return render_template("dashboard.html", videos=videos, result=None)  # Include result=None to avoid missing var

# Route: Analyze selected video
@app.route('/analyze', methods=['POST'])
def analyze():
    video_id = request.form.get('video_id')
    youtube = get_authenticated_service()
    if not youtube:
        return redirect(url_for("auth.login"))

    # Get comments on selected video
    comments = get_video_comments(youtube, video_id)
    user_channel_id = youtube.channels().list(part='id', mine=True).execute()['items'][0]['id']

    toxic_comments = []

    # Predict using ML model
    texts = [c["text"] for c in comments]
    predictions = model.predict(texts)

    for comment, pred in zip(comments, predictions):
        if pred == 1 and comment['author'] != user_channel_id:
            delete_comment(youtube, comment['id'])
            toxic_comments.append(comment)

    # After analyzing, show result + video list again
    videos = get_user_videos(youtube)
    return render_template("dashboard.html", videos=videos, result=toxic_comments)

if __name__ == '__main__':
    app.run(debug=True)
