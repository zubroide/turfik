from typing import List


def get_coord(coord) -> List[float]:
    """
    Unwrap a coordinate from a Point Feature, Geometry or a single coordinate
    """
    if not coord:
        raise Exception("coord is required")

    if type(coord) == dict:
        if coord.get('type') == "Feature" and coord.get('geometry') is not None and coord.get('geometry').get('type') == "Point":
            return coord.get('geometry').get('coordinates')
        if coord.get('type') == "Point":
            return coord.coordinates
    if (type(coord) == list or type(coord) == tuple) and len(coord) >= 2 \
            and type(coord[0]) != list and type(coord[0]) != tuple \
            and type(coord[1]) != list and type(coord[1]) != tuple:
        return coord

    raise Exception("coord must be GeoJSON Point or an Array of numbers")


def get_coords(coords):
    """
    Unwrap coordinates from a Feature, Geometry Object or an Array
    """
    if type(coords) == list:
        return coords

    # Feature
    if coords.get('type') == "Feature":
        if coords.get('geometry') is not None:
            return coords.get('geometry').get('coordinates')
    else:
        # Geometry
        if coords.get('coordinates'):
            return coords.get('coordinates')

    raise Exception("coords must be GeoJSON Feature, Geometry Object or an Array")
