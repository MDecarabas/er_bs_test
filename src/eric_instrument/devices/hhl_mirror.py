from ophyd import Component, Device, EpicsMotor


class HHL_Mirrors(Device):
    jack = Component(EpicsMotor, 'm1', labels=('motor',), kind='config')
    lateral = Component(EpicsMotor, 'm3', labels=('motor',), kind='config')
    pitch = Component(EpicsMotor, 'm5', labels=('motor',), kind='config')
    fine_pitch = Component(EpicsMotor, 'piezo:m1', labels=('motor',), kind='config')
    bender_1 = Component(EpicsMotor, 'm7', labels=('motor',), kind='config')
    bender_2 = Component(EpicsMotor, 'm8', labels=('motor',), kind='config')