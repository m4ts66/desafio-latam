import json, requests, re

def code_gpt(message, agent):
    headers = {"Authorization": f"Bearer {'6fbfff41-7a5d-4c45-a146-61d06154e275'}"}
    body = {
        "agent": agent,
        "messages": [
            { "role": "user", "content": message }
        ]
    }
    completion_call = requests.post('https://api.codegpt.co/v1/completion', json=body, headers=headers)
    if completion_call.status_code == 200:
        return parse_completion_response(completion_call.text)
    else:
        return f"Error, {json.loads(completion_call.text)['detail']}"

#COMPLETION FUNCTION
def parse_completion_response(completion_text):
    pattern = r"data: (.+)"
    matches = re.findall(pattern, completion_text)
    completion = ''.join(matches)
    return completion