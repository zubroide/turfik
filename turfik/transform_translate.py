import copy

from shapely.geometry import Point

from .invariant import get_coords
from .rhumb_destination import rhumb_destination


def transform_translate(geojson, distance, direction, options):
    """
    Moves any geojson Feature or Geometry of a specified distance along a Rhumb Line
    on the provided direction angle.
    """
    # Optional parameters
    if options is None:
        options = {}
    if type(options) == object:
        raise Exception('options is invalid')
    units = options.get('units')
    zTranslation = options.get('zTranslation')
    mutate = options.get('mutate')

    # Input validation
    if not geojson:
        raise Exception('geojson is required')

    # Shortcut no-motion
    if distance == 0 and zTranslation == 0:
        return geojson

    if direction is None:
        raise Exception('direction is required')

    # Invert with negative distances
    if distance < 0:
        distance = -distance
        direction = -direction

    # Clone geojson to avoid side effects
    if mutate is None or not mutate:
        geojson = copy.deepcopy(geojson)

    # Translate each coordinate
    new_coords_list = []
    if hasattr(geojson, 'coords'):
        coords = geojson.coords
    else:
        coords = geojson.get("geometry").get("coordinates")
    for k, point_coords in enumerate(coords):
        new_coords = get_coords(rhumb_destination(point_coords, distance, direction, {"units": units}))
        if zTranslation and len(new_coords) == 3:
            new_coords[2] += zTranslation
        new_coords_list.append(new_coords)

    if type(geojson) == Point:
        if zTranslation and len(new_coords_list[0]) == 3:
            return type(geojson)(new_coords_list[0][0], new_coords_list[0][1], new_coords_list[0][2])
        return type(geojson)(new_coords_list[0][0], new_coords_list[0][1])

    if type(geojson) != dict:
        return type(geojson)(new_coords_list)

    geojson.get("geometry")['coordinates'] = new_coords_list
    return geojson
