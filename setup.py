from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5", "numpy"],
                     "optimize": 2}

setup(
        name = "BDSP Changelogger",
        version = "1.0",
        description = "Unpacks and Repacks in for Unity monobehavior jsons",
        executables = [Executable("Trainers.py"), Executable("Movesets.py"), Executable("Pokemon.py"), Executable("TMCompat.py"), Executable("TMLearned.py")])