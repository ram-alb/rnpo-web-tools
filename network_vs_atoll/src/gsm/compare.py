"""Compare parameters from the network with atoll parameters."""


comma_separator = ', '


def create_parameter_diff(row, parameter, network_value, atoll_value):
    """
    Create a dict with info about one parameter diff.

    Args:
        row: cx-Oracle row object
        parameter: string
        network_value: could be string, number or list
        atoll_value: could be string, number or list

    Returns:
        dict
    """
    return {
        'BSC': row.bscname,
        'Site': row.sitename,
        'Cell': row.cell,
        'Parameter': parameter,
        'Network value': network_value,
        'Atoll value': atoll_value,
    }


def compare_common_parameters(diff, row):
    """
    Add to the diff list an each common parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
    """
    common_parameters = [
        'bscname',
        'sitename',
        'lac',
        'cellid',
        'bcch',
    ]
    row_as_dict = row._asdict()
    for parameter in common_parameters:
        network_value = str(row_as_dict[parameter])
        atoll_value = str(row_as_dict[f'atoll_{parameter}'])
        if network_value == atoll_value:
            continue
        diff.append(create_parameter_diff(row, parameter, network_value, atoll_value))


def compare_fband(diff, row):
    """
    Add to the diff list fband parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
    """
    if row.bcch is None:
        return
    arfcn_number = 125
    fband = 'GSM 900' if int(row.bcch) < arfcn_number else 'GSM 1800'
    atoll_fband = row.atoll_fband
    if fband != atoll_fband:
        diff.append(create_parameter_diff(row, 'fband', fband, atoll_fband))


def compare_bsic(diff, row):
    """
    Add to the diff list bsic parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
    """
    if str(row.ncc) == '0':
        bsic = str(row.bcc)
    else:
        bsic = f'{row.ncc}{row.bcc}'
    atoll_bsic = str(row.atoll_bsic)
    if bsic != atoll_bsic:
        diff.append(create_parameter_diff(row, 'bsic', bsic, atoll_bsic))


def compare_tch(diff, row):
    """
    Add to the diff list tchfreqs parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
    """
    if row.tchfreqs is None:
        tch_list = ''
    else:
        tch_list = row.tchfreqs.split(comma_separator)
        tch_list.append(str(row.bcch))
        tch_list = comma_separator.join(sorted(tch_list))

    if row.atoll_tchfreqs is None:
        atoll_tch_list = ''
    else:
        atoll_tchfreqs = row.atoll_tchfreqs.strip()
        atoll_tch_list = atoll_tchfreqs.split(' ')
        atoll_tch_list = comma_separator.join(sorted(atoll_tch_list))

    if tch_list != atoll_tch_list:
        diff.append(create_parameter_diff(row, 'tchfreqs', tch_list, atoll_tch_list))


def compare_maio(diff, row, atoll_maio_data):
    """
    Add to the diff list maio parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
        atoll_maio_data: dict
    """
    if row.maio is None:
        maio = ''
    else:
        maio = row.maio.split(comma_separator)
        maio = comma_separator.join(sorted(maio))

    label = f'{row.cell}-{row.sitename}'
    try:
        atoll_maio = sorted(atoll_maio_data[label])
    except KeyError:
        atoll_maio = ''
    else:
        atoll_maio = comma_separator.join([str(maio) for maio in atoll_maio])

    if maio != atoll_maio:
        diff.append(create_parameter_diff(row, 'maio', maio, atoll_maio))


def compare_hsn(diff, row, atoll_hsn_data):
    """
    Add to the diff list hsn parameter diff.

    Args:
        diff: list
        row: cx-Oracle row object
        atoll_hsn_data: dict
    """
    label = f'{row.cell}-{row.sitename}'
    try:
        atoll_hsn = atoll_hsn_data[label]
    except KeyError:
        atoll_hsn = None
    if row.hsn != atoll_hsn:
        diff.append(create_parameter_diff(row, 'hsn', row.hsn, atoll_hsn))


def compare_gsm(atoll_cell_parameters, atoll_hsn, atoll_maio_data):
    """
    Compare gsm parameters from the network with atoll parameters.

    Args:
        atoll_cell_parameters: cx-Oracle fetchall object
        atoll_hsn: dict
        atoll_maio_data: dict

    Returns:
        dict
    """
    diff = {}
    for row in atoll_cell_parameters:
        bsc = row.bscname
        if bsc not in diff.keys():
            diff[bsc] = []
        bsc_diff = diff[bsc]
        compare_common_parameters(bsc_diff, row)
        compare_fband(bsc_diff, row)
        compare_bsic(bsc_diff, row)
        compare_tch(bsc_diff, row)
        compare_maio(bsc_diff, row, atoll_maio_data)
        compare_hsn(bsc_diff, row, atoll_hsn)
    return diff
