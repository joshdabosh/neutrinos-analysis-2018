import NeutrinoBlazarMatching as nbm
import json

"""
Does not work anymore as this was the first results tester, our functions
have then changed
"""


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


print("completed testing")
print("total successes: {}".format(succ))
print("total fails: {}".format(fail))
print("successes to total ratio: {}".format(succ/(succ+fail)))
