"""Select gsm data from Network Live and Atoll."""

from collections import namedtuple

from network_vs_atoll.src.select_data import execute_sql_select


def select_cell_parameters():
    """
    Select cell level parameters from Network Live and Atoll.

    Returns:
        cx-Oracle fatchall object
    """
    select_sql = """
        SELECT
            network_live.gsmcells2.cell,
            network_live.gsmcells2.bscname,
            atoll_mrat.sites.bsc_name as atoll_bscname,
            network_live.gsmcells2.sitename,
            atoll_mrat.gtransmitters.site_name as atoll_sitename,
            network_live.gsmcells2.lac,
            atoll_mrat.gtransmitters.lac as atoll_lac,
            network_live.gsmcells2.cellid,
            atoll_mrat.gtransmitters.cell_identity as atoll_cellid,
            network_live.gsmcells2.bcch,
            atoll_mrat.gtransmitters.control_channel as atoll_bcch,
            atoll_mrat.gtransmitters.fband as atoll_fband,
            network_live.gsmcells2.ncc,
            network_live.gsmcells2.bcc,
            atoll_mrat.gtransmitters.bsic as atoll_bsic,
            network_live.gsmcells2.tchfreqs,
            atoll_mrat.gtransmitters.channels as atoll_tchfreqs,
            network_live.gsmcells2.maio,
            network_live.gsmcells2.hsn
        FROM
            network_live.gsmcells2
        LEFT JOIN
            atoll_mrat.gtransmitters
            ON network_live.gsmcells2.cell = atoll_mrat.gtransmitters.tx_id
        LEFT JOIN
            atoll_mrat.sites
            ON atoll_mrat.gtransmitters.site_name = atoll_mrat.sites.name
        WHERE
            network_live.gsmcells2.oss = 'OSS' or network_live.gsmcells2.oss = 'ENM'
    """

    row_factory = namedtuple(
        'CellParams',
        [
            'cell',
            'bscname',
            'atoll_bscname',
            'sitename',
            'atoll_sitename',
            'lac',
            'atoll_lac',
            'cellid',
            'atoll_cellid',
            'bcch',
            'atoll_bcch',
            'atoll_fband',
            'ncc',
            'bcc',
            'atoll_bsic',
            'tchfreqs',
            'atoll_tchfreqs',
            'maio',
            'hsn',
        ],
    )

    return execute_sql_select(select_sql, row_factory)


def select_atoll_hsn():
    """
    Select hsn values from atoll.

    Returns:
        cx-Oracle fatchall object
    """
    select_sql = """
        SELECT
            atoll_mrat.gtrgs.tx_id,
            atoll_mrat.gtrgs.hsn,
            atoll_mrat.gtrgs.synchro_name
        FROM
            atoll_mrat.gtrgs
        WHERE
            atoll_mrat.gtrgs.trx_type = 'TCH'
    """
    row_factory = namedtuple(
        'Hsn',
        [
            'cell',
            'hsn',
            'sitename',
        ],
    )
    return execute_sql_select(select_sql, row_factory)


def select_atoll_maio():
    """
    Select maio values from atoll.

    Returns:
        cx-Oracle fatchall object
    """
    select_sql = """
        SELECT
            atoll_mrat.gtrxs.tx_id,
            atoll_mrat.gtrxs.maio,
            atoll_mrat.gtransmitters.site_name
        FROM
            atoll_mrat.gtrxs
        LEFT JOIN
            atoll_mrat.gtransmitters
            ON atoll_mrat.gtransmitters.tx_id = atoll_mrat.gtrxs.tx_id
        WHERE
            atoll_mrat.gtrxs.trx_type = 'TCH'
        ORDER BY
            atoll_mrat.gtrxs.tx_id
    """
    row_factory = namedtuple(
        'Maio',
        [
            'cell',
            'maio',
            'sitename',
        ],
    )
    return execute_sql_select(select_sql, row_factory)
