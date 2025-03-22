from enum import Enum
import math
from decimal import Decimal

class AirCraft(Enum):
    L = 1
    M = 2.5
    H = 5
    J = 12
def distance(lat_from: Decimal, long_from: Decimal,  lat_to: Decimal, long_to: Decimal) -> Decimal:
   math.radians(lat_to)
   math.radians(lat_from)
   math.radians(long_to)
   math.radians(long_from)
   D = R*(arcos(sin(lat_from)*sin(lat_to)+cos(lat_from)*cos(lat_to)*(cos(long_from-long_to))))
   return D


def emission(distance: Decimal, aircraft: AirCraft) -> Decimal:
    resultat= 5*(1838/800)*3.15*2
    return resultat
print(emission)