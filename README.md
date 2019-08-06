# Turfik

Turfik is implementation of Turf.js library on Python.

## Installation

```bash
pip install turfik
```

## Requirements

Python 3.5+

## How to use

```python
import turfik
from shapely.geometry import Point

point = Point(37.622504, 55.753215)  # Point(longitude, latitude)

translatedPoint = turfik.transform_translate(point, 100, 90, {
    "units": "meters",
})
```

## Features

- [ ] `along`
- [ ] `area`
- [ ] `bbox`
- [ ] `bbox-clip`
- [ ] `bbox-polygon`
- [ ] `bearing`
- [ ] `bezier-spline`
- [ ] `boolean-clockwise`
- [ ] `boolean-contains`
- [ ] `boolean-crosses`
- [ ] `boolean-disjoint`
- [ ] `boolean-equal`
- [ ] `boolean-overlap`
- [ ] `boolean-parallel`
- [ ] `boolean-point-in-polygon`
- [ ] `boolean-point-on-line`
- [ ] `boolean-within`
- [ ] `buffer`
- [ ] `center`
- [ ] `center-mean`
- [ ] `center-median`
- [ ] `center-of-mass`
- [x] `centroid`
- [ ] `circle`
- [ ] `clean-coords`
- [ ] `clone`
- [ ] `clusters`
- [ ] `clusters-dbscan`
- [ ] `clusters-kmeans`
- [ ] `collect`
- [ ] `combine`
- [ ] `concave`
- [ ] `convex`
- [x] `destination`
- [ ] `difference`
- [ ] `dissolve`
- [x] `distance`
- [ ] `ellipse`
- [ ] `envelope`
- [ ] `explode`
- [ ] `flatten`
- [ ] `flip`
- [ ] `great-circle`
- [x] `helpers`
- [ ] `hex-grid`
- [ ] `interpolate`
- [ ] `intersect`
- [x] `invariant`
- [ ] `isobands`
- [ ] `isolines`
- [ ] `kinks`
- [ ] `length`
- [ ] `line-arc`
- [ ] `line-chunk`
- [ ] `line-intersect`
- [ ] `line-offset`
- [ ] `line-overlap`
- [ ] `line-segment`
- [ ] `line-slice`
- [ ] `line-slice-along`
- [ ] `line-split`
- [ ] `line-to-polygon`
- [ ] `mask`
- [ ] `meta`
- [ ] `midpoint`
- [ ] `nearest-point`
- [ ] `nearest-point-on-line`
- [ ] `nearest-point-to-line`
- [ ] `planepoint`
- [ ] `point-grid`
- [ ] `point-on-feature`
- [ ] `point-to-line-distance`
- [ ] `points-within-polygon`
- [ ] `polygon-tangents`
- [ ] `polygon-to-line`
- [ ] `polygonize`
- [ ] `projection`
- [ ] `random`
- [ ] `rewind`
- [x] `rhumb-bearing`
- [x] `rhumb-destination`
- [x] `rhumb-distance`
- [ ] `sample`
- [ ] `sector`
- [ ] `shortest-path`
- [ ] `simplify`
- [ ] `square`
- [ ] `square-grid`
- [ ] `standard-deviational-ellipse`
- [ ] `tag`
- [ ] `tesselate`
- [ ] `tin`
- [x] `transform-rotate`
- [ ] `transform-scale`
- [x] `transform-translate`
- [ ] `triangle-grid`
- [ ] `truncate`
- [ ] `union` (use `shapely.ops.cascaded_union`)
- [ ] `unkink-polygon`
- [ ] `voronoi`

## License

MIT

## How to contribute

Open [Turf.js package list](https://github.com/Turfjs/turf/tree/master/packages).

Select one of not ported package. 
List of not ported packages see above (without checkbox).
For example, [`transform-scale`](https://github.com/Turfjs/turf/blob/master/packages/turf-transform-scale/index.js).

Create new file in Turfik. For example above filename will be `transform_scale.py`.
Translate JS code into Python code. Don't forget to include new file into `__init__.py`, for example above `from .transform_scale import *`.

Create pull request.
