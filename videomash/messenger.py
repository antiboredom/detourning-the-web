import random
import paramiko
from twilio.rest import TwilioRestClient
import videomash

sid = ''
token = ''


nouns = open('nouns.txt', 'r').readlines()
word1 = random.choice(nouns).strip()
word2 = random.choice(nouns).strip()
print word1, word2

outfile = word1+word2+'.mp4'
videomash.mash(word1, word2, outfile)

username = ''
password = ''
host = "vidds.lav.io"                    #hard-coded
port = 22
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

path = './vidds.lav.io/' + outfile
sftp.put(outfile, path)

sftp.close()
transport.close()

url = 'http://vidds.lav.io/' + outfile
print url

body = word1 + ' ' + word2 + ': ' + url

client = TwilioRestClient(sid, token)
message = client.messages.create(to="+12024566213", from_="+13473346912", body=body)
