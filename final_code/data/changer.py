import json

backups = json.loads(open("blazar2.json").read())

for b in range(len(backups)):
    if backups[b]["ra"] == "77.35817":
        backups[b]["z"] = "0.336"

with open("blazar2.json", "w") as f:
    f.write(json.dumps(backups))
