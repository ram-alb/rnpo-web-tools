"""Compare parameters from the network with atoll parameters."""


def create_diff(row, parameter, network_value, atoll_value):
    """
    Make diff for one parameter.

    Args:
        row: namedtuple
        parameter: string
        network_value: string or number
        atoll_value: string or number or None

    Returns:
        dict
    """
    return {
        'Subnetwork': row.subnetwork,
        'Site': row.sitename,
        'Cell': row.eutrancell,
        'Parameter': parameter,
        'Network value': network_value,
        'Atoll value': atoll_value,
    }


def compare_parameter(diff, row, parameter_name, atoll_value):
    """
    Compare one parameter and add it to diff if network value is not equal to atoll value.

    Args:
        diff: list
        row: namedtuple
        parameter_name: string
        atoll_value: string or number or None
    """
    row_as_dict = row._asdict()
    if row_as_dict[parameter_name] != atoll_value:
        diff.append(create_diff(
            row,
            parameter_name,
            row_as_dict[parameter_name],
            atoll_value,
        ))


def compare(selected_network_cells, atoll_cells):
    """
    Compare parameters from the network with atoll parameters.

    Args:
        selected_network_cells: cx-Oracle fetchall object
        atoll_cells: dict

    Returns:
        dict
    """
    diff = {}
    for row in selected_network_cells:
        subnetwork = row.subnetwork
        cell_name = row.eutrancell
        try:
            atoll_cell = atoll_cells[cell_name]
        except KeyError:
            continue
        if subnetwork not in diff.keys():
            diff[subnetwork] = []
        subnetwork_diff = diff[subnetwork]
        compare_parameter(subnetwork_diff, row, 'sitename', atoll_cell['sitename'])
        compare_parameter(subnetwork_diff, row, 'tac', atoll_cell['tac'])
        compare_parameter(subnetwork_diff, row, 'cellid', atoll_cell['cellid'])
        compare_parameter(subnetwork_diff, row, 'pci', atoll_cell['pci'])
        compare_parameter(subnetwork_diff, row, 'earfcndl', atoll_cell['earfcndl'])
        compare_parameter(subnetwork_diff, row, 'rach', atoll_cell['rach'])
    return diff
