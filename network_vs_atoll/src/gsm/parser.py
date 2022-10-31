"""Parse gsm parameters from selected data."""


def parse_hsn(atoll_hsn_data):
    """
    Parse hsn values from atoll.

    Args:
        atoll_hsn_data: cx-Oracle fetchall object

    Returns:
        dict
    """
    atoll_hsns = {}
    for row in atoll_hsn_data:
        label = f'{row.cell}-{row.sitename}'
        atoll_hsns[label] = row.hsn
    return atoll_hsns


def parse_maio(atoll_maio_data):
    """
    Parse maio values from atoll.

    Args:
        atoll_maio_data: cx-Oracle fetchall object

    Returns:
        dict
    """
    atoll_maios = {}
    for row in atoll_maio_data:
        if row.maio is None:
            continue
        label = f'{row.cell}-{row.sitename}'
        if label in atoll_maios.keys():
            atoll_maios[label].append(row.maio)
        else:
            atoll_maios[label] = [row.maio]
    return atoll_maios
