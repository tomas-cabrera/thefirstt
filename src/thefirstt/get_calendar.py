"""An initial module getting the calendar from Google Calendar API."""

import json

import google.oauth2.credentials as go2credentials
from googleapiclient.discovery import build

###############################################################################

# Read credentials from local file
PATH_TO_CREDS = "/home/tomas/Documents/google/thefirstt_credentials.json"
with open(PATH_TO_CREDS, encoding="utf8") as json_file:
    tokens = json.load(json_file)
cred_kwarg_tokens = {
    k: v
    for k, v in tokens.items()
    if k
    in [
        "refresh_token",
        "token_uri",
        "client_id",
        "client_secret",
    ]
}

credentials = go2credentials.Credentials(
    tokens["access_token"],
    **cred_kwarg_tokens,
)

with build("calendar", "v3", credentials=credentials) as service:
    calendar = service.calendars().get(calendarId=tokens["calendarId"]).execute()
    print(calendar)

    page_token = None
    pages = 0
    while True:
        pages += 1
        events = (
            service.events()
            .list(
                calendarId=tokens["calendarId"],
                # pageToken=page_token,
            )
            .execute()
        )
        for event in events["items"]:
            print()
            # print(event)
            if event["status"] == "confirmed":
                print(event["summary"])
                print(event["status"])
                print(event["start"])
                print(event["end"])
            elif event["status"] != "cancelled":
                print(event)
        page_token = events.get("nextPageToken")
        if not page_token:
            break
print(len(events))
print(events.keys())
print(len(events["items"]))
print(pages)
