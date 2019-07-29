import copy

from .centroid import centroid
from .invariant import get_coords
from .rhumb_bearing import rhumb_bearing
from .rhumb_destination import rhumb_destination
from .rhumb_distance import rhumb_distance


def transform_rotate(geojson, angle, options):
    """
    Rotates any geojson Feature or Geometry of a specified angle, around its `centroid` or a given `pivot` point;
    all rotations follow the right-hand rule: https://en.wikipedia.org/wiki/Right-hand_rule
    """
    # Optional parameters
    if options is None:
        options = {}
    if type(options) == object:
        raise Exception('options is invalid')
    pivot = options.get('pivot')
    mutate = options.get('mutate')

    # Input validation
    if not geojson:
        raise Exception('geojson is required')
    if angle is None:
        raise Exception('angle is required')

    # Shortcut no-rotation
    if angle == 0:
        return geojson

    # Use centroid of GeoJSON if pivot is not provided
    if not pivot:
        pivot = centroid(geojson)

    # Clone geojson to avoid side effects
    if not mutate:
        geojson = copy.deepcopy(geojson)

    # Rotate each coordinate
    new_coords_list = []
    for k, point_coords in enumerate(geojson.coords):
        initial_angle = rhumb_bearing(pivot, point_coords)
        final_angle = initial_angle + angle
        distance = rhumb_distance(pivot, point_coords)
        new_coords = get_coords(rhumb_destination(pivot, distance, final_angle))
        new_coords_list.append(new_coords)
    return type(geojson)(new_coords_list)
