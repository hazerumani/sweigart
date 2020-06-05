To make it convenient to run your Python program, create a .bat batch file for running the Python program with py.exe. To make a batch file, make a new text file containing a single line like the following:

```bat
@py.exe C:\path\to\your\pythonScript.py %*
```

Replace this path with the absolute path to your own program, and save this file with a `.bat` file extension (for example, `pythonScript.bat`). This batch file will keep you from
having to type the full absolute path for the Python program every time you want to run it. I recommend you place all your batch and .py files in a single folder, such as `C:\MyPythonScripts` or `C:\Users\YourName\PythonScripts.`

The `C:\MyPythonScripts` folder should be added to the system path on Windows so that you can run the batch files in it from the Run dialog. To do this, modify the `PATH` environment variable. Click the _Start_ button and type _Edit environment variables for your account_. This option should auto-complete after you’ve begun to type it.
