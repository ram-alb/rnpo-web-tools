"""Make Atoll instance for working with Atoll LTE data."""

from collections import namedtuple

from utils.atoll import Atoll


def make_lte_atoll(site_id):
    """
    Make Atoll instance for working with Atoll LTE data.

    Args:
        site_id (str): 5 digits string

    Returns:
        Atoll instance
    """
    select_lte_site = """
        SELECT
            s.lte_sitename as site_name,
            c.cell_id,
            s.longitude,
            s.latitude,
            t.antenna_name,
            t.height,
            t.azimut,
            t.fband,
            s.lte_region
        FROM
            atoll_mrat.sites s
        INNER JOIN
            atoll_mrat.xgtransmitters t
            ON s.name = t.site_name
        INNER JOIN
            atoll_mrat.xgcellslte c
            ON t.tx_id = c.tx_id
        WHERE
            t.active = -1
            AND s.lte_sitename LIKE :site_id
        ORDER BY
            c.cell_id
    """

    row_factory = namedtuple(
        'AtollLteSite',
        [
            'site',
            'cell',
            'longitude',
            'latitude',
            'antenna_type',
            'height',
            'azimut',
            'band',
            'location',
        ],
    )

    sql_params = {'site_id': f'%{site_id}%'}

    sql_commands = {
        'select_lte_site': (select_lte_site, sql_params, row_factory),
    }

    return Atoll(sql_commands)
