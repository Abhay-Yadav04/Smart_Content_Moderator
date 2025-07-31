# 🎯 Smart Content Moderator

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/Abhay-Yadav04/Smart_Content_Moderator/blob/main/LICENSE) [![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/built%20with-Flask-yellow)](https://flask.palletsprojects.com/)  
A child-safe YouTube content recommender and comment moderator using Machine Learning & YouTube API.

---

## 🚀 About the Project

**Smart Content Moderator** is a web application that ensures safe content consumption on YouTube by:
- Recommending only child-safe videos based on comment toxicity.
- Automatically classifying and **deleting toxic comments** from a user's own videos after logging in via Google/YouTube.
- Providing a friendly, interactive interface with Google OAuth authentication.

This project combines **Machine Learning (Random Forest Classifier)**, and  **Flask**, **YouTube Data API**, **OAuth 2.0** to help creators and parents maintain a safe and clean video environment.

---

## ✨ Features

✅ Login using YouTube (Google OAuth)  
✅ Fetch all uploaded videos of the logged-in user  
✅ Analyze comments using a trained ML toxicity detection model  
✅ Automatically delete toxic comments from your own videos  
✅ Recommend videos based on user input **(e.g. “trip vlog”)**, filtering out toxic-commented ones  
✅ Intuitive frontend with a kid-friendly design and animations

---

## 🛠️ Tech Stack

| Tech           | Usage                        |
|----------------|------------------------------|
| **Python**     | Core language                |
| **Flask**      | Web framework                |
| **YouTube API**| Fetching videos & comments   |
| **Google OAuth** | Secure user login           |
| **Scikit-learn** | Machine learning model      |
| **TF-IDF**     | Comment feature extraction   |
| **HTML/CSS**| Frontend                     |

---

## 🧠 Machine Learning

The model used is a **Random Forest Classifier** trained on a labeled dataset of YouTube comments.  
It uses **TF-IDF Vectorization** to convert text into numerical features.  

- ✅ Trained & serialized using `joblib`
- ✅ Accurate toxicity classification
- ✅ Plug-and-play in production

---

## 📸 Screenshots

<details>
  <summary>🔍 Click to expand</summary>

| Dashboard                         |
|-----------------------------------|
| ![image alt](https://github.com/Abhay-Yadav04/Smart_Content_Moderator/blob/b5128136e2c78460b264b1bd0b3f48e370ed6c9f/out_project.PNG) |

</details>

---

## 🔐 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhay-Yadav04/Smart_Content_Moderator.git
   cd Smart_Content_Moderator
