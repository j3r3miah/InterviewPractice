

def best_route(ranges):
    # ranges = sorted([(a[1], a[0]) for a in ranges])
    ranges = sorted(ranges, key=lambda x: x[1])

    rv = []
    last_end = -10**5
    
    for o in ranges:
        start, end = o
        if start >= last_end:
            rv.append(o)
            last_end = end

    return rv



deliveries = [
    (1,8),
    (2,3),
    (3,4),
    (2,4),
    (3,7),
    (6,10),
]

print(best_route(deliveries))
