import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil

from BaseService import SampleService1, SampleService2,SampleService3

class TestService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "My service description"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
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
            rc = win32event.WaitForSingleObject(self.hWaitStop, 500)



if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService)
