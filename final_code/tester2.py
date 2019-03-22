import NeutrinoBlazarMatching as nbm

events_listing = "40 59 79 86a 86b 86c".split()

succ_a, fails_a, succ_v, fails_v, succ_i, fails_i = 0, 0, 0, 0, 0, 0

for suffix in events_listing:
    print("starting work on events_IC{}.txt...".format(suffix))
    f = open("txs0506_events/events_IC{}.txt".format(suffix)).readlines()

    events = [i.split() for i in f][1:]

    for ev in events:
        a, v, t = nbm.main(ev[1], ev[2], verbose=False)

        # PCCS1217G195.39- is the name for the TXS blazar

        found = False

        #for b in a:
        if a[0]["blazar"]["a"] == "PCCS1217G195.39-":
            found = True
            succ_a += 1

        if not found:
            fails_a += 1

        ####
            
        found = False

        #for b in v:
        if v[0]["blazar"]["a"] == "PCCS1217G195.39-":
            found = True
            succ_v += 1

        if not found:
            fails_v += 1

        ####

print()

print("RESULTS")
print("-"*len("RESULTS"))

print("angular: {} successes to {} fails".format(succ_a, fails_a))
print("vector: {} successes to {} fails".format(succ_v, fails_v))
