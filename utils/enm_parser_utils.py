"""ENM data parser utils."""

import re


def parse_mo_value(fdn, mo_type):
    """
    Parse MO value from FDN for related MO type.

    Args:
        fdn: string
        mo_type: string

    Returns:
        strings
    """
    mo_re_patterns = {
        'MeContext': 'MeContext=[^,]*',
        'SubNetwork': ',SubNetwork=[^,]*',
        'EUtranCellFDD': r'EUtranCellFDD=\d{6}-\d{3}',
        'UtranCell': 'UtranCell=.*',
        'IubLink': 'IubLink=.*',
        'GeranCell': 'GeranCell=.*',
        'ChannelGroupCell': 'GeranCell=[^,]*',
        'NRSectorCarrier': 'NRSectorCarrier=.*',
        'NRCellDU': 'NRCellDU=.*',
        'NbIotCell': 'NbIotCell=.*',
    }
    mo = re.search(mo_re_patterns[mo_type], fdn).group()
    return mo.split('=')[-1]
