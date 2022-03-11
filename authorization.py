
import tekore as tk

def authorize():
     CLIENT_ID = "e10ac37a1f52485398654da6db1a33b3"
     CLIENT_SECRET = "833e872d58e046008ef235980bb1b289"
     app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
     return tk.Spotify(app_token)
