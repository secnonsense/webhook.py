import requests
import sys
import json

def webhook(uri,message):
    title = "My Title"
    colors={"blue": "#142954","yellow": "#FFFF00","red": "#FF0000", "hotpink": "#FF00FF","green": "#85FF7A"}
    color=colors['yellow']
    body = json.dumps({"pretext": title, "text": message, "color": color})
    try:
        r = requests.post(uri, data=body, headers={"Content-type": "application/json"})
        if r.status_code != 200:
            sys.stderr.write(f"Response code: {r.status_code} {r.text} \n {r.__dict__} \n")
        else:
            print(r.text)
    except Exception as error:
            sys.stderr.write("Exception occurred retrieving data from cloudflare API:. Error Code: {}\n".format(error))

def main():
    uri = "https://hooks.slack.com/services/XXXXXXXX/YYYYYYYYYYYY/ZZZZZZZZZZZZZZZ"
    message="testing one two three!!!"
    webhook(uri,message)

if __name__ == "__main__":
    main()

