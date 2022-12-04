class UndergroundSystem:

    """
    1396. Design Underground System

    Input
    ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

    checkIns = {
        45: ("Leyton",3),
        32: ("Paradise",8),
        27: ("Leyton",10),
    }
    Average = {
        (Leyton, Waterloo): (22, 2)
        (Paradise,Cambridge): (14, 1)
    }
    """

    def __init__(self):
        self.checkIns = dict()
        self.average = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None: # 32,"Cambridge",22
        startStation, startTime = self.checkIns[id] # "Paradise",8
        key = (startStation, stationName)
        acc_time, count_ = self.average[key] # (0, 0)
        acc_time += t - startTime # 22 - 8 14
        count_ += 1
        self.average[key] = (acc_time, count_)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        acc_time, count_ = self.average[key]
        return acc_time/count_


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
