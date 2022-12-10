"""Prepare sector poligons."""

from geopy.distance import geodesic


def make_sector_polygons(atoll_site_data, technology):
    """
    Make sectors polygons.

    Args:
        atoll_site_data (list): a list of namedtuples
        technology (str): network technology

    Returns:
        list: a list of dicts with coordinates to draw antenna direction
    """
    dist = {
        'GSM': 0.4,
        'WCDMA': 0.3,
        'LTE': 0.2,
        'NR': 0.1,
    }

    colors = {
        'GSM': 'green',
        'WCDMA': 'red',
        'LTE': 'yellow',
        'NR': 'blue',
    }

    sector_points = []
    azimut_delta_left = -30
    azimut_delta_right = 30

    for row in atoll_site_data:
        base_point = (row.latitude, row.longitude)
        point1 = geodesic(kilometers=dist[technology]).destination(
            base_point,
            bearing=row.azimut + azimut_delta_left,
        )
        point2 = geodesic(kilometers=dist[technology]).destination(
            base_point,
            bearing=row.azimut + azimut_delta_right,
        )
        sector_points.append(
            {
                'point0': base_point,
                'point1': (point1.latitude, point1.longitude),
                'point2': (point2.latitude, point2.longitude),
                'color': colors[technology],
            },
        )

    return sector_points
