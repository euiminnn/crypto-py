import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2122874603954-2146687030304-YQblwimwWlCwob02TUO0nLM6"
 
post_message(myToken,"#coin_alert","먕이 부자되기 프로젝트 시작!")
