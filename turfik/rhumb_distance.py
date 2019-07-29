import math
from typing import List

from .helpers import convert_length, earth_radius
from .invariant import get_coord


def rhumb_distance(start, end, options=None) -> float:
    """
    Calculates the distance along a rhumb line between two {@link Point|points} in degrees, radians,
    miles, or kilometers
    """
    if options is None:
        options = {}
    origin = get_coord(start)
    destination = get_coord(end)
    destination_list = list(destination)

    # compensate the crossing of the 180th meridian (https://macwright.org/2016/09/26/the-180th-meridian.html)
    # solution from https://github.com/mapbox/mapbox-gl-js/issues/3250#issuecomment-294887678
    destination_list[0] += -360 if destination_list[0] - origin[0] > 180 \
        else (360 if origin[0] - destination_list[0] > 180 else 0)
    distance_in_meters = _calculate_rhumb_distance(origin, destination_list)
    distance = convert_length(distance_in_meters, "meters", options.get('units'))
    return distance


def _calculate_rhumb_distance(origin: List[float], destination: List[float], radius: float = None):
    """
    Returns the distance travelling from ‘this’ point to destination point along a rhumb line.
    Adapted from Geodesy: https://github.com/chrisveness/geodesy/blob/master/latlon-spherical.js
    """
    # φ => phi
    # λ => lambda
    # ψ => psi
    # Δ => Delta
    # δ => delta
    # θ => theta

    radius = earth_radius if radius is None else radius
    # see www.edwilliams.org/avform.htm#Rhumb

    r = radius
    phi1 = origin[1] * math.pi / 180
    phi2 = destination[1] * math.pi / 180
    delta_phi = phi2 - phi1
    delta_lambda = abs(destination[0] - origin[0]) * math.pi / 180
    # if dLon over 180° take shorter rhumb line across the anti-meridian:
    if delta_lambda > math.pi:
        delta_lambda -= 2 * math.pi

    # on Mercator projection, longitude distances shrink by latitude; q is the 'stretch factor'
    # q becomes ill-conditioned along E-W line (0/0); use empirical tolerance to avoid it
    DeltaPsi = math.log(math.tan(phi2 / 2 + math.pi / 4) / math.tan(phi1 / 2 + math.pi / 4))
    q = delta_phi / DeltaPsi if abs(DeltaPsi) > 10e-12 else math.cos(phi1)

    # distance is pythagoras on 'stretched' Mercator projection
    delta = math.sqrt(delta_phi * delta_phi + q * q * delta_lambda * delta_lambda)  # angular distance in radians
    dist = delta * r

    return dist
