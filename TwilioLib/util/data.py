
import requests, os, json, subprocess

from twilio.rest import Client
import os


class TW:
    account_sid = os.getenv('TWILIO_API_KEY')
    auth_token = os.environ.get('TWILIO_API_SECRET')

    def __init__(self):
        self.client = Client(self.account_sid, self.auth_token)

    def GetList(self):
        count = 1
        out = []
        for sms in self.client.messages.list():
            if sms.direction == "inbound":
                out.append([sms.date_sent,sms.sid,sms.from_,sms.body])
            count += 1
            if count > 20:
                return out



class SRE:
    url = "https://api.npe.nike.com/v1/runtimes"

    def GetToken(self):
        file = os.getenv("HOME") + "/.npe/auth.yaml"
        with open(file) as f:
            r = f.read().split('\n')
            token = r[1].split('accesstoken: ')[1]
        return token

    def runtimes(self):
        response = requests.get(self.url,
                            headers={'Authorization': 'Bearer %s' % self.GetToken()})
        y = json.loads(response.text)
        return y["data"]


    def thing(self):
        return "thing"


class AWScmds:
    encoding = 'utf-8'
    def getVPCcount(self):
        cmd = """aws ec2 --output text --query 'Vpcs[*].{VpcId:VpcId,Name:Tags[?Key==`Name`].Value|[0],CidrBlock:CidrBlock}' describe-vpcs --profile 754757074681-NIKE.SSO.AdminRole|wc"""
        count = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode(self.encoding).split()[0]
        return int(count)

    def updateKubeconfig(self):
        cmd = """aws eks --region us-west-2 update-kubeconfig --name npe-prod-us-west-2 --profile 623244905753-NIKE.SSO.AdminRole"""
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode(self.encoding)
        return result

    def getPods(self):
        cmd = """kubectl get pods --sort-by=.metadata.creationTimestamp -A --no-headers"""
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode(self.encoding)
        result = result.split('\n')
        return result






class Junk:
    def stuff(self):
        return "we stuff"


if __name__ == "__main__":
    print("here")
