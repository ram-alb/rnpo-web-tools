"""Make Atoll instance for working with Atoll WCDMA data."""

from collections import namedtuple

from utils.atoll import Atoll


def make_wcdma_atoll(site_id):
    """
    Make Atoll instance for working with Atoll WCDMA data.

    Args:
        site_id (str): 5 digits string

    Returns:
        Atoll instance
    """
    select_wcdma_site = """
        SELECT
            t.site_name,
            c.cell_id,
            s.latitude,
            s.longitude,
            t.antenna_name,
            t.height,
            t.azimut,
            t.fband,
            c.rnc_name
        FROM
            atoll_mrat.utransmitters t
            JOIN atoll_mrat.ucells c
                ON t.tx_id = c.tx_id
            JOIN atoll_mrat.sites s
                ON t.site_name = s.name
        WHERE
            t.active = -1
            AND t.site_name LIKE :site_id
        ORDER BY
            c.cell_id
    """

    row_factory = namedtuple(
        'AtollWcdmaSite',
        [
            'site',
            'cell',
            'latitude',
            'longitude',
            'antenna_type',
            'height',
            'azimut',
            'band',
            'location',
        ],
    )

    sql_params = {'site_id': f'{site_id}%'}

    sql_commands = {
        'select_wcdma_site': (select_wcdma_site, sql_params, row_factory),
    }
    return Atoll(sql_commands)
