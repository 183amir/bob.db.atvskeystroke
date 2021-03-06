#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the ATVS Keystroke database.
"""

import os, sys
import unittest
from .query import Database

class ATVSKeystrokeDatabaseTest(unittest.TestCase):

    def test_clients(self):
      db = Database()
      assert len(db.groups()) == 1
      assert len(db.clients()) == 126
      assert len(db.clients(groups='eval')) == 63
      assert len(db.clients(groups='Genuine')) == 63
      assert len(db.clients(groups='Impostor')) == 63
      assert len(db.models()) == 63
      assert len(db.models(groups='eval')) == 63
      assert len(db.models(groups='Genuine')) == 63


    def test_objects(self):
      db = Database()
      assert len(db.objects()) == 1512
      # A
      assert len(db.objects(protocol='A')) == 1512
      assert len(db.objects(protocol='A', groups='eval')) == 1512
      assert len(db.objects(protocol='A', groups='eval', purposes='enrol')) == 378
      assert len(db.objects(protocol='A', groups='eval', purposes='probe')) == 1134
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', classes='client')) == 378
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', classes='impostor')) == 756
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1])) == 18
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1], classes='client')) == 6
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1], classes='impostor')) == 12
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2])) == 36
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2], classes='client')) == 12
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2], classes='impostor')) == 24


    def test_driver_api(self):

      from bob.db.base.script.dbmanage import main
      assert main('atvskeystroke dumplist --self-test'.split()) == 0
      assert main('atvskeystroke checkfiles --self-test'.split()) == 0
      assert main('atvskeystroke reverse Genuine_1_1 --self-test'.split()) == 0
      assert main('atvskeystroke path 37 --self-test'.split()) == 0
