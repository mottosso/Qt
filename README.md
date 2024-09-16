<img width=260 src=https://raw.githubusercontent.com/mottosso/Qt.py/master/logo.svg>

[![Downloads](https://pepy.tech/badge/qt-py)](https://pepy.tech/project/qt-py)
[![Run Tests](https://github.com/mottosso/Qt.py/actions/workflows/run-tests.yml/badge.svg)](https://github.com/mottosso/Qt.py/actions)
[![PyPI version](https://badge.fury.io/py/Qt.py.svg)](https://pypi.python.org/pypi/Qt.py)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/qt.py/badges/version.svg)](https://anaconda.org/conda-forge/qt.py)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Qt-py/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)

Qt.py enables you to write software that runs on any of the supported bindings - PySide, PySide2, PySide6, PyQt4 and PyQt5.

<br>

##### News

| Date     | Version   | Event
|:---------|:----------|:----------
| May 2024 | [1.4.1][] | Added support for Qt 6
| Jan 2024 | [1.3.9][] | Run CI on Github Actions, instead of Travis CI.
| Sep 2020 | [1.3.0][] | Stability improvements and greater ability for `QtCompat.wrapInstance` to do its job
| Jun 2019 | [1.2.1][] | Bugfixes and [additional members](https://github.com/mottosso/Qt.py/releases/tag/1.2.0)
| Jan 2018 | [1.1.0][] | Adds new test suite, new members
| Mar 2017 | [1.0.0][] | Increased safety, **backwards incompatible**
| Sep 2016 | [0.6.9][] | Stable release
| Sep 2016 | [0.5.0][] | Alpha release of `--convert`
| Jun 2016 | [0.2.6][] | First release of Qt.py

- [More details](https://github.com/mottosso/Qt.py/releases).

[0.2.6]: https://github.com/mottosso/Qt.py/releases/tag/0.2.6
[0.5.0]: https://github.com/mottosso/Qt.py/releases/tag/0.5.0
[0.6.9]: https://github.com/mottosso/Qt.py/releases/tag/0.6.9
[1.0.0]: https://github.com/mottosso/Qt.py/releases/tag/1.0.0
[1.1.0]: https://github.com/mottosso/Qt.py/releases/tag/1.1.0
[1.2.1]: https://github.com/mottosso/Qt.py/releases/tag/1.2.1
[1.3.0]: https://github.com/mottosso/Qt.py/releases/tag/1.3.0
[1.3.9]: https://github.com/mottosso/Qt.py/releases/tag/1.3.9
[1.4.0]: https://github.com/mottosso/Qt.py/releases/tag/1.4.1

##### Guides

- [Qt 6 Transition Guide](#qt-6-transition-guide)
- [Developing with Qt.py](https://fredrikaverpil.github.io/blog/2016/07/25/developing-with-qtpy/)
- [Dealing with Maya 2017 and PySide2](https://fredrikaverpil.github.io/blog/2016/07/25/dealing-with-maya-2017-and-pyside2/)
- [Vendoring Qt.py](https://fredrikaverpil.github.io/blog/2017/05/04/vendoring-qtpy/)
- [Udemy Course](https://www.udemy.com/python-for-maya/learn/v4/t/lecture/6027394)
- [PythonBytes #77](https://pythonbytes.fm/episodes/show/77/you-don-t-have-to-be-a-workaholic-to-win) (Starts at 5:00)

##### Table of contents

- [Project goals](#project-goals)
- [Install](#install)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Environment Variables](#environment-variables)
  - [Subset](#subset)
  - [Branch binding-specific code](#branch-binding-specific-code)
  - [Override preferred choice](#override-preferred-choice)
  - [QtSiteConfig.py](#qtsiteconfigpy)
  - [Compile Qt Designer files](#compile-qt-designer-files)
  - [Loading Qt Designer files](#loading-qt-designer-files)
  - [sip API v2](#sip-api-v2)
- [Rules](#rules)
- [How it works](#how-it-works)
- [Known problems](#known-problems)
- [Who's using Qt.py?](#whos-using-qtpy)
- [Projects using Qt.py](#projects-using-qtpy)
- [Projects similar to Qt.py](#projects-similar-to-qtpy)
- [Developer guide](#developer-guide)
- [Qt 6 transition guide](#qt-6-transition-guide)

<br>
<br>
<br>

### Project goals

Write once, run in any binding.

Qt.py was born in the film and visual effects industry to address the growing need for software capable of running with more than one flavor of the Qt bindings for Python - PySide, PySide2, PyQt4 and PyQt5.

| Goal                                 | Description
|:-------------------------------------|:---------------
| *Support co-existence*               | Qt.py should not affect other bindings running in same interpreter session.
| *Build for one, run with all*        | Code written with Qt.py should run on any binding.
| *Explicit is better than implicit*   | Differences between bindings should be visible to you.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for more details.

<br>
<br>
<br>

### Install

Qt.py is a single file and can either be [copy/pasted](https://raw.githubusercontent.com/mottosso/Qt.py/master/Qt.py) into your project, [downloaded](https://github.com/mottosso/Qt.py/archive/master.zip) as-is, cloned as-is or installed via `pip` or `conda`.

```bash
# From PyPI
$ pip install Qt.py
```

```bash
# From Anaconda
$ conda config --add channels conda-forge
$ conda install qt.py
```

- Pro tip: **Never use the latest commit for production**. Instead, use [the latest release](https://github.com/mottosso/Qt.py/releases). That way, when you read bug reports or make one for yourself you will be able to match a version with the problem without which you will not know which fixes apply to you nor would we be able to help you. Installing via pip or conda as above ensures you are provided the latest *stable* release. Unstable releases are suffixed with a `.b`, e.g. `1.1.0.b3`.
- Pro tip: Supports [vendoring](https://fredrikaverpil.github.io/blog/2017/05/04/vendoring-qtpy/)

<br>
<br>
<br>

### Usage

Use Qt.py as you would use PySide2.

![image](https://cloud.githubusercontent.com/assets/2152766/15653248/b5ce298e-2683-11e6-8c0c-f041ecae203d.png)

```python
import sys
from Qt import QtWidgets

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Hello World")
button.show()
app.exec_()
```

- Also see [/examples](examples)

<br>
<br>
<br>

### Documentation

All members of `Qt` stem directly from those available via PySide2, along with these additional members.

| Attribute               | Returns     | Description
|:------------------------|:------------|:------------
| `__version__`           | `str`       | Version of this project
| `__binding__`           | `str`       | A string reference to binding currently in use
| `__qt_version__`        | `str`       | Reference to version of Qt, such as Qt 5.6.1
| `__binding_version__`   | `str`       | Reference to version of binding, such as PySide 1.2.6

**Example**

```python
>>> from Qt import __binding__
>>> __binding__
'PyQt5'
```

### Compatibility

Qt.py also provides compatibility wrappers for critical functionality that differs across bindings, these can be found in the added `QtCompat` submodule.

| Attribute                                 | Returns     | Description
|:------------------------------------------|:------------|:------------
| `loadUi(uifile=str, baseinstance=QWidget)`| `QObject`   | Minimal wrapper of PyQt4.loadUi and PySide equivalent
| `translate(...)`        					| `function`  | Compatibility wrapper around [QCoreApplication.translate][]
| `wrapInstance(addr=long, type=QObject)`   | `QObject`   | Wrapper around `shiboken2.wrapInstance` and PyQt equivalent
| `getCppPointer(object=QObject)`           | `long`      | Wrapper around `shiboken2.getCppPointer` and PyQt equivalent
| `isValid(object=QObject)`                 | `bool`      | Wrapper around `shiboken2.isValid` and PyQt equivalent
| `dataChanged(topLeft=QModelIndex, bottomRight=QModelIndex, roles=[])` | `None` | Wrapper around `QtCore.QAbstractItemModel.dataChanged.emit`

[QCoreApplication.translate]: https://doc.qt.io/qt-5/qcoreapplication.html#translate

**Example**

```python
>>> from Qt import QtCompat
>>> QtCompat.loadUi
```

#### Class specific compatibility objects

Between Qt4 and Qt5 there have been many classes and class members that are obsolete. Under Qt.QtCompat there are many classes with names matching the classes they provide compatibility functions. These will match the PySide2 naming convention.

```python
from Qt import QtCore, QtWidgets, QtCompat
header = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
QtCompat.QHeaderView.setSectionsMovable(header, False)
movable = QtCompat.QHeaderView.sectionsMovable(header)
```

This also covers inconsistencies between bindings. For example PyQt4's QFileDialog matches Qt4's return value of the selected. While all other bindings return the selected filename and the file filter the user used to select the file. `Qt.QtCompat.QFileDialog` ensures that getOpenFileName(s) and getSaveFileName always return the tuple.

<br>

##### Environment Variables

These are the publicly facing environment variables that in one way or another affect the way Qt.py is run.

| Variable                  | Type  | Description
|:--------------------------|:------|:----------
| QT_PREFERRED_BINDING_JSON | str   | Override order and content of binding to try. This can apply per Qt.py namespace.
| QT_PREFERRED_BINDING      | str   | Override order and content of binding to try. Used if QT_PREFERRED_BINDING_JSON does not apply.
| QT_VERBOSE                | bool  | Be a little more chatty about what's going on with Qt.py
| QT_SIP_API_HINT           | int   | Sets the preferred SIP api version that will be attempted to set.

<br>

##### Subset (or "common members")

Members of Qt.py is a subset of PySide2. Which means for a member to be made accessible via Qt.py, it will need to (1) be accessible via PySide2 and (2) each of the other supported bindings. This excludes large portions of the Qt framework, including the newly added QtQml and QtQuick modules but guarantees that anything you develop with Qt.py will work identically on any binding - PySide, PySide2, PyQt4 and PyQt5. If you need to use such excluded modules with Qt.py, please see [QtSiteConfig.py](#qtsiteconfigpy).

We call this subset "common members" and these can be generated by running the `build_membership.sh` script. The script will output all modules and members of each binding into individual JSON files. These JSON files are then compared and a `common_members.json` file is generated. The contents of this file is copy-pasted into the `_common_members` dictionary of Qt.py. Please note that the script will only use the very latest version of our [Docker test suite](DOCKER.md) to generate the common members subset, using the most up-to-date set of VFX Platform-stipulated software versions.

:warning: The version of PySide2 used as reference is the one specified on [VFX Platform](http://www.vfxplatform.com/), currently version is 2.0.x. But unfortunately, the version string of PySide2 is not yet properly maintained and the VFX Platform does not specifiy a explicit commit SHA for PySide2. Therefore, it could be difficult to know exactly which PySide2 is running on your system (unless you built it from source). In layman's terms; as PySide2 is in development and is continuously adding new support for modules, you may see differences between PySide2 built early in the year vs PySide2 built later in the year. The exact commit SHAs of PySide2 used by the Qt.py test suite can be reviewed in [DOCKER.md](DOCKER.md). QtC implemented an alternative way to identify which version of PySide2 you are running. You can read more about that [here](https://codereview.qt-project.org/#/c/202199/).

<br>

##### Branch binding-specific code

Some bindings offer features not available in others, you can use `__binding__` to capture those.

```python
if "PySide" in __binding__:
  do_pyside_stuff()
```

<br>

##### Override preferred choice

If your system has multiple choices where one or more is preferred, you can override the preference and order in which they are tried with this environment variable.

```bash
$ set QT_PREFERRED_BINDING=PyQt5  # Windows
$ export QT_PREFERRED_BINDING=PyQt5  # Unix/OSX
$ python -c "import Qt;print(Qt.__binding__)"
PyQt5
```

Constrain available choices and order of discovery by supplying multiple values.

```bash
# Try PyQt4 first and then PySide, but nothing else.
$ export QT_PREFERRED_BINDING=PyQt4:PySide
```

Using the OS path separator (`os.pathsep`) which is `:` on Unix systems and `;` on Windows.

If you need to control the preferred choice of a specific vendored Qt.py you can use the `QT_PREFERRED_BINDING_JSON` environment variable instead.

```json
{
    "Qt":["PyQt5"],
    "myproject.vendor.Qt":["PyQt5"],
    "default":["PySide2"]
}
```

This json data forces any code that uses `import Qt` or `import myproject.vendor.Qt` to use PyQt5(`from x import Qt` etc works too, this is based on `__name__` of the Qt.py being imported). Any other imports of a Qt module will use the "default" PySide2 only. If `"default"` is not provided or a Qt.py being used does not support `QT_PREFERRED_BINDING_JSON`, `QT_PREFERRED_BINDING` will be respected.

```bash
# Try PyQt5 first and then PyQt4 for the Qt module name space.
$ export QT_PREFERRED_BINDING_JSON="{"Qt":["PyQt5","PyQt4"]}"
# Use PyQt4 for any other Qt module name spaces.
$ export QT_PREFERRED_BINDING=PySide2
```

<br>

##### QtSiteConfig.py

Add or remove members from Qt.py at run-time.

-  [Examples](/examples/QtSiteConfig)

<br>

If you need to expose a module that isn't included in Qt.py by default or wish to remove something from being exposed in Qt.py you can do so by creating a `QtSiteConfig.py` module and making it available to Python.

1. Create a new file `QtSiteConfig.py`
2. Implement `update_members`
3. Expose to Python

```python
# QtSiteConfig.py
def update_members(members):
    """Called by Qt.py at run-time to modify the modules it makes available.

    Arguments:
        members (dict): The members considered by Qt.py
    """
    members.pop("QtCore")
```

Finally, expose the module to Python.

```bash
$ set PYTHONPATH=/path/to
$ python -c "import Qt.QtCore"
ImportError: No module named Qt.QtCore
```

> Linux and MacOS users, replace `set` with `export`

<br>

##### Compile Qt Designer files

> WARNING - ALPHA FUNCTIONALITY<br>
> See [#132](https://github.com/mottosso/Qt.py/pull/132) for details.

`.ui` files compiled via `pyside2-uic` inherently contain traces of PySide2 - e.g. the line `from PySide2 import QtGui`.

In order to use these with Qt.py, or any other binding, one must first erase such traces and replace them with cross-compatible code.

```bash
$ pyside2-uic my_ui.ui -o my_ui.py
$ python -m Qt --convert my_ui.py
# Creating "my_ui_backup.py"..
# Successfully converted "my_ui.py"
```

Now you may use the file as you normally would, with Qt.py

<br>

##### Loading Qt Designer files

The `uic.loadUi` function of PyQt4 and PyQt5 as well as the `QtUiTools.QUiLoader().load` function of PySide/PySide2 are mapped to a convenience function `loadUi`.

```python
import sys
from Qt import QtCompat

app = QtWidgets.QApplication(sys.argv)
ui = QtCompat.loadUi(uifile="my.ui")
ui.show()
app.exec_()
```
For `PyQt` bindings it uses their native implementation, whereas for `PySide` bindings it uses our custom implementation borrowed from the [qtpy](https://github.com/spyder-ide/qtpy) project.

`loadUi` has two arguments as opposed to the multiple that PyQt ships with. See [here](https://github.com/mottosso/Qt.py/pull/81) for details - in a nutshell, those arguments differ between PyQt and PySide in incompatible ways.
The second argument is `baseinstance` which allows a ui to be dynamically loaded onto an existing QWidget instance.

```python
QtCompat.loadUi(uifile="my.ui", baseinstance=QtWidgets.QWidget)
```

`uifile` is the string path to the ui file to load.

If `baseinstance` is `None`, the a new instance of the top-level
widget will be created. Otherwise, the user interface is created within
the given `baseinstance`. In this case `baseinstance` must be an
instance of the top-level widget class in the UI file to load, or a
subclass thereof. In other words, if you've created a `QMainWindow`
interface in the designer, `baseinstance` must be a `QMainWindow`
or a subclass thereof, too. You cannot load a `QMainWindow` UI file
with a plain `QWidget` as `baseinstance`.

`loadUi` returns `baseinstance`, if `baseinstance` is provided.
Otherwise it will return the newly created instance of the user interface.

<br>

##### sip API v2

If you're using PyQt4, `sip` attempts to set its API to version 2 for the following:
- `QString`
- `QVariant`
- `QDate`
- `QDateTime`
- `QTextStream`
- `QTime`
- `QUrl`

<br>
<br>
<br>

### Rules

The PyQt and PySide bindings are similar, but not identical. Where there is ambiguity, there must to be a clear direction on which path to take.

**Governing API**

The official [Qt 5 documentation](http://doc.qt.io/qt-5/classes.html) is always right. Where the documentation lacks answers, PySide2 is right.

For example.

```python
# PyQt5 adheres to PySide2 signals and slots
PyQt5.Signal = PyQt5.pyqtSignal
PyQt5.Slot = PyQt5.pyqtSlot

# PySide2 adheres to the official documentation
PySide2.QtCore.QStringListModel = PySide2.QtGui.QStringListModel
```

**Caveats**

There are cases where Qt.py is not handling incompatibility issues. Please see [`CAVEATS.md`](CAVEATS.md) for more information.

<br>
<br>
<br>

### Known Problems

Send us a pull-request with known problems here!

- [Maya and incompatible bindings on PYTHONPATH](https://github.com/mottosso/Qt.py/issues/146)

<br>
<br>
<br>

### Who's using Qt.py?

Send us a pull-request with your studio here.

- [Atomic Fiction](http://www.atomicfiction.com/)
- [Bläck](http://www.blackstudios.se/)
- [Blur Studio](http://www.blur.com)
- [CGRU](http://cgru.info/)
- [Colorbleed](http://www.colorbleed.nl/)
- [Digital Domain](https://www.digitaldomain.com/)
- [Disney Animation](https://www.disneyanimation.com/)
- [Dreamworks Animation](https://github.com/dreamworksanimation)
- [Epic Games](https://www.epicgames.com/)
- [Fido](http://fido.se/)
- [Framestore](https://framestore.com)
- [ftrack](https://www.ftrack.com/)
- [Futureworks](http://futureworks.in/)
- [Industrial Brothers](http://industrialbrothers.com/)
- [Industriromantik](http://www.industriromantik.se/)
- [Mackevision](http://www.mackevision.com/)
- [Method Studios](http://www.methodstudios.com/)
- [Mikros Image](http://www.mikrosimage.com/)
- [Moonbot Studios](http://moonbotstudios.com/)
- [MPC](http://www.moving-picture.com)
- [Overmind Studios](https://www.overmind-studios.de/)
- [Psyop](http://www.psyop.com/)
- [Raynault VFX](https://www.raynault.com/)
- [Rising Sun Pictures](https://rsp.com.au)
- [Rodeo FX](https://www.rodeofx.com/en/)
- [Sony Pictures Imageworks](http://www.imageworks.com/)
- [Spin VFX](http://www.spinvfx.com/)
- [Weta Digital](https://www.wetafx.co.nz/)
- [GermanTechJobs](https://germantechjobs.de)

Presented at Siggraph 2016, BOF!

![image](https://cloud.githubusercontent.com/assets/2152766/17621229/c2448db2-6089-11e6-915f-0604e5d8c7ee.png)

<br>
<br>
<br>

### Projects using Qt.py

Send us a pull-request with your project here.

- [USD Manager](http://www.usdmanager.org)
- [Cosmos](http://cosmos.toolsfrom.space/)
- [maya-capture-gui](https://github.com/BigRoy/maya-capture-gui)
- [pyblish-lite](https://github.com/pyblish/pyblish-lite)
- [pyvfx-boilerplate](https://github.com/fredrikaverpil/pyvfx-boilerplate)
- [riffle](https://gitlab.com/4degrees/riffle)
- [cmt](https://github.com/chadmv/cmt)
- [PythonForMayaSamples](https://github.com/dgovil/PythonForMayaSamples)
- [Kraken](https://github.com/fabric-engine/Kraken)
- [AFANASY](http://cgru.info/afanasy/afanasy)
- [Syncplay](https://github.com/Syncplay/syncplay)
- [BlenderUpdater](https://github.com/overmindstudios/BlenderUpdater)
- [QtPyConvert](https://github.com/DigitalDomain/QtPyConvert)
- [Pyper](https://gitlab.com/brunoebe/pyper.git)

<br>
<br>
<br>

### Projects similar to Qt.py

Comparison matrix.

| Project       | Audience      | Reference binding | License   | PEP8 |Standalone | PyPI   | Co-existence
|:--------------|:--------------|:------------------|:----------|------|:----------|--------|--------------
| Qt.py         | Film          | PySide2           | MIT       | X    | X         | X      | X
| [jupyter][]   | Scientific    | N/A               | N/A       | X    |           |        |
| [QtPy][]      | Scientific    | N/A               | MIT       |      | X         | X      |
| [pyqode.qt][] | Scientific    | PyQt5             | MIT       | X    |           | X      |
| [QtExt][]     | Film          | N/A               | N/A       |      | X         |        |
| [python_qt_binding][] | Robotics | N/A            | BSD       | X    | X        | X       | X

Also worth mentioning, [pyqt4topyqt5](https://github.com/rferrazz/pyqt4topyqt5); a good starting point for transitioning to Qt.py.

Send us a pull-request with your project here.

[QtPy]: https://github.com/spyder-ide/qtpy
[jupyter]: https://github.com/jupyter/qtconsole/blob/master/qtconsole/qt_loaders.py
[pyqode.qt]: https://github.com/pyQode/pyqode.qt
[QtExt]: https://bitbucket.org/ftrack/qtext
[python_qt_binding]: https://github.com/ros-visualization/python_qt_binding

<br>
<br>
<br>

### Developer Guide

Tests are performed on each aspect of the shim.

- [Functional](tests.py)
- [Caveats](build_caveats.py)
- [Examples](examples)

Each of these are run under..

- Python 2.7
- Python 3.4
- Python 3.5
- Python 3.6

..once for each binding or under a specific binding only.

Each test is run within it's own isolated process, so as to allow an `import` to occur independently from other tests. Process isolation is handled via [nosepipe](https://pypi.python.org/pypi/nosepipe).

Tests that are written at module level are run four times - once per binding - whereas tests written under a specific if-statement are run only for this particular binding.

```python
if binding("PyQt4"):
    def test_something_related_to_pyqt4():
        pass
```

**Code convention**

Below are some of the conventions that used throughout the Qt.py module and tests.

- **Etiquette: PEP8**
    - All code is written in PEP8. It is recommended you use a linter as you work, flake8 and pylinter are both good options. Anaconda if using Sublime is another good option.
- **Etiquette: Double quotes**
    - " = yes, ' = no.
- **Etiquette: Napoleon docstrings**
    - Any docstrings are made in Google Napoleon format. See [Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for details.
- **Etiquette: Semantic Versioning**
    - This project follows [semantic versioning](http://semver.org).
- **Etiquette: Underscore means private**
    - Anything prefixed with an underscore means that it is internal to Qt.py and not for public consumption.

**Running tests**

Due to the nature of multiple bindings and multiple interpreter support, setting up a development environment in which to properly test your contraptions can be challenging. So here is a guide for how to do just that using **Docker**.

With Docker setup, here's what you do. Please note this will pull down a ~1 GB image.

```bash
cd Qt.py

# Run nosetests (Linux/OSX)
docker run --rm -v $(pwd):/Qt.py -e PYTHON=2.7 fredrikaverpil/qt.py:2018
docker run --rm -v $(pwd):/Qt.py -e PYTHON=3.4 fredrikaverpil/qt.py:2018
docker run --rm -v $(pwd):/Qt.py -e PYTHON=3.5 fredrikaverpil/qt.py:2018
docker run --rm -v $(pwd):/Qt.py -e PYTHON=3.6 fredrikaverpil/qt.py:2018

# Run nosetests (Windows)
docker run --rm -v %CD%:/Qt.py -e PYTHON=2.7 fredrikaverpil/qt.py:2018
docker run --rm -v %CD%:/Qt.py -e PYTHON=3.4 fredrikaverpil/qt.py:2018
docker run --rm -v %CD%:/Qt.py -e PYTHON=3.5 fredrikaverpil/qt.py:2018
docker run --rm -v %CD%:/Qt.py -e PYTHON=3.6 fredrikaverpil/qt.py:2018

# Doctest: test_caveats.test_1_qtgui_qabstractitemmodel_createindex ... ok
# Doctest: test_caveats.test_2_qtgui_qabstractitemmodel_createindex ... ok
# Doctest: test_caveats.test_3_qtcore_qitemselection ... ok
# ...
#
# ----------------------------------------------------------------------
# Ran 21 tests in 7.799s
#
# OK
```

Now both you and Github Actions are operating on the same assumptions which means that when the tests pass on your machine, they pass on Github Actions. And everybody wins!

For details on the Docker image for testing, see [`DOCKER.md`](DOCKER.md).

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for more of the good stuff.

**Upload to PyPI**

To make a new release onto PyPI, you'll need to be mottosso and type this.

```bash
cd Qt.py
python .\setup.py sdist bdist_wheel
python -m twine upload .\dist\*
```

<br>
<br>
<br>

### Qt 6 Transition Guide

| Replace | With | Notes
|:--------|:-----|:----------------------------
| `QFont().setWeight(...)` | `QtCompat.QFont.setWeight(font, ...)`
| `QFont().setWeight(QFont().Bold)` | `QFont().setWeight(QFont.Bold)` | Instance of class doesn't have the enums, apparently
| `QEvent().Resize` | `QEvent.Resize` | Instance of class doesn't have the enums, seems to apply overall
| `QtCore.Qt.MidButton`  | `QtCompat.Qt.MidButton`
| `QLabel.setPixmap(str)` | `QLabel.setPixmap(QPixmap())` | Can't take a string anymore (tested in Maya 2025.0)
| `QModelIndex.child` | `QModel.index` | This one is apparently from Qt 4 and should not have been in Qt.py to begin with
| `QtSvg.QSvgWidget` | `QtSvgWidgets.QSvgWidget` | Moved to QtSvgWidgets in Qt 6
| | Submit your known issues here! |

##### Removed Members

Many members were removed from Qt.py due to no longer existing in PySide 6.

> If you find where they went, or think some were removed in error, please submit a pull-request!

```json
"QtCore": [
    "QAbstractState",
    "QAbstractTransition",
    "QEventTransition",
    "QFinalState",
    "QSignalTransition",
    "QTextCodec",
    "QTextDecoder",
    "QTextEncoder",
    "QtCriticalMsg",
    "QtDebugMsg",
    "QtFatalMsg",
    "QtSystemMsg",
    "QtWarningMsg",
    "qChecksum",
    "QPictureIO",
],
"QtMultimedia": [
    "QAbstractVideoBuffer",
    "QAbstractVideoSurface",
    "QAudio",
    "QAudioDeviceInfo",
    "QAudioFormat",
    "QAudioInput",
    "QAudioOutput",
    "QVideoFrame",
    "QVideoSurfaceFormat"
],
"QtNetwork": [
    "QNetworkConfiguration",
    "QNetworkConfigurationManager",
    "QNetworkSession",
],
"QtOpenGL": [
    "QGL",
    "QGLContext",
    "QGLFormat",
    "QGLWidget"
],
"QtSql": [
    "QSql",
    "QSqlDatabase",
    "QSqlDriver",
    "QSqlDriverCreatorBase",
    "QSqlError",
    "QSqlField",
    "QSqlIndex",
    "QSqlQuery",
    "QSqlQueryModel",
    "QSqlRecord",
    "QSqlRelation",
    "QSqlRelationalDelegate",
    "QSqlRelationalTableModel",
    "QSqlResult",
    "QSqlTableModel"
],
"QtSvg": [
    "QSvgGenerator",
    "QSvgRenderer",
],
"QtWidgets": [
    "QActionGroup",
    "QDesktopWidget",
    "QDirModel",
    "QKeyEventTransition",
    "QMouseEventTransition",
    "QUndoCommand",
    "QUndoGroup",
    "QUndoStack",
],
"QtX11Extras": [
    "QX11Info"
],
"QtXml": [
    "QXmlAttributes",
    "QXmlContentHandler",
    "QXmlDTDHandler",
    "QXmlDeclHandler",
    "QXmlDefaultHandler",
    "QXmlEntityResolver",
    "QXmlErrorHandler",
    "QXmlInputSource",
    "QXmlLexicalHandler",
    "QXmlLocator",
    "QXmlNamespaceSupport",
    "QXmlParseException",
    "QXmlReader",
    "QXmlSimpleReader"
],
"QtXmlPatterns": [
    "QAbstractMessageHandler",
    "QAbstractUriResolver",
    "QAbstractXmlNodeModel",
    "QAbstractXmlReceiver",
    "QSourceLocation",
    "QXmlFormatter",
    "QXmlItem",
    "QXmlName",
    "QXmlNamePool",
    "QXmlNodeModelIndex",
    "QXmlQuery",
    "QXmlResultItems",
    "QXmlSchema",
    "QXmlSchemaValidator",
    "QXmlSerializer"
]
```

##### Static Members Missing from Instances

An overall change is that instances of classes, like `QFont()` no longer provides access to static members, such as `QFont.Bold`. So things like:

```py
font = QFont()
font.setWeight(font.Bold)
```

Must be replaced with:

```py
font = QFont()
font.setWeight(QFont.Bold)
```

Or:

```py
font.setWeight(type(font).Bold)
```

Tedious and seemingly unnecessary.. But there you have it!

##### Notes

Qt.py 1.4.0, released in May 2024, added support for Qt 6 whilst preserving compatibility with Qt 4 and 5. That means that in most cases, code you've already written for Qt 4 or 5 will now continue to work with Qt 6, such as Maya 2025.

However, some changes between 5 and 6 require up-front work by you the developer to make your codebase run on Qt 6 whilst continuing to run on Qt 4 and 5.

The above is what we know, please do submit issues and pull-request with what else you find!

- https://github.com/mottosso/Qt.py/issues/new

**See also**

The official PySide2 to PySide6 transition guide, which is especially helpful since Qt.py is modeled after PySide2.

- https://doc.qt.io/qtforpython-6/gettingstarted/porting_from2.html
