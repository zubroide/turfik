import math
from typing import List

from .helpers import convert_length, earth_radius, degrees_to_radians, point
from .invariant import get_coord


def rhumb_destination(origin, distance: float, bearing: float, options: dict = None):
    """
    Returns the destination {@link Point} having travelled the given distance along a Rhumb line from the
    origin Point with the (varant) given bearing
    """
    if options is None:
        options = {}
    was_negative_distance = distance < 0
    distance_in_meters = convert_length(abs(distance), options.get('units'), "meters")
    if was_negative_distance:
        distance_in_meters = -abs(distance_in_meters)
    coords = get_coord(origin)
    destination = _calculate_rhumb_destination(coords, distance_in_meters, bearing)

    # compensate the crossing of the 180th meridian (https://macwright.org/2016/09/26/the-180th-meridian.html)
    # solution from https://github.com/mapbox/mapbox-gl-js/issues/3250#issuecomment-294887678
    destination[0] += -360 if destination[0] - coords[0] > 180 else (360 if coords[0] - destination[0] > 180 else 0)
    return point(destination, options.get('properties'))


def _calculate_rhumb_destination(origin: List[float], distance: float, bearing: float, radius: float = None):
    """
    Returns the destination point having travelled along a rhumb line from origin point the given
    distance on the  given bearing.
    Adapted from Geodesy: http://www.movable-type.co.uk/scripts/latlong.html#rhumblines
    """
    # φ => phi
    # λ => lambda
    # ψ => psi
    # Δ => Delta
    # δ => delta
    # θ => theta

    radius = earth_radius if radius is None else radius

    delta = distance / radius  # angular distance in radians
    lambda1 = origin[0] * math.pi / 180  # to radians, but without normalize to 𝜋
    phi1 = degrees_to_radians(origin[1])
    theta = degrees_to_radians(bearing)

    delta_phi = delta * math.cos(theta)
    phi2 = phi1 + delta_phi

    # check for some daft bugger going past the pole, normalise latitude if so
    if abs(phi2) > math.pi / 2:
        phi2 = math.pi - phi2 if phi2 > 0 else -math.pi - phi2

    delta_psi = math.log(math.tan(phi2 / 2 + math.pi / 4) / math.tan(phi1 / 2 + math.pi / 4))
    # E-W course becomes ill-conditioned with 0/0
    q = delta_phi / delta_psi if abs(delta_psi) > 10e-12 else math.cos(phi1)

    delta_lambda = delta * math.sin(theta) / q
    lambda2 = lambda1 + delta_lambda

    return [((lambda2 * 180 / math.pi) + 540) % 360 - 180, phi2 * 180 / math.pi]  # normalise to −180..+180°
