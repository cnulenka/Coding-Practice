class UndergroundSystem:

    def __init__(self):
        self.customerTravelling = dict()
        self.tourAvg = defaultdict(float)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        if id not in self.customerTravelling:
            self.customerTravelling[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        
        if id in self.customerTravelling:
            startStation, startTime = self.customerTravelling[id]
            
            # compute tour average
            tourId = startStation + '_' + endStation
            
            if tourId in self.tourAvg:
                prevAvg, numTravelers = self.tourAvg[tourId]
                newAvg = ((prevAvg*numTravelers) + (endTime-startTime))/(numTravelers+1)
                self.tourAvg[tourId] = (newAvg, numTravelers+1)
            else:
                self.tourAvg[tourId] = (endTime-startTime, 1)
            
            # remove passenger
            self.customerTravelling.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tourId = startStation + '_' + endStation
        Avg, numTravelers = self.tourAvg[tourId]
        return Avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)