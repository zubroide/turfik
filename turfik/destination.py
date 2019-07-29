import math

from .helpers import degrees_to_radians, length_to_radians, radians_to_degrees, point
from .invariant import get_coord


def destination(origin, distance: float, bearing: float, options: dict = None):
    """
    Takes a {@link Point} and calculates the location of a destination point given a distance in
    degrees, radians, miles, or kilometers; and bearing in degrees.
    This uses the [Haversine formula](http://en.wikipedia.org/wiki/Haversine_formula) to account for global curvature.
    """
    if options is None:
        options = {}

    # Handle input
    coordinates1 = get_coord(origin)
    longitude1 = degrees_to_radians(coordinates1[0])
    latitude1 = degrees_to_radians(coordinates1[1])
    bearing_rad = degrees_to_radians(bearing)
    radians = length_to_radians(distance, options.get('units'))

    # Main
    latitude2 = math.asin(math.sin(latitude1) * math.cos(radians) +
                          math.cos(latitude1) * math.sin(radians) * math.cos(bearing_rad))
    longitude2 = longitude1 + math.atan2(math.sin(bearing_rad) * math.sin(radians) * math.cos(latitude1),
                                         math.cos(radians) - math.sin(latitude1) * math.sin(latitude2))
    lng = radians_to_degrees(longitude2)
    lat = radians_to_degrees(latitude2)

    return point([lng, lat], options.get('properties'))
