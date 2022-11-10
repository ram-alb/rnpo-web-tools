"""Fill excel file with inconsistencies."""

from openpyxl import Workbook
from openpyxl.styles import Alignment


def fill_excel(technology, node_diffs, node):
    common_columns = [
        'Site',
        'Cell',
        'Parameter',
        'Network value',
        'Atoll value',
    ]

    if technology == 'LTE':
        columns = ['Subnetwork', *common_columns]
    elif technology == 'WCDMA':
        columns = ['RNC', *common_columns]
    elif technology == 'GSM':
        columns = ['BSC', *common_columns]

    work_book = Workbook()
    sheet = work_book.active

    for col in columns:
        current_cell = sheet.cell(row=1, column=columns.index(col) + 1)
        current_cell.value = col
        current_cell.alignment = Alignment(horizontal='center')

    row = 2
    for diff in node_diffs:
        for column in columns:
            current_cell = sheet.cell(row=row, column=columns.index(column) + 1)
            current_cell.value = diff[column]
            current_cell.alignment = Alignment(horizontal='center')
        row += 1

    report_path = f'network_vs_atoll/reports/{node}-inconsistencies.xlsx'
    work_book.save(report_path)
    return report_path
