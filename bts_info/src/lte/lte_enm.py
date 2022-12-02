"""Create LTE ENM CLI object for working with ENM."""

from collections import namedtuple

from utils.enm_cli import EnmCli


def make_lte_enm_cli(site_id):
    """
    Create LTE ENM CLI object.

    Args:
        site_id (str): 5 numbers string

    Returns:
        EnmCli instance
    """
    LteMoInfo = namedtuple('LteMoInfo', ['type', 'scope', 'parameters'])

    lte_mo_data = [
        LteMoInfo('SectorCarrier', f'ERBS_{site_id}*', 'noOfTxAntennas, reservedBy'),
    ]

    return EnmCli(lte_mo_data)
