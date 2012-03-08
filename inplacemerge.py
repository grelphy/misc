def sort(x, start, end):
    if end - start <= 1: return
    mid = start + (end - start) / 2
    sort(x, start, mid)
    sort(x, mid, end)
    merge(x, start, mid, end)

def merge(x, start, mid, end):
    startheadA = mid    # Top of headA
    endheadA = mid      # Bottom of headA
    starttailA = start  # Top of tailA
    endtailA = mid      # Bottom of tailA
    startB = mid        # Top of B
    endB = end          # Bottom of B
    todo = end - start
    while todo > 0:
        haveheadA = endheadA - startheadA > 0
        haveB = endB - startB > 0
        # top of A
        if not haveheadA:
            a = x[starttailA]
        else:
            a = x[startheadA]
        # top of B
        if haveB:
            b = x[startB]
        if (not haveB) or a < b:
            if not haveheadA:
                starttailA += 1
            else:
                # Shift the head
                for i in xrange(startheadA, endheadA - 1):
                    x[i] = x[i + 1]
                x[endheadA - 1] = x[starttailA]
                x[starttailA] = a
                starttailA += 1
        else:
            # Pull from B
            x[startB] = x[starttailA]
            x[starttailA] = b
            startB += 1
            starttailA += 1
            endheadA += 1
        todo -= 1
        if endtailA - starttailA < 1:   # no tail, reset A
            starttailA = startheadA
            endtailA = endheadA
            startheadA = endtailA
            endheadA = endtailA
