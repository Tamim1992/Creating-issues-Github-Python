import requests
import json

GITHUB_API = 'https://api.github.com'
GITHUB_OWNER = "Mi-BI"
GITHUB_REPO = "Demo"
GITHUB_TOKEN = 'ghp_OTFQeM6ypaKvzlGv1CagAq0'
REDCAP_API = 'https://showmeportal.missouri.edu/redcap/api/'

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_issues():
    url = f'{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues?state=open'
    response = requests.get(url, headers=HEADERS)
    if response.status_code!= 200:
        raise Exception(f Request failed with status {response.status_code}")
    return response.json()

def get_redcap_data():
    payload = {
        'token': '',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }
    response = requests.post(REDCAP_API, data=payload)
    print('HTTP Status: ' + str(response.status_code))
    if response.status_code!= 200:
        raise Exception(f"Request failed with status {response.status_code}")
    return response.json()

def post_issue(issue):
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues"
    response = requests.post(url, data=json.dumps(issue), headers=HEADERS)
    if response.status_code != 201:
        raise Exception(f"Issue creation failed with status {response.status_code}")

def create_issues():
    issue_data = get_issues()
    redcap_data = get_redcap_data()

    for item in redcap_data:
        issue_title = f"{item['issue_id']} {item['request_title']}"
        issue_body = f"{item['prob_desc']}\nFullname: {item['full_name']}\nEmail: {item['email_address']}\nIssue_Type: {item['issue_type']}"
        labels = [item['email_address']]
        issue = {"title": issue_title, "body": issue_body, "labels": labels}

        if any(existing_issue["title"] == issue_title for existing_issue in issue_data):
            print(f"Issue '{issue_title}' already exists!")
        else:
            post_issue(issue)

    print("Issues created")

if __name__ == "__main__":
    create_issues()
