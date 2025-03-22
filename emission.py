from enum import Enum
import math
from decimal import Decimal

class AirCraft(Enum):
    L = 1
    M = 2.5
    H = 5
    J = 12


def emission(distance: Decimal, aircraft: AirCraft) -> Decimal:
    resultat= class Aircraft*(distance/800)*3.15*2
    return resultat
print(emission)
