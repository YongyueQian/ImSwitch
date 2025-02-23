from imswitch.imcommon.model import initLogger
from imswitch.imcontrol.model.interfaces.ESP32RestAPI import ESP32Client

class ESP32Manager:
    """ A low-level wrapper for TCP-IP communication (ESP32 REST API)
    """

    def __init__(self, rs232Info, name, **_lowLevelManagers):
        self.__logger = initLogger(self, instanceName=name)
        self._settings = rs232Info.managerProperties
        self._name = name
        try:
            self._host = rs232Info.managerProperties['host']
        except:
            self._host = None

        try:
            self._serialport = rs232Info.managerProperties['serialport']
        except:
            self._port = None

        # initialize the ESP32 device adapter
        self._esp32 = ESP32Client(host=self._host, port=80, serialport=self._serialport, baudrate=115200)
        # self._esp32 = ESP32Client(self._host, port=80)

    def send(self, arg: str) -> str:
        """ Sends the specified command to the RS232 device and returns a
        string encoded from the received bytes. """
        self._esp32.post_json(arg)
        
    def finalize(self):
        pass 


# Copyright (C) 2020-2021 ImSwitch developers
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
