from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5", "numpy", "matplotlib", "scipy"],
                     "include_files": ["settings.txt", "Resources"],
                     "optimize": 2}

setup(
        name = "BDSP Changelogger",
        version = "1.0",
        options = {"build_exe": build_exe_options},
        description = "Creates changelogs for different values from masterdatas and personal_masterdatas",
        executables = [Executable("main.py")])