🍕 What you should have before starting.
-------------------------------------

* IntelliJ IDE
* Homebrew & Xcode (Mac)
* python 3.5.0+ (recommended version as per 11/05/2021: 3.9.0)

✈️ How to set up.
-------------------------------------
### 🚀 MAC
1. Open terminal inside the root of project directory ``brew install pyenv``
3. Upgrade Xcode if you haven’t yet
4. ``pyenv install 3.9.0``
5. ``pip3 install virtualenv``
6. ``virtualenv -p /Users/{your_username}/.pyenv/versions/3.9.0/bin/python venv``

         - If this returns a "command not found" error, run ``pip3 install virtualenv`` and then retry the command
         - If it still does not work, then try using ``sudo``

7. ``source venv/bin/activate``
8. ``pip3 install -r requirements.txt``
9. Ensure the Python plugin is installed in IntelliJ.
10. Create a new SDK in IntelliJ linked to this Virtual environment
11. Link your IntelliJ project to this SDK

### 🛻 WINDOWS
1. Download and install Visual C++ 14.0 by installing Visual studio community edition https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017
2. Visit https://www.python.org/downloads/release/python-390/. Download and install this version.
3. Install pip following this tutorial https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
4. Install virtual environment (venv) via pip ``pip install virtualenv``
5. Open terminal inside the root of project directory
6. Create venv ``virtualenv venv`` it will take a while, then ``{path_to_project}\venv\Scripts\activate.bat``. For example: ``C:\Users\ngocy\IdeaProjects\tinypulse-qc-assignment\venv\Scripts\activate.bat``
7. Now you need to add your venv directory to PATH, let's open command prompt as administrator ``setx /M path "%path%;{path_to_project}\venv\Scripts\"``
8. Restart your computer
9. Open terminal inside the root of project directory again then install all requirements ``pip install -r requirements.txt``
10. Ensure the Python plugin is installed in IntelliJ.
11. Create a new SDK in IntelliJ linked to this Virtual environment
12. Link your IntelliJ project to this SDK

🍵 How to run test.
-------------------------------------
* Via terminal, press Alt + F12 to open IntelliJ terminal then ``behave features/tinypulse.feature``
* Or you can open _features/tinypulse.feature_ file then click on run button near each Scenario

