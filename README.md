# Dude Where's my Lift Ticket
Automate lift ticket reservation at Crystal Mountain via the Ikon Pass portal.


*WARNING: This application could break at any time, due to its inherent reliance on CSS and HTML Elements. If
any elements that we are targeting are changed, functionality could be affected. USE AT YOUR OWN RISK.*

*WARNING_2: Lots of gotchas and hard-coded stuff, have fun.*

### Instructions

*NOTE: These instructions are assuming you are using a Windows OS.*

1. An installation of Chrome is required to run Selenium. That Chrome version must match the version of the Selenium
   driver. In our case, that version is '87'. I could have put more work into this to allow different versions of chrome
   to be used, but I am lazy... Sorry.
    1. Run this in Powershell to check your version: 
       
            (Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo

    2. If it does not output 87.xx.xxx, please download and install it. Or if you want, download the Selenium Chrome Driver to match your Chrome version and put it in './chrome_driver'
    3. Finally, ensure the Selenium Chrome Driver is in your systems PATH.
    
2. Create a Python virtual environment and activate it
   1. If you are new to virtual environments this will help: https://docs.python.org/3/tutorial/venv.html
    
3. Ensure Python version is greater than 3.9.1
    
4. Navigate to the root directory of the project and install the required Python packages:
        1. pip install -r requirements.txt
   
5. Run through the Globals.py file and set required variables.

6. Run the application (The second argument is the date you want to reserve.):
   
        python ./main.py 'Jan 14 2021'