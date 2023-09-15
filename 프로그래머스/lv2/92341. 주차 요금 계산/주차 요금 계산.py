from collections import defaultdict

class Car:
    def __init__(self, num: int, I: str, O: str = '23:59') -> None:
        self.num: int = num
        self.I: list[int] = list(map(int, I.split(':')))
        self.O: list[int] = list(map(int, O.split(':')))
        self.time = self.stay()
    
    def stay(self) -> int:
        H, M = 0, 0
        ih, im = self.I
        oh, om = self.O
        if om >= im:
            M = om - im
        else:
            oh -= 1
            om += 60
            M = om - im
        H = oh - ih
        return H * 60 + M

def solution(fees, records):
    answer = []
    parking: defaultdict[int, list[Car]] = defaultdict(list)
    for rec in records:
        T, num, status = rec.split()
        num = int(num)
        if status == 'IN':
            parking[num].append(Car(num, T))
        else:
            car = parking[num][-1]
            car.O = list(map(int, T.split(':')))
            car.time = car.stay()
    for num, cars in sorted(parking.items()):
        time = sum([c.time for c in cars])
        answer.append(calc_cost(fees, time))
    return answer

def calc_cost(fees: list, time: int) -> int:
    base_M, base_F, unit_M, unit_F = fees
    if time <= base_M: 
        return base_F
    else:
        time -= base_M
        quot, rem = divmod(time, unit_M)
        if rem != 0:
            quot += 1
        return base_F + quot * unit_F