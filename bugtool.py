import json
import time
import requests

def bugtool():
    """获取bug信息 如状态 优先级等"""
    header = {
        "Accept":"*/*",
        "Connection":"keep-alive",
        "content-type":"application/json"
    }
    cookie = {"ajs_anonymous_id":"%22772a5426-d38d-40f4-91c7-ceedc0d30a3f%22","atlassian.xsrf.token":"725e5e66-f148-4f2e-a701-9a168378c0b7_d2ad8fed3052cef27f93327a4e1661de93fc26f2_lin","jira.navigation.expandableMenuStates.classic-issues-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","jira.navigation.expandableMenuStates.classic-apps-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","JSESSIONID":"ED16D3B1E1424A848F87F1095CB3FED4","cloud.session.token":"eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI2Mjk3MDdlYjU2M2QzODAwNjhiMWQ3NzMiLCJlbWFpbERvbWFpbiI6InJjdC5haSIsImltcGVyc29uYXRpb24iOltdLCJjcmVhdGVkIjoxNjY0MzYyMTIxLCJyZWZyZXNoVGltZW91dCI6MTY2NzI4MzEyOSwidmVyaWZpZWQiOnRydWUsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6IjE0ODQ0ZWI2LWMyYmItNGJiZC1iMzU5LWNlMjAxMmMxNTFiMCIsInN0ZXBVcHMiOltdLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE2NjcyODI1MjksImV4cCI6MTY2OTg3NDUyOSwiaWF0IjoxNjY3MjgyNTI5LCJlbWFpbCI6IndhbmdsaWppZUByY3QuYWkiLCJqdGkiOiIxNDg0NGViNi1jMmJiLTRiYmQtYjM1OS1jZTIwMTJjMTUxYjAifQ.WFoT_iUfEMoXPEu2-lwbHEmoM-ksIIKxVmfH4wM7N8ZQO0ZKgyGNL5nFl9xYYRhFlnxE9vRJRaM53aQJ0TaUakIi6ZnpD0-ORb_YS-3ui8mStUPOslTonJjh-wvc0WVOT9Sp6bfdkwZMAc1Z01C3vYdbzgq6KO62fAWA_hKherNFsjkyVvfrdVhSLTu4YeMEjR5A9oHWIJdr335SDO5ZOcP5HVh7Spm6088XV5JPD_86s6jmOKTDLgR1uCPHjigIHzhlHL-5J2jU2E-rxm_oeXPznxUYfymbxmBUB8DIlMeBs7CNm3zXAWJQ58ouNGDXqbTdX4faTm5gSN2InexDNQ"}
    query = """query IssueListQuery($jql: String, $first: Int!, $last: Int, $filterId: Int, $amountOfIds: Int, $isMaxResultsLimitEnabled: Boolean!) {\n  issueIds: issues(first: $amountOfIds, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      issueId\n      __typename\n    }\n    __typename\n  }\n  issues(first: $first, last: $last, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      ...GetIssueDetails\n      __typename\n    }\n    ...GetTotalCountFragment\n    jql\n    __typename\n  }\n}\n\nfragment GetIssueDetails on Issue {\n  ...GetIdFragment\n  ...GetIssueIdFragment\n  ...GetIssueKeyFragment\n  ...GetAssigneeFragment\n  ...GetIssueTypeFragment\n  ...GetSummaryFragment\n  ...GetStatusFragment\n  ...GetReporterFragment\n  ...GetPriorityFragment\n  ...GetCreatedFragment\n  ...GetResolutionFragment\n  ...GetUpdatedFragment\n  ...GetDueDateFragment\n  __typename\n}\n\nfragment GetIdFragment on Issue {\n  __typename\n  id\n}\n\nfragment GetIssueIdFragment on Issue {\n  issueId\n  __typename\n}\n\nfragment GetIssueKeyFragment on Issue {\n  issuekey {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetAssigneeFragment on Issue {\n  assignee {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetIssueTypeFragment on Issue {\n  issuetype {\n    iconUrl\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetSummaryFragment on Issue {\n  summary {\n    textValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetStatusFragment on Issue {\n  status {\n    name\n    statusId\n    statusCategoryId\n    __typename\n  }\n  __typename\n}\n\nfragment GetReporterFragment on Issue {\n  reporter {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetPriorityFragment on Issue {\n  priority {\n    name\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment GetCreatedFragment on Issue {\n  created {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetResolutionFragment on Issue {\n  resolution {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetUpdatedFragment on Issue {\n  updated {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetDueDateFragment on Issue {\n  duedate {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetTotalCountFragment on GQLIssueConnection {\n  totalCount\n  __typename\n}\n"""
    variables = {"first": 50, "last": 50, "jql": "project = 'DX' AND type = Bug AND fixVersion = 'SSO 1.5.1' ORDER BY created DESC", "amountOfIds": 1000, "isMaxResultsLimitEnabled": True}
    url = 'https://rct-ai.atlassian.net/rest/gira/1/?operation=IssueListQuery'
    resp = requests.post(url=url, json={"operationName":"IssueListQuery","query": query,"variables":variables}, headers=header, cookies=cookie)
    print(resp.json())
    i = 0
    all = len(resp.json()['data']['issueIds']['nodes'])
    upUnFix = []
    P0UnFix = []
    P1UnFix = []
    AllUnFix = []
    while i < len(resp.json()['data']['issueIds']['nodes']):
        priority = resp.json()['data']['issues']['nodes'][i]['priority']['name']
        status = resp.json()['data']['issues']['nodes'][i]['status']['name']
        name = [str(resp.json()['data']['issues']['nodes'][i]['summary']['textValue'])]
        if priority == '阻止程序' and status == '打开' or priority == '阻止程序' and status == 'In Dev':
            upUnFix += name
        if priority == 'P0-重要紧急' and status == '打开' or priority == 'P0-重要紧急' and status == 'In Dev':
            P0UnFix += name
        if priority == 'P1-重要不紧急' and status == '打开' or priority == 'P1-重要不紧急' and status == 'In Dev':
            P1UnFix += name
        if status == '打开' or status == 'In Dev':
            AllUnFix += name
        i += 1
    print(upUnFix)
    print(P0UnFix)
    print(P1UnFix)
    print(AllUnFix)
    print(all)

    """修改格式推送至飞书"""
    upUnFixNum = len(upUnFix)
    P0UnFixNum = len(P0UnFix)
    P1UnFixNum = len(P1UnFix)
    AllUnFixNum = len(AllUnFix)

    upUnFixTitle = "\n*".join(upUnFix)
    P0UnFixTitle = "\n*".join(P0UnFix)
    P1UnFixTitle = "\n*".join(P1UnFix)
    AllUnFixTitle = "\n*".join(AllUnFix)

    today = time.strftime("%Y-%m-%d",time.localtime())
    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "tag": "div",
                "text": {
                        "content": "📒 **10/11 SSO & DMA Purchase On Mobile**",
                        "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Above Unfixed Bugs  **{upUnFixNum}**\n*{upUnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Unfixed Bugs  **{P0UnFixNum}**\n*{P0UnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P1 Unfixed Bugs  **{P1UnFixNum}**\n*{P1UnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of All Unfixed Bugs  **{AllUnFixNum}**\n*{AllUnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Total Number Of Bugs  **{all}**",
                    "tag": "lark_md"
                }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": "🔍 CLICK HERE FOR DETAILS",
                                    "tag": "lark_md"
                            },
                            "url": "https://rct-ai.atlassian.net/jira/software/c/projects/DX/boards/43",
                            "type": "default",
                            "value": {}
                    }],
                    "tag": "action"
            }],
            "header": {
                    "title": {
                            "content": f"🔔  {today} BUG INFO",
                            "tag": "plain_text"
                    }
            }
        }
    }
    #send = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/0da6a938-d932-4e91-86a0-86a3d43ecf11',json.dumps(p))
    send = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/0df503a9-e556-4452-b869-80c6c1894665',json.dumps(p))
    print(send.status_code,send.json())
    return send

if __name__ == '__main__':
    bugtool()
