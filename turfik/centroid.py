from .helpers import point


def centroid(geojson, options: dict = None):
    """
    Takes one or more features and calculates the centroid using the mean of all vertices.
    This lessens the effect of small islands and artifacts when calculating the centroid of a set of polygons
    """
    if options is None:
        options = {}
    x_sum = 0
    y_sum = 0
    length = 0
    for coord in geojson:
        x_sum += coord[0]
        y_sum += coord[1]
        length += 1
    return point([x_sum / length, y_sum / length], options.get('properties'))
