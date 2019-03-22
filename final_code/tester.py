import NeutrinoBlazarMatching as nbm
import json

"""
Runs through a list of blazars, checks to see our main function returns
the right blazar and has a distance of < 1 using the vector comparison
method.
"""


blazars = json.loads(open("data/blazar2.json").read())

succ = 0
succ_2 = 0
succ_3 = 0

fails = 0

for b in blazars:
    if b['z'] == "0":
        pass
    else:
        a, v, t = nbm.main(float(b["ra"]), float(b["de"]), verbose=False)

        r = v[0]
        if r["n_b_dist"] < 1 and r["blazar"]["a"] == b["a"]:
            succ += 1

        else:
            if v[1]["n_b_dist"] < 1 and v[1]["blazar"]["a"] == b["a"]:
                succ_2 += 1

            else:
                if v[2]["n_b_dist"] < 1 and v[2]["blazar"]["a"] == b["a"]:
                    succ_3 += 1

                else:
                    fails += 1


print("RESULTS")
print("-"*len("RESULTS"))

print("Total number of 1st closest blazar successes:", succ)
print("Total number of 2nd closest blazar successes:", succ_2)
print("Total number of 3rd closest blazar successes:", succ_3)
print("Total successes:", succ+succ_2+succ_3)
print("Total fails:", fails)








