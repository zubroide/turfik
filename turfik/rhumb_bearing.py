import math
from typing import List

from .helpers import radians_to_degrees, degrees_to_radians
from .invariant import get_coord


def rhumb_bearing(start, end, options=None) -> float:
    """
    Takes two {@link Point|points} and finds the bearing angle between them along a Rhumb line
    i.e. the angle measured in degrees start the north line (0 degrees)
    """
    if options is None:
        options = {}
    if options.get('final'):
        bear360 = _calculate_rhumb_bearing(get_coord(end), get_coord(start))
    else:
        bear360 = _calculate_rhumb_bearing(get_coord(start), get_coord(end))

    bear180 = - (360 - bear360) if bear360 > 180 else bear360

    return bear180


def _calculate_rhumb_bearing(cfrom: List[float], to: List[float]):
    """
    Returns the bearing from ‘this’ point to destination point along a rhumb line.
    Adapted from Geodesy: https://github.com/chrisveness/geodesy/blob/master/latlon-spherical.js
    """
    # φ => phi
    # Δλ => delta_lambda
    # Δψ => delta_psi
    # θ => theta
    phi1 = degrees_to_radians(cfrom[1])
    phi2 = degrees_to_radians(to[1])
    delta_lambda = degrees_to_radians((to[0] - cfrom[0]))
    # if deltaLambdaon over 180° take shorter rhumb line across the anti-meridian:
    if delta_lambda > math.pi:
        delta_lambda -= 2 * math.pi
    if delta_lambda < -math.pi:
        delta_lambda += 2 * math.pi

    delta_psi = math.log(math.tan(phi2 / 2 + math.pi / 4) / math.tan(phi1 / 2 + math.pi / 4))

    theta = math.atan2(delta_lambda, delta_psi)

    return (radians_to_degrees(theta) + 360) % 360
