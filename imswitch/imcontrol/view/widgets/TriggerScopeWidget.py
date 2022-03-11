from qtpy import QtCore, QtWidgets

from imswitch.imcontrol.view import guitools
from .basewidgets import Widget


class TriggerScopeWidget(Widget):
    """ Widget for controlling the parameters of a TriggerScope. """
    sigRunToggled = QtCore.Signal(float)  # (enabled)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.runButton = guitools.BetterPushButton('Run')
        # self.runButton.setCheckable(True)
        # self.runButton.clicked.connect(self.sigRunToggled)
        # grid.addWidget(self.runButton, 0, 0)

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        self.incrementVoltageLabel = QtWidgets.QLabel("Increment/V")
        grid.addWidget(self.incrementVoltageLabel, 0, 0)

        self.incrementVoltage = QtWidgets.QLineEdit()
        grid.addWidget(self.incrementVoltage, 0, 1)
        self.incrementVoltage.textChanged[str].connect(self.action)

        self.setVoltageLabel = QtWidgets.QLabel("Set Voltage/V")
        grid.addWidget(self.setVoltageLabel, 0, 2)

        self.setVoltage = QtWidgets.QDoubleSpinBox()
        self.setVoltage.setKeyboardTracking(False)
        self.setVoltage.setDecimals(3)
        self.setVoltage.setMinimum(-5.0)
        self.setVoltage.setMaximum(5.0)
        self.setVoltage.valueChanged.connect(self.sigRunToggled)
        grid.addWidget(self.setVoltage, 0, 3)

        self.TTLtimeLabel = QtWidgets.QLabel("TTL Time/ms")
        grid.addWidget(self.TTLtimeLabel, 0, 4)

        self.setTTLtime = QtWidgets.QLineEdit()
        grid.addWidget(self.setTTLtime, 0, 5)

        self.setSlopeLabel = QtWidgets.QLabel("Slope/V")
        grid.addWidget(self.setSlopeLabel, 1, 0)

        self.setSlope = QtWidgets.QLineEdit()
        grid.addWidget(self.setSlope, 1, 1)

        self.currentVoltageLabel = QtWidgets.QLabel("Current Voltage/V")
        grid.addWidget(self.currentVoltageLabel, 1, 2)

        self.currentVoltage = QtWidgets.QLineEdit()
        self.currentVoltage.setReadOnly(True)
        self.currentVoltage.setText(str(0))
        grid.addWidget(self.currentVoltage, 1, 3)

        self.DACtimeLabel = QtWidgets.QLabel("DAC Time/ms")
        grid.addWidget(self.DACtimeLabel, 1, 4)

        self.setDACtime = QtWidgets.QLineEdit()
        grid.addWidget(self.setDACtime, 1, 5)

        self.RepLabel = QtWidgets.QLabel("Repetition")
        grid.addWidget(self.RepLabel, 1, 6)

        self.setREP = QtWidgets.QLineEdit()
        grid.addWidget(self.setREP, 1, 7)
    def action(self):
        self.setVoltage.setSingleStep(float(self.incrementVoltage.text()))

