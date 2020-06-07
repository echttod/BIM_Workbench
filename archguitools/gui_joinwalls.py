#***************************************************************************
#*   Copyright (c) 2011 Yorik van Havre <yorik@uncreated.net>              *
#*   Copyright (c) 2020 Carlo Pavan                                        *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

"""Provide the Arch_Wall command."""

## @package gui_wall
# \ingroup ARCH
# \brief Provide the Arch_Wall command used in Arch to create an Arch Wall.

import os
import FreeCAD as App
import FreeCADGui as Gui
import Draft
from archmake.joinwalls import join_walls
from PySide import QtCore,QtGui

# ---------------------------------------------------------------------------
# this is just a very rough implementation to test the objects
# ---------------------------------------------------------------------------

class Arch_JoinWalls:

    "the Arch JoinWalls command definition"

    def GetResources(self):

        return {'Pixmap'  : os.path.join(os.path.dirname(__file__),"..","icons","Arch_Wall_Experimental.svg"),
                'MenuText': "Join_Walls_EXPERIMENTAL",
                'ToolTip': "EXPERIMENTAL\nJoin two walls.\nSelect first the wall that you want to\n extend and then the target wall."}

    def IsActive(self):

        return not App.ActiveDocument is None

    def Activated(self):
        sel = Gui.Selection.getSelection()
        w1 = sel[0]
        w2 = sel[1]
        join_walls(w1, w2)
        App.ActiveDocument.recompute()




Gui.addCommand('Arch_JoinWalls', Arch_JoinWalls())