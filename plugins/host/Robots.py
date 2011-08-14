# Tachyon - Fast Multi-Threaded Web Discovery Tool
# Copyright (c) 2011 Gabriel Tremblay - initnull hat gmail.com
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#

from core import conf, utils
from core.fetcher import Fetcher
from urlparse import urljoin

def execute():
    """ Fetch /robots.txt and add the disallowed paths as target """
    target_url = urljoin(conf.target_host, "/robots.txt")
    fetcher = Fetcher()
    response_code, content, headers = fetcher.fetch_url(target_url, 'GET', conf.user_agent, True, conf.fetch_timeout_secs)

    print headers
    if response_code is 200 or response_code is 302 and content:
        utils.output(content)
    else:
        utils.output('Robots.txt not found')
