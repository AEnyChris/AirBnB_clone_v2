#!/usr/bin/python3
"""A fabric file to create archive of
a webstatic folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    local("mkdir -p versions")

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{time_stamp}.tgz"

    result = local(f"tar -cvzf {archive_name} web_static/")

    if result.failed:
        return None
    return archive_name
