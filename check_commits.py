import requests
import json

# Replace with your GitHub username, repository, and personal access token
USERNAME = 'harsha378'
REPO_NAME = 'CI-CD-setup'
ACCESS_TOKEN = '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'
# URL to the GitHub API endpoint for the commits of the repository
url = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/commits'

# Headers containing the personal access token for authentication
headers = {'Authorization': f'token {ACCESS_TOKEN}'}

def get_latest_commit():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            latest_commit = commits[0]
            return latest_commit
        else:
            return None
    else:
        print('Error fetching commits:', response.status_code)
        return None

def main():
    latest_commit = get_latest_commit()
    if latest_commit:
        print('Latest commit SHA:', latest_commit['sha'])
        print('Author:', latest_commit['commit']['author']['name'])
        print('Date:', latest_commit['commit']['author']['date'])
        print('Message:', latest_commit['commit']['message'])
    else:
        print('No commits found.')

if __name__ == '__main__':
    main()
