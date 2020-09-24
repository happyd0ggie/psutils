#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os


class PsUtils:
    """Process utilities, use Python builtin modules and functions, do not
    use third-party libs.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_process_id_by_name(name):
        """Get process id by name.

        Args:
            name: process name to check.
        Returns:
            A list containing process pid.
        Raises:
            None.
        """
        pids = []
        for dirname in os.listdir('/proc'):
            if dirname.isdigit():
                cmdline = '/proc/{}/cmdline'.format(dirname)
                if os.path.exists(cmdline):
                    with open(cmdline) as out:
                        if name in out.read():
                            pids.append(int(dirname))
        return pids

    @staticmethod
    def process_is_running(name):
        """Check where given process 'name' is running.

        Args:
            name: process name to check.
        Returns:
            True if process is running, otherwise False.
        Raises:
            None.
        """
        pathname = '/proc/[1-9]*/cmdline'

        def cmdline_exists():
            for _item in glob.glob(pathname):
                if os.path.exists(_item):
                    with open(_item) as out:
                        if name in out.read():
                            yield True
                        else:
                            yield False

        return any(cmdline_exists())
