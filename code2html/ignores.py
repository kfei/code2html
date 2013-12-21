# -*- coding: utf-8 -*-


def get_ignores():
    """
    Return a list of ignore directories.
    """

    # Ignore all directories start with a dot
    ignores = ['/\.\w+/*']

    return ignores
