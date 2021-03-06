##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libfs(AutotoolsPackage):
    """libFS - X Font Service client library.

    This library is used by clients of X Font Servers (xfs), such as
    xfsinfo, fslsfonts, and the X servers themselves."""

    homepage = "http://cgit.freedesktop.org/xorg/lib/libFS"
    url      = "https://www.x.org/archive/individual/lib/libFS-1.0.7.tar.gz"

    version('1.0.7', 'd8c1246f5b3d0e7ccf2190d3bf2ecb73')

    depends_on('xproto@7.0.17:', type='build')
    depends_on('fontsproto', type='build')
    depends_on('xtrans', type='build')
    depends_on('pkg-config@0.9.0:', type='build')
    depends_on('util-macros', type='build')
