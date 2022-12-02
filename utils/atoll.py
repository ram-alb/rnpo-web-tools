"""Communicate with Atoll db through cx_Oracle."""

import os

import cx_Oracle


class Atoll(object):
    """Create object for working with Atoll db."""

    def __init__(self, sql_commands):
        """
        Create sql_commands dict attribute with sql commands.

        Args:
            sql_commands (dict): each item has tuple with sql_command
                params and rowfactory
        """
        self.sql_commands = {**sql_commands}

    def execute_sql_command(self, sql_name):
        """
        Execute sql command.

        Args:
            sql_name (str): key for self.sql_commands dict, by this key
                sql_command, params and rowfactory are accessable

        Returns:
            list: a list of obects according to row_factory
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
            sql_command, sql_params, row_factory = self.sql_commands[sql_name]

            cursor.execute(sql_command, sql_params)
            if row_factory:
                cursor.rowfactory = row_factory

            return cursor.fetchall()
