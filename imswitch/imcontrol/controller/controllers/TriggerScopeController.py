from ..basecontrollers import ImConWidgetController
from imswitch.imcommon.model import initLogger
import numpy as np


class TriggerScopeController(ImConWidgetController):
    """ Linked to TriggerScopeWidget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Connect PositionerWidget signals
        self._widget.sigRunToggled.connect(self.run)

    def run(self):
        #self._master.triggerScopeManager.send("*", 1)
        self.increment = float(self._widget.incrementVoltage.text())
        self.slope = float(self._widget.setSlope.text())
        self.finalVoltage = float(self._widget.setVoltage.value())
        self.current = float(self._widget.currentVoltage.text())
        self._widget.currentVoltage.setText(str(round(self.finalVoltage, 3)))
        steps = int(np.ceil(np.abs(self.finalVoltage - self.current) / self.slope)) + 1
        self.TTLdelay = int(self._widget.setTTLtime.text())
        self.DACdelay = int(self._widget.setDACtime.text())
        self.Repetition = int(self._widget.setREP.text())
        dacarray = np.linspace(self.current, self.finalVoltage, steps)
        ttlarray = np.ones(steps, dtype=int)
        params = self.setParams(1, 1, len(dacarray), 0, self.DACdelay, self.TTLdelay, self.Repetition)
        self._master.triggerScopeManager.run_wave(dacarray, ttlarray, params)

        #self._master.triggerScopeManager.sendAnalog(1, 1)

    def setParams(self, analogLine, digitalLine, length, trigMode, delayDAC, delayTTL, reps):
        params = dict([])
        params["analogLine"] = analogLine
        params["digitalLine"] = digitalLine
        params["length"] = length
        params["trigMode"] = trigMode
        params["delayDAC"] = delayDAC
        params["delayTTL"] = delayTTL
        params["reps"] = reps
        return params

