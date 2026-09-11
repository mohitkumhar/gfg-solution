class Solution:
    def minMeetingRooms(self, start, end):
        # code here

        events = []

        for i in range(len(start)):
            events.append((start[i], 1))
            events.append((end[i], -1))

        events.sort()

        maxRoom = 0
        currRoom = 0

        for event in events:
            currRoom += event[1]
            maxRoom = max(maxRoom, currRoom)

        return maxRoom
