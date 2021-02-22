from datetime import datetime
import croniter
import time
from abc import ABCMeta, abstractmethod
from threading import Thread

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
    ScheduleTask.__init__(self, "*/2 * * * *")

  
  def process(self):
    _now = datetime.now()
    print('service 1 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M"))


class SampleService2(ScheduleTask, Thread):
  def __init__(self):
    ScheduleTask.__init__(self, "*/5 * * * *")

  
  def process(self):
    _now = datetime.now()
    print('service 2 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M"))

class SampleService3(ScheduleTask, Thread):
  def __init__(self):
    ScheduleTask.__init__(self, "*/1 * * * *")

  
  def process(self):
    _now = datetime.now()
    print('service 3 ' + self.getName() + ' -> ' + _now.strftime("%m/%d/%Y, %H:%M"))


if __name__ == '__main__':
  c1 = SampleService1()
  c2 = SampleService2()
  c3 = SampleService3()

  # try:
  c1.start()
  c2.start()
  c3.start()


  threads = []
  threads.append(c1)
  threads.append(c2)
  threads.append(c3)

  for t in threads:
    t.join()
  
  while True:
    time.sleep(2)
    _min = datetime.now().minute()
    print(_min)
    if(_min == 44):
      c1.terminate()

  # except Exception as e:
  #     print("Oops!", e.__class__, "occurred.")
  #     print()
