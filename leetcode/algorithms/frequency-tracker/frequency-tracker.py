from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self._m = defaultdict(int)
        self._mf = defaultdict(set)

    def add(self, number: int) -> None:
        if len(self._mf[self._m[number]]):
            self._mf[self._m[number]].remove(number)
        self._m[number] += 1
        self._mf[self._m[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if self._m[number] == 0:
            return
        if len(self._mf[self._m[number]]):
            self._mf[self._m[number]].remove(number)
        self._m[number] -= 1
        if self._m[number] != 0:
            self._mf[self._m[number]].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self._mf[frequency]) != 0
