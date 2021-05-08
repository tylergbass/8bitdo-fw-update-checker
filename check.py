import requests
import hashlib

headers = {
	"type": "8",
	"beta": "1"
}
r = requests.post("http://dl.8bitdo.com:8080/firmware/select", headers=headers)

updatetext = "8BitDo Wireless USB Adapter firmware available:<br />"
for item in r.json()["list"]:
	updatetext += str(round(item["version"], 4))
	if item["beta"] == '1':
		updatetext += " beta"
	updatetext += " (" + item["date"] + "):<br />"
	updatetext += item["readme_en"].replace("\n", "<br />") + "<br /><br />"

changeloghash = hashlib.sha1(updatetext.encode('utf8')).hexdigest()

with open("lastresponse.txt", "r") as file:
	if file.read() != changeloghash:
		notify = requests.post("https://maker.ifttt.com/trigger/[event_name]/with/key/[key]", data={"value1": updatetext})

with open("lastresponse.txt", "w") as file:
	file.write(changeloghash)