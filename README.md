# YouTube-Channel-Video-Monitor
Periodically check if a YouTube channel made videos public, private, unlisted, or deleted them.

# Requirements
- Python
- Google API Key (get one at https://console.cloud.google.com/ - specifically the YouTube Data API v3)
- Discord Webhook
- Your Discord User ID

# Setup
1. Open a command prompt in this program's directory and run `pip install -r requirements.txt`
2. Run `python main.py` - this will create a keys.json file on first launch.
3. Open keys.json and input all of the relevant API keys and other values - the names should be self-explanatory
4. Run `python main.py` again - this time it will actually do the thing!

