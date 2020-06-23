art = {"Rolf", "anne", "jen"}
science = {"jen","charlie"}

art_not_science = art.difference(science)

print(art_not_science)
print("\n")

not_both = art.symmetric_difference(science)
print(not_both)
print("\n")

both = art.intersection(science)
print(both)
print("\n")

all_friends = art.union(science)
print(all_friends)
