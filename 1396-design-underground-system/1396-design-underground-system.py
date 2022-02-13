class UndergroundSystem:

    def __init__(self):
        self.customerTravelling = dict()
        self.tourAvg = defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.customerTravelling[id] = [stationName, t]

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        
        startStation, startTime = self.customerTravelling[id]
            
        # compute tour average
        tourId = startStation + '_' + endStation
        self.tourAvg[tourId][0] += endTime-startTime
        self.tourAvg[tourId][1] += 1

        # remove passenger to save space
        self.customerTravelling.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tourId = startStation + '_' + endStation
        routeSum, numTravelers = self.tourAvg[tourId]
        return routeSum/numTravelers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)