"""Make Atoll instance for working with Atoll GSM data."""

from collections import namedtuple

from utils.atoll import Atoll


def make_gsm_atoll(site_id):
    """
    Make Atoll instance for working with Atoll GSM data.

    Args:
        site_id (str): 5 digits string

    Returns:
        Atoll instance
    """
    select_gsm_site = """
        SELECT
            t.site_name,
            t.tx_id,
            s.latitude,
            s.longitude,
            t.antenna_name,
            t.height,
            t.azimut,
            t.fband,
            s.bsc_name
        FROM
            atoll_mrat.gtransmitters t
            JOIN atoll_mrat.sites s
                ON t.site_name = s.name
        WHERE
            t.active = -1
            AND t.site_name LIKE :site_id
        ORDER BY
            t.tx_id
    """

    row_factory = namedtuple(
        'AtollGsmSite',
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
        'select_gsm_site': (select_gsm_site, sql_params, row_factory),
    }
    return Atoll(sql_commands)
