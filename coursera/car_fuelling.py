def minRefills(stations, n, maxdistance):
    numRefills = 0
    currentPos = 0
    while currentPos < n + 1:
        lastRefillPos = currentPos
        while currentPos < n + 1 and stations[currentPos + 1] - stations[lastRefillPos] <= maxdistance:
            currentPos += 1
        if currentPos == lastRefillPos:
            return "IMPOSSIBLE"
        if currentPos < n + 1:
            print "Stopped at:", stations[currentPos]
            numRefills += 1
    return numRefills


stations = [200, 375, 550, 750]
dest = 900
start = 0

n = len(stations)

stations.insert(0, start)
stations.append(dest)
maxdistance = 400
print stations

print minRefills(stations, n, maxdistance)
