def sublists(lst):
    if not lst:
        return [[]]
    rest = sublists(lst[1:])
    return rest + [lst[:1] + x for x in rest]

# Main Program
lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

for lst in lists:
    print(f"Sublists of {lst}: {sublists(lst)}")
