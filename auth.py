import os
import json
import google_auth_oauthlib.flow
from flask import Blueprint, session, redirect, request, url_for
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials  

auth_bp = Blueprint('auth', __name__)

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
CLIENT_SECRETS_FILE = "client_secret"                          # use your client secret file you can get it from google cloud console

@auth_bp.route("/login")
def login():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('auth.oauth2callback', _external=True)

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="select_account consent"  # This forces Google to show the account chooser
    )

    session["state"] = state
    return redirect(authorization_url)


@auth_bp.route("/oauth2callback")
def oauth2callback():
    state = session["state"]
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('auth.oauth2callback', _external=True)

    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    session["credentials"] = credentials_to_dict(credentials)

    return redirect(url_for("dashboard"))

def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes
    }

def get_authenticated_service():
    credentials_data = session.get("credentials")
    if not credentials_data:
        return None
    credentials = Credentials(**credentials_data)  #using google.oauth2.credentials.Credentials
    return build("youtube", "v3", credentials=credentials)

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

