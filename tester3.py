import NeutrinoBlazarMatching as nbm
import operator


"""
Uses IceCube's data that lead to the discovery of blazar TXS 0506+056.

Counts the number of times a blazar was returned as the closest from
our main function after a neutrino's RA and DEC were given
"""

events_listing = "40 59 79 86a 86b 86c".split()

succ_a, fails_a, succ_v, fails_v, succ_i, fails_i = 0, 0, 0, 0, 0, 0

counts_a, counts_v, counts_i = {}, {}, {}

for suffix in events_listing:
    print("starting work on events_IC{}.txt...".format(suffix))
    f = open("txs0506_events/events_IC{}.txt".format(suffix)).readlines()

    events = [i.split() for i in f][1:]

    for ev in events:
        a, v, i = nbm.main(ev[1], ev[2], verbose=False)

        # PCCS1217G195.39- is the name for the TXS blazar

        b_name = a[0]["blazar"]["a"]

        if b_name in counts_a.keys():
            counts_a[b_name] += 1
        else:
            counts_a[b_name] = 1

        b_name = v[0]["blazar"]["a"]

        if b_name in counts_v.keys():
            counts_v[b_name] += 1
        else:
            counts_v[b_name] = 1

        if not len(i) > 0:
            continue
        
        b_name = i[0]["blazar"]["a"]

        if b_name in counts_i.keys():
            counts_i[b_name] += 1
        else:
            counts_i[b_name] = 1

print()

print("RESULTS")
print("-"*len("RESULTS"))

b_template = "{name: <20}{count: <5}"

# magic

print("Blazar recorded counts in angular comparison list:")
print(b_template.format(
    name="Blazar name",
    count="Count"
    ))

for name, count in reversed(sorted(counts_a.items(), key=operator.itemgetter(1))):
    print(b_template.format(name=name, count=count))

print()

print("Blazar recorded counts in vector comparison list:")
print(b_template.format(
    name="Blazar name",
    count="Count"
    ))

for name, count in reversed(sorted(counts_v.items(), key=operator.itemgetter(1))):
    print(b_template.format(name=name, count=count))

print()

print("Blazar recorded counts in intersect list:")
print(b_template.format(
    name="Blazar name",
    count="Count"
    ))

for name, count in reversed(sorted(counts_i.items(), key=operator.itemgetter(1))):
    print(b_template.format(name=name, count=count))
