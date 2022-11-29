"""Communicate with ENM CLI via enmscripting."""

import os

import enmscripting


class EnmCli(object):
    """Communicate with ENM CLI via enmscripting."""

    def __init__(self, mo_info):
        """
        Construct a new object to communicate with ENM CLI.

        Args:
            mo_info: list of namedtuples with scope, mo_type and parameters
        """
        self.cmedit_get_commands = {}
        for mo_item in mo_info:
            command = 'cmedit get {scope} {mo_type}.({parameters})'.format(
                scope=mo_item.scope,
                mo_type=mo_item.type,
                parameters=mo_item.parameters,
            )
            self.cmedit_get_commands[mo_item.type] = command

    def execute_cmedit_get_command(self, mo_type):
        """
        Execute cmedit get CLI commands.

        Args:
            mo_type: mo type name string

        Returns:
            enmscripting ElementGroup object
        """
        session = enmscripting.open(os.getenv('ENM_SERVER')).with_credentials(
            enmscripting.UsernameAndPassword(
                os.getenv('ENM_LOGIN'),
                os.getenv('ENM_PASSWORD'),
            ),
        )
        enm_cmd = session.command()
        response = enm_cmd.execute(self.cmedit_get_commands[mo_type])
        enmscripting.close(session)
        return response.get_output()
