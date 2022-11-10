"""Parse selected lte data."""


def parse_atoll_earfcndl(atoll_earfcndl):
    """
    Parse earfcndl from atoll_earfcndl value.

    Args:
        atoll_earfcndl: string

    Returns:
        number
    """
    earfcndl = atoll_earfcndl.split('(')[-1]
    return int(earfcndl[:-1])


def parse_rach(atoll_rach):
    """
    Parse rach from atoll_rach value.

    Args:
        atoll_rach: string

    Returns:
        number
    """
    try:
        last_index = atoll_rach.index('-')
    except ValueError:
        rach = int(atoll_rach)
    except AttributeError:
        rach = None
    else:
        rach = int(atoll_rach[:last_index])
    return rach


def parse_cellid(atoll_cellid):
    """
    Parse cellid from atoll_cellid value.

    Args:
        atoll_cellid: string

    Returns:
        number or None
    """
    try:
        cellid = int(atoll_cellid)
    except TypeError:
        cellid = None
    return cellid


def parse_atoll_cells(selected_atoll_cells):
    """
    Parse selected atoll lte cells.

    Args:
        selected_atoll_cells: cx-Oracle fetchall object

    Returns:
        dict
    """
    atoll_cells = {}
    for cell in selected_atoll_cells:
        atoll_cells[cell.eutrancell] = {
            'sitename': cell.sitename,
            'tac': cell.tac,
            'cellid': parse_cellid(cell.cellid),
            'pci': cell.pci,
            'earfcndl': parse_atoll_earfcndl(cell.earfcndl),
            'rach': parse_rach(cell.rach),
        }
    return atoll_cells
