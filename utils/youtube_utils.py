def get_user_videos(youtube):
    request = youtube.channels().list(
        part="contentDetails",
        mine=True
    )
    response = request.execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    next_page_token = None
    while True:
        playlist_request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=10,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()

        for item in playlist_response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            title = item["snippet"]["title"]
            thumbnail = item["snippet"]["thumbnails"]["default"]["url"]
            videos.append({
                "id": video_id,
                "title": title,
                "thumbnail": thumbnail
            })

        next_page_token = playlist_response.get("nextPageToken")
        if not next_page_token:
            break

    return videos



def get_video_comments(youtube, video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    while request:
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "id": item["snippet"]["topLevelComment"]["id"],
                "text": comment["textDisplay"],
                "author": comment["authorChannelId"]["value"]
            })
        request = youtube.commentThreads().list_next(request, response)
    return comments


def delete_comment(youtube, comment_id):
    youtube.comments().setModerationStatus(
        id=comment_id,
        moderationStatus='rejected'
    ).execute()
