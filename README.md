To use clone this git:
git clone sa_gitlab@gitserver.corp.stingraydigital.com:jbureau/stats-dashboard.git

Install dependencies:
sudo pip install selenium cryptography pyautogui

Install chromium driver:
sudo dpkg -i Resources/chromium.deb 

Go to python file directory:
cd ~/Dashboard/DashboardPackage 

To generate cryped password:
CryptHandler.py yourpassword

Start dashboard:
python DashboardModule.py crypted password


DashboardModule.py would need to have some modification to use for someone else
# dashboard-stats
