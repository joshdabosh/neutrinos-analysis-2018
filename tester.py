import NeutrinoBlazarMatching as nbm
import json

blazars = json.loads(open("data/blazar2.json").read())

succ = 0
fail = 0

for b in blazars:
    if b['z'] == "0":
        pass
    else:
        res = nbm.main(b["ra"], float(b["de"]))

        found = False

        for r in res:
            if r["dist"] < 1:
                succ += 1
                found = True

        if not found:
            fail += 1
