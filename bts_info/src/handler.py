"""Handle Atoll data."""


def handle_atoll_data(atoll_gsm_data):
    """
    Handle Atoll data.

    Args:
        atoll_gsm_data (list): a list of namedtuples selected from atoll

    Returns:
        list: a list of dicts
    """
    site_data = []
    for row in atoll_gsm_data:
        row = row._replace(latitude=round(row.latitude, 5))
        row = row._replace(longitude=round(row.longitude, 5))
        site_data.append({**row._asdict(), 'MIMO': ''})
    return site_data
