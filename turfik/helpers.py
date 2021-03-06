import math


earth_radius = 6371008.8

# Unit of measurement factors using a spherical (non-ellipsoid) earth radius.
factors = {
    'centimeters': earth_radius * 100,
    'centimetres': earth_radius * 100,
    'degrees': earth_radius / 111325,
    'feet': earth_radius * 3.28084,
    'inches': earth_radius * 39.370,
    'kilometers': earth_radius / 1000,
    'kilometres': earth_radius / 1000,
    'meters': earth_radius,
    'metres': earth_radius,
    'miles': earth_radius / 1609.344,
    'millimeters': earth_radius * 1000,
    'millimetres': earth_radius * 1000,
    'nauticalmiles': earth_radius / 1852,
    'radians': 1,
    'yards': earth_radius / 1.0936,
}


def feature(geom, properties: dict = None, options: dict = None):
    """
    Wraps a GeoJSON {@link Geometry} in a GeoJSON {@link Feature}
    """
    if properties is None:
        properties = {}
    if options is None:
        options = {}
    feat = {
        'type': "Feature",
    }
    if options.get('id') is not None:
        feat['id'] = options.get('id')
    if options.get('bbox'):
        feat['bbox'] = options.get('bbox')
    feat['properties'] = properties
    feat['geometry'] = geom
    return feat

def feature_collection(features, options: dict = None):
    if options is None:
        options = {}
    fc = {
        'type': 'FeatureCollection',
    }
    if options.get('id') is not None:
        fc['id'] = options.get('id')
    if options.get('bbox'):
        fc['bbox'] = options.get('bbox')
        fc['features'] = features
    return fc


def point(coordinates, properties=None, options: dict = None):
    """
    Creates a {@link Point} {@link Feature} from a Position
    """
    if options is None:
        options = {}
    geom = {
        'type': 'Point',
        'coordinates': coordinates,
    }
    return feature(geom, properties, options)


def line_string(coordinates, properties=None, options: dict = None):
    """
    Creates a {@link Point} {@link Feature} from a Position
    """
    if len(coordinates) < 2:
        raise Exception('coordinates must be an array of two or more positions')
    if options is None:
        options = {}
    geom = {
        'type': 'LineString',
        'coordinates': coordinates,
    }
    return feature(geom, properties, options)


def polygon(coordinates, properties=None, options: dict = None):
    if options is None:
        options = {}
    for ring in coordinates:
        if len(ring) < 4:
            raise Exception('Each LinearRing of a Polygon must have 4 or more Positions.')
        for j in range(len(ring[-1])):
            # Check if first point of Polygon contains two numbers
            if ring[-1][j] != ring[0][j]:
                raise Exception('First and last Position are not equivalent.')
    geom = {
        'type': 'Polygon',
        'coordinates': coordinates,
    }
    return feature(geom, properties, coordinates)

def geometry(type, coordinates, options: dict = None):
    if options is None:
        options = {}
    if type == 'Point':
        return point(coordinates)['geometry']
    elif type == 'LineString':
        return line_string(coordinates)['geometry']
    elif type == 'Polygon':
        return polygon(coordinates)['geometry']
    else:
        raise NotImplemented()


def degrees_to_radians(degrees: float) -> float:
    """
    Converts an angle in degrees to radians
    """
    radians = degrees % 360
    return radians * math.pi / 180


def radians_to_degrees(radians: float) -> float:
    """
    Converts an angle in radians to degrees
    """
    degrees = radians % (2 * math.pi)
    return degrees * 180 / math.pi


def length_to_radians(distance: float, units: str = "kilometers") -> float:
    """
    Convert a distance measurement (assuming a spherical Earth) from a real-world unit into radians
    Valid units: miles, nauticalmiles, inches, yards, meters, metres, kilometers, centimeters, feet
    """
    factor = factors.get(units)
    if not factor:
        raise Exception("{0} units is invalid".format(units))
    return distance / factor


def radians_to_length(radians: float, units: str = "kilometers") -> float:
    """
    Convert a distance measurement (assuming a spherical Earth) from radians to a more friendly unit.
    Valid units: miles, nauticalmiles, inches, yards, meters, metres, kilometers, centimeters, feet
    """
    factor = factors.get(units)
    if not factor:
        raise Exception("{0} units is invalid".format(units))
    return radians * factor


def convert_length(length: float, original_unit: str = "kilometers", final_unit: str = None) -> float:
    """
    Converts a length to the requested unit.
    Valid units: miles, nauticalmiles, inches, yards, meters, metres, kilometers, centimeters, feet
    """
    if final_unit is None:
        final_unit = 'kilometers'
    if original_unit is None:
        original_unit = 'kilometers'
    if not length >= 0:
        raise Exception("length must be a positive number")
    return radians_to_length(length_to_radians(length, original_unit), final_unit)
