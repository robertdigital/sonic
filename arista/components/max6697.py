
from .common import I2cComponent
from ..core.component import Priority
from ..drivers.max6697 import Max6697KernelDriver

class Max6697(I2cComponent):
   def __init__(self, addr, drivers=None,
                priority=Priority.THERMAL, **kwargs):
      drivers = drivers or [ Max6697KernelDriver(addr=addr) ]
      self.sensors = []
      super(Max6697, self).__init__(addr=addr, drivers=drivers, priority=priority,
                                    **kwargs)

   def addTempSensors(self, sensors):
      self.sensors.extend(sensors)
