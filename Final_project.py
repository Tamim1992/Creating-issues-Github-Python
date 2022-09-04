
import requests
import json

# Git hub data 
owner = "Missouri-BMI"
repo = "Demo"
myToken = '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'
myUrl = f'https://api.github.com/repos/{owner}/{repo}/issues?state=Open'
head = {'Authorization': 'token {}'.format(myToken)}
r = requests.get(myUrl, headers=head)


def call_api(apicall, header, **kwargs):
    data = kwargs.get('page', [])

    resp = requests.get(apicall, headers=header)
    data += resp.json()

    # failsafe
    if len(data) > 500:
        return (data)

    if 'next' in resp.links.keys():
        return (call_api(resp.links['next']['url'], header, page=data))

    return (data)


issue_data = call_api(myUrl, head)
print(len(issue_data))

#fetching data from REDCAP

data = {
    'token': '9D08561FC9245E68E890E7AFCB68ABD3',
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
r = requests.post('https://showmeportal.missouri.edu/redcap/api/',data=data)
print('HTTP Status: ' + str(r.status_code))
my_dict = r.json()


#CREATEING ISSUES IN GITHUB
url = "https://api.github.com/repos/{}/{}/issues".format(owner, repo)

if len(issue_data) == 0:
    for item1 in my_dict:
        rc_name = item1['full_name']
        rc_req_id = item1['issue_id']
        rc_req_title = item1['request_title']
        rc_pb_desc = item1['prob_desc']
        rc_issue_type =item1['issue_type']
        rc_label = item1['email_address']
        datas = {"title": str(rc_req_id) + " " + str(rc_req_title), "body": str(rc_pb_desc) + '\n' + " " + '\n' + "Fullname: " + str(rc_name) + '\n' + "Email: " + str(rc_label) + '\n' + "Issue_Type: " + str(rc_issue_type), "labels": [rc_label]}
        requests.post(url, data=json.dumps(datas), headers=head)
else:
    for item1 in my_dict:
        rc_name = item1['full_name']
        rc_req_id = item1['issue_id']
        rc_req_title = item1['request_title']
        rc_pb_desc = item1['prob_desc']
        rc_issue_type =item1['issue_type']
        rc_label = item1['email_address']
        datas = {"title": str(rc_req_id) + " " + str(rc_req_title), "body": str(rc_pb_desc) + '\n' + "Fullname: " + str(rc_name) + '\n' + "Email: " + str(rc_label) + '\n' + "Issue_Type: " + str(rc_issue_type), "labels": [rc_label]}
        flag = False
        for item in issue_data:
            if item["title"] == str(rc_req_id) + " " + str(rc_req_title):
                flag = True
                print("It is alreay Exist!")

        if flag==False:
            requests.post(url, data=json.dumps(datas), headers=head)

print("Creating Issues")