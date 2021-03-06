#!/usr/bin/env python3
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2015-2016 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""cx_Freeze script to run qutebrowser tests on the frozen executable."""

import sys

import pytest
import pytestqt.plugin
import pytest_mock
import pytest_catchlog
import pytest_instafail
import pytest_faulthandler
import pytest_xvfb
import pytest_rerunfailures
import pytest_warnings
import pytest_benchmark.plugin

sys.exit(pytest.main(plugins=[pytestqt.plugin, pytest_mock,
                              pytest_catchlog, pytest_instafail,
                              pytest_faulthandler, pytest_xvfb,
                              pytest_rerunfailures, pytest_warnings,
                              pytest_benchmark.plugin]))
