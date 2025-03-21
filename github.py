import requests
from datetime import datetime, timedelta

import requests
import json


def push_to_slack(text):
    payload = json.dumps({"text": text})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)


def get_repo_stats(owner, repo, access_token):
    # GitHub API endpoint for fetching contributor stats
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Set the headers for authentication
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github+json",
    }

    # Calculate the time range for the last 24 hours
    now = datetime.now()
    last_24_hours = now - timedelta(days=1)
    last_week = now - timedelta(days=7)
    # Print the header

    # Make the API request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        contributors = {}
        push_to_slack(f"Repository: {owner}/{repo}")
        push_to_slack("Contributor\tLines\tCommits (last 24 hours)")

        for commit in data:
            if commit["commit"]["committer"]["date"] >= last_24_hours.isoformat():
                author = commit["commit"]["author"]["name"]
                if author not in contributors:
                    contributors[author] = {"lines": 0, "commits": 0}

                contributors[author]["commits"] += 1

                # Get the number of lines in the commit
                sha = commit["sha"]
                commit_url = (
                    f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
                )
                commit_response = requests.get(commit_url, headers=headers)
                if commit_response.status_code == 200:
                    commit_data = commit_response.json()
                    for file in commit_data["files"]:
                        contributors[author]["lines"] += file["changes"]

        for contributor, stats in contributors.items():
            push_to_slack(f"{contributor}\t{stats['lines']}\t{stats['commits']}")
        push_to_slack(f"Repository: {owner}/{repo}")
        push_to_slack("Contributor\tLines\tCommits (last week)")
        contributors = {}
        for commit in data:
            if commit["commit"]["committer"]["date"] >= last_week.isoformat():
                author = commit["commit"]["author"]["name"]
                if author not in contributors:
                    contributors[author] = {"lines": 0, "commits": 0}

                contributors[author]["commits"] += 1

                # Get the number of lines in the commit
                sha = commit["sha"]
                commit_url = (
                    f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
                )
                commit_response = requests.get(commit_url, headers=headers)
                if commit_response.status_code == 200:
                    commit_data = commit_response.json()
                    for file in commit_data["files"]:
                        contributors[author]["lines"] += file["changes"]

        for contributor, stats in contributors.items():
            push_to_slack(f"{contributor}\t{stats['lines']}\t{stats['commits']}")

    else:
        print(f"Error: {response.status_code} - {response.text}")
        print(response)


# CONFIGURATION
url = "SLACK_HOOK_URL"
access_token = "YUOR_GITHUB_ACCESS_TOKEN"
get_repo_stats("OWNER", "REPO_NAME", access_token)
