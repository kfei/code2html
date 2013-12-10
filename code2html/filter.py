# -*- coding: utf-8 -*-


def get_filter():
    """
    Return a list of ignore directories.
    """

    # Ignore all directories start with a dot
    filter = ['/\.\w+/*']

    return filter
