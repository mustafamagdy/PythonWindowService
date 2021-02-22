import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
from crontab import CronTab

class TestService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "My service description"

    cron = None
    job1: CronItem = None

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        # cron = CronTab(tabfile='d:/temp/python/dist/service-cron.tab')
        cron = CronTab()
        job1 = cron.new(command='python say-hello.py')
        print('test 1')
        job1.every(1).minute()
        print('test 2')

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        # if cron != None:
        #     cron.clear()

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            self.job1
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)



if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService)
