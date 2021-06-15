# Python as windows service

Convert python scripts to Windows Service, with scheduler

## How to use
- cd root folder of project

- open cmd and run following commands
```sh
	pip install pywinservicemanager==1.0.2
	pip install pywin32
	pip install croniter
```

- change service name and service display name in ``` PythonMainClass ```

- run command : ``` pyinstaller -F --hidden-import=win32timezone filename.py```

- cd dist folder
	- install command : ``` filename.exe install```
	- start command : ``` filename.exe start```
	- stop command : ``` filename.exe stop```
	- remove service : ``` sc.exe SERVICE_NAME remove```
