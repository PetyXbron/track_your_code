# track_your_code
Script that tracks number of lines and number of commits made by contributors to a particular repo in the last 24 hours and last 1 week. 

## How to run?

### Requirements ❗

- **Python 3.x**
- **requests** module (cmd: `pip install requests`)

### Installation 💻

1. Clone this repository.

2. Make sure you have a valid GitHub Access Token with repository read access. You can generate one by following these steps:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Generate a token with the necessary permissions for accessing the repository commits.

3. Set up a Slack Incoming Webhook:
   - Go to [Slack API: Incoming Webhooks](https://api.slack.com/messaging/webhooks) and create an incoming webhook for the desired channel.
   - Copy the Webhook URL.

4. Follow the [Configuration](#configuration) section below.

5. See in the [Run](#run) section.

### Configuration ⚙️

Before running the script, update the following variables:

1. Replace `SLACK_HOOK_URL` with your Slack Incoming Webhook URL.
2. Replace `YOUR_GITHUB_ACCESS_TOKEN` with your GitHub personal access token.
3. Replace `OWNER` with the GitHub username or organization name.
4. Replace `REPO_NAME` with the repository name.


```python
url = "SLACK_HOOK_URL"
access_token = "YOUR_GITHUB_ACCESS_TOKEN"
get_repo_stats("OWNER", "REPO_NAME", access_token)
```

You can find this code block at the end of the [file](./github.py).

### Run 🟢

Simply run the script with **Python**.  
One of the possible commands is **`py ./github.py`**.