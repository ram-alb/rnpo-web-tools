"""Select data from Atoll db."""

import os

import cx_Oracle


def execute_sql_select(sql_select, row_factory):
    """
    Execute SQL select command and fetch rows with given row_factory.

    Args:
        sql_select: string
        row_factory: object with needed stucture

    Returns:
        object according to row_factory
    """
    atoll_dsn = cx_Oracle.makedsn(
        os.getenv('ATOLL_HOST'),
        os.getenv('ATOLL_PORT'),
        service_name=os.getenv('SERVICE_NAME'),
    )
    with cx_Oracle.connect(
        user=os.getenv('ATOLL_LOGIN'),
        password=os.getenv('ATOLL_PASSWORD'),
        dsn=atoll_dsn,
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_select)
        cursor.rowfactory = row_factory
        return cursor.fetchall()
