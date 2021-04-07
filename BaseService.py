from datetime import datetime
from os import system
import croniter
import time
from abc import ABCMeta, abstractmethod
from threading import Thread
from multiprocessing import Process, process
import json
import sys
import os

config_dir = os.path.join(os.getcwd(), "config.json")

class ScheduleTask(Thread):
  _nextRun = datetime.now()
  defaultSchedule = "*/5 * * * *"
  _isDisabled = False
  cron = None
  def __init__(self, cronExp):
    Thread.__init__(self)
    if(cronExp == None or cronExp == ""):
      self.cronExp = self.defaultSchedule
    else:
      self.cronExp = cronExp

    self.cron = croniter.croniter(self.cronExp, self._nextRun)


  @abstractmethod
  def process():
    """Implement this method on derived class with the scheduled job."""

  def run(self):
    """This should be called by windows service main thread."""

    while not self._isDisabled:
      _now = datetime.now()
      _minute = _now.min

      if(_now > self._nextRun):
        self.process()
        self._nextRun = self.cron.get_next(datetime)

      time.sleep(5)


class SampleService1(ScheduleTask, Thread):
  def __init__(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    
    ScheduleTask.__init__(self, "*/1 * * * *")

  
  def process(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    if(config["service1"]["status"] == "stop"):
      return

    _now = datetime.now()
    print('service 1 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M")+ "\n")
    f = open("service1.txt", "a")
    f.write('service 1 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M")+ "\n")
    f.close()


class SampleService2(ScheduleTask, Thread):
  def __init__(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    ScheduleTask.__init__(self, config["service2"]["schedule"])

  
  def process(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    if(config["service2"]["status"] == "stop"):
      return
    try:
        _now = datetime.now()
        raise Exception("error in service 2")
    except:
      print('service 2 error')
      _now = datetime.now()
      f = open("service2.txt", "a")
      f.write('service 2 error' + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M")+ "\n")
      f.close()


class SampleService3(ScheduleTask, Thread):
  def __init__(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    ScheduleTask.__init__(self, config["service3"]["schedule"])

  
  def process(self):
    with open(config_dir) as configSchema:
      config = json.load(configSchema)
    if(config["service3"]["status"] == "stop"):
      return        
    _now = datetime.now()
    print('service 3 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M")+ "\n")
    f = open("service3.txt", "a")
    f.write('service 3 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M" + "\n"))
    f.close()

