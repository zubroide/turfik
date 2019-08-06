import typing
import math

from .invariant import get_coord
from .helpers import radians_to_length, degrees_to_radians


def distance(from_coord: typing.List[float], to_coord: typing.List[float], units: str = "kilometers") -> float:
    coordinates1 = get_coord(from_coord)
    coordinates2 = get_coord(to_coord)
    d_lat = degrees_to_radians((coordinates2[1] - coordinates1[1]))
    d_lon = degrees_to_radians((coordinates2[0] - coordinates1[0]))
    lat1 = degrees_to_radians(coordinates1[1])
    lat2 = degrees_to_radians(coordinates2[1])

    a = math.pow(math.sin(d_lat / 2), 2) + math.pow(math.sin(d_lon / 2), 2) * math.cos(lat1) * math.cos(lat2)

    return radians_to_length(2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)), units)
