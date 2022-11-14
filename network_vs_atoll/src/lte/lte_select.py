"""Select lte data from Network Live and Atoll."""

from collections import namedtuple

from network_vs_atoll.src.select_data import execute_sql_select


def select_network_live_cells():
    """
    Select network live lte cells with neccessary parameters.

    Returns:
        cx-Oracle fetchall object
    """
    select_sql = """
        SELECT
            subnetwork,
            sitename,
            eutrancell,
            tac,
            cellid,
            physicalcellid,
            earfcndl,
            rachrootsequence
        FROM
            network_live.ltecells2
        WHERE
            oss = 'ENM'
    """

    row_factory = namedtuple(
        'NetworkCells',
        [
            'subnetwork',
            'sitename',
            'eutrancell',
            'tac',
            'cellid',
            'pci',
            'earfcndl',
            'rach',
        ],
    )

    return execute_sql_select(select_sql, row_factory)


def select_atoll_cells():
    """
    Select atoll lte cells with neccessary parameters.

    Returns:
        cx-Oracle fetchall object
    """
    select_sql = """
        SELECT
            ATOLL_MRAT.SITES.LTE_SITENAME as sitename,
            CELL_ID AS EUTRANCELL,
            TAC,
            UNIQUE_ID AS CELLID,
            PCI,
            CARRIER as EARFCNDL,
            PRACH_RSI_LIST AS RACH
        FROM
            ATOLL_MRAT.XGCELLSLTE
        INNER JOIN
            ATOLL_MRAT.XGTRANSMITTERS
            ON ATOLL_MRAT.XGTRANSMITTERS.TX_ID = ATOLL_MRAT.XGCELLSLTE.TX_ID
        INNER JOIN
            ATOLL_MRAT.SITES
            ON ATOLL_MRAT.SITES.NAME = ATOLL_MRAT.XGTRANSMITTERS.SITE_NAME
        WHERE
            ATOLL_MRAT.XGTRANSMITTERS.ACTIVE = -1
            AND UNIQUE_ID BETWEEN '100' AND '149'
            AND ATOLL_MRAT.XGCELLSLTE.CELL_ID LIKE '5%%'
            AND ATOLL_MRAT.SITES.LTE_SITENAME LIKE '%%RBS_%%'
    """

    row_factory = namedtuple(
        'AtollCells',
        [
            'sitename',
            'eutrancell',
            'tac',
            'cellid',
            'pci',
            'earfcndl',
            'rach',
        ],
    )

    return execute_sql_select(select_sql, row_factory)
