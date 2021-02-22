import croniter
import datetime

if __name__ == '__main__':
  now = datetime.datetime.now()
  cron = croniter.croniter('* * * * *', now)
  next1_ = cron.get_next(datetime.datetime)
  print(next1_)
  # datetime.datetime(2011, 9, 14, 17, 45)
  # cron.get_next(datetime.datetime)
  # datetime.datetime(2011, 9, 16, 17, 45)
  # cron.get_next(datetime.datetime)
  # datetime.datetime(2011, 9, 18, 17, 45)
