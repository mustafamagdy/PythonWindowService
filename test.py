import croniter
import datetime
import os

if __name__ == '__main__':
  now = datetime.datetime.now()
  cron = croniter.croniter('* * * * *', now)
  next1_ = cron.get_next(datetime.datetime)
  goal_dir = os.path.join(os.getcwd(), "config.json")
  print(goal_dir)  # prints C:/here/I/am/../../my_dir
  print(os.path.normpath(goal_dir))  # prints C:/here/my_dir
  print(os.path.realpath(goal_dir))  # prints C:/here/my_dir
  print(os.path.abspath(goal_dir))  # prints C:/here/my_dir
  print(next1_)
  # datetime.datetime(2011, 9, 14, 17, 45)
  # cron.get_next(datetime.datetime)
  # datetime.datetime(2011, 9, 16, 17, 45)
  # cron.get_next(datetime.datetime)
  # datetime.datetime(2011, 9, 18, 17, 45)
