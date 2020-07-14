def angleClock(self, hour: int, minutes: int) -> float:
        return 180 - abs(abs(11*minutes/2 - hour*30) - 180)
