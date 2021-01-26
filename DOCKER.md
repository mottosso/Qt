## Docker

In order to successfully test Qt.py against the different bindings of different versions, we use Travis-CI to run Docker containers based on [pre-built CentOS-based images](https://hub.docker.com/r/fredrikaverpil/qt.py/tags/).

The Docker images follow the [VFX Reference Platform specifications](http://www.vfxplatform.com/) with some additionals, and are quite jam-packed.


<br>
<br>


**Software built from source**

* glibc<sup>1</sup>
* gcc<sup>1</sup>
* git<sup>2</sup>
* cmake<sup>3</sup>
* Qt4<sup>4</sup>
* Qt5 + Autodesk-modifications<sup>1</sup>
* Qt5 Creator<sup>1, 5</sup>
* SIP<sup>4</sup>
* PyQt4<sup>4</sup>
* PySide<sup>4</sup>
* PyQt5<sup>1</sup>
* PySide2<sup>1</sup>

<sup>1</sup> Per specification from VFX Platform  
<sup>2</sup> Adds possibility to faster clone large repositories  
<sup>3</sup> cmake 3.x required to build PySide2  
<sup>4</sup> Required for Qt.py testing  
<sup>5</sup> Required for `PySide2.QtUiTools`

<br>
<br>


**Software versions**

We create new Docker containers when the VFX Reference Platform is updated; around the time of [SIGGRAPH](http://www.siggraph.org) (usually July/August) each year.

We abide the software versions stipulated by the VFX Platform reference. But for other software required by Qt.py, we checkout specific commit SHAs or source archives rather than going for the always-latest version of software. This also helps to re-build Docker images later, if needed.

There are non-strict rules (guidelines) for choosing software versions to build:

- No commit SHA can be newer than the commit SHA from PySide2
- No binding's commit SHA can be older than their respective Qt commit SHA

Other noteworthy things:

- PySide cannot be built with anything newer than Python 3.4.
- SIP is used by both PyQt4 and PyQt5 and its version must therefore be chosen carefully.
- PySide2 does not have a maintained `__version__` string as of Qt.py v1.1.0.b3.
- All Qt bindings and Qt itself are built using their respective 5.6.x branch.

<br>
<br>


**Image tagging**

A new image should be tagged like `repo/qt.py:YYYY`. For CY2018, this translates into `fredrikaverpil/qt.py:2018-update1`.

If there happens to be an update between VFX Platform specifications, a revision version number could be added: `repo/qt.py:YYYY-update1`.

Build command example:

    docker build . -t fredrikaverpil/qt.py:2018-update1 -f Dockerfile.vfxplatform2018-update1

<br>
<br>


**Enter the container**

For debugging reasons, you can enter the container like this:

```bash
docker run --rm --interactive --tty --entrypoint=bash fredrikaverpil/qt.py:2018-update1
```

You can then run `python2.7`, `python3.4`, `python3.5`, `python3.6` and so on (depending on which Python versions were built).

<br>
<br>

**Dockerfile.vfxplatform2018-update1**

| Software | Date | Details |
| -------- | ---- | --------------- |
| PySide2 | 2017-08-24 | [commit](http://code.qt.io/cgit/pyside/pyside-setup.git/commit/?h=5.6&id=117e0ff91275b4bc06dd5383f19e7028c5ef6ff8) |
| PySide | 2015-10-15 | [commit](https://github.com/pyside/pyside-setup/commit/7860bda363438e96fa9e810def0858635a9766cc) |
| SIP | 2016-07-25 | [v4.18.1](https://sourceforge.net/projects/pyqt/files/sip/) |
| PyQt5 | 2016-04-25 | [v5.6](https://sourceforge.net/projects/pyqt/files/PyQt5/) |
| PyQt4 | 2015-08-01 | [v4.11.4](https://sourceforge.net/projects/pyqt/files/PyQt4/) |
| Python 2.7 | 2015-12-05 | [v2.7.11](https://www.python.org/downloads/source/) |
| Python 3.4 | 2017-08-09 | [v3.4.7](https://www.python.org/downloads/source/) |
| Python 3.5 | 2017-08-08 | [v3.5.4](https://www.python.org/downloads/source/) |
| Python 3.6 | 2017-07-17 | [v3.6.2](https://www.python.org/downloads/source/) |
| Qt5 | 2016-06-16 | [commit](http://code.qt.io/cgit/qt/qt5.git/commit/?h=5.6&id=4566f0ac50e5ea143943c1251028fb01c70289ce) |
| Adsk Qt5 `qtbase` | 2017-06-07 | [commit](https://github.com/autodesk-forks/qtbase/commit/c4e51d0162f7619c83e25e623ecd3bc549932040) |
| Adsk Qt5 `qtx11extras` | 2017-02-24 | [commit](https://github.com/autodesk-forks/qtx11extras/commit/c6c59d5d902db8be3661cab929be85a38fda0faa) |
| Adsk Qt5 `qtdeclarative` | 2017-05-09 | [commit](https://github.com/autodesk-forks/qtdeclarative/commit/b14cd49f891327d8fa5f5607eb19288ca137c5e2) |
| Qt5 Creator | 2017-08-09 | [commit](http://code.qt.io/cgit/qt-creator/qt-creator.git/commit/?h=4.3&id=a094841bdda5461ebeaeab4620dde8222fa8312d) |
| Qt4 | 2015-10-23 | [commit](http://code.qt.io/cgit/qt/qt.git/commit/?id=0a2f2382541424726168804be2c90b91381608c6) |
| cmake | 2017-07-18 | [v3.9.0](https://cmake.org/files/) |
| glibc | 2012 (installed via yum) | 2.17 |
| gcc | 2016-12-...? (installed via devtoolset-6) | [v6.3.1] |

<br>
<br>


**Dockerfile.vfxplatform2018**

| Software | Date | Details |
| -------- | ---- | --------------- |
| PySide2 | 2017-08-24 | [commit](http://code.qt.io/cgit/pyside/pyside-setup.git/commit/?h=5.6&id=117e0ff91275b4bc06dd5383f19e7028c5ef6ff8) |
| PySide | 2015-10-15 | [commit](https://github.com/pyside/pyside-setup/commit/7860bda363438e96fa9e810def0858635a9766cc) |
| SIP | 2016-07-25 | [v4.18.1](https://sourceforge.net/projects/pyqt/files/sip/) |
| PyQt5 | 2016-04-25 | [v5.6](https://sourceforge.net/projects/pyqt/files/PyQt5/) |
| PyQt4 | 2015-08-01 | [v4.11.4](https://sourceforge.net/projects/pyqt/files/PyQt4/) |
| Python 2.7 | 2015-12-05 | [v2.7.11](https://www.python.org/downloads/source/) |
| Python 3.4 | 2017-08-09 | [v3.4.7](https://www.python.org/downloads/source/) |
| Python 3.5 | 2017-08-08 | [v3.5.4](https://www.python.org/downloads/source/) |
| Python 3.6 | 2017-07-17 | [v3.6.2](https://www.python.org/downloads/source/) |
| Qt5 | 2016-06-16 | [commit](http://code.qt.io/cgit/qt/qt5.git/commit/?h=5.6&id=4566f0ac50e5ea143943c1251028fb01c70289ce) |
| Adsk Qt5 `qtbase` | 2017-06-07 | [commit](https://github.com/autodesk-forks/qtbase/commit/c4e51d0162f7619c83e25e623ecd3bc549932040) |
| Adsk Qt5 `qtx11extras` | 2017-02-24 | [commit](https://github.com/autodesk-forks/qtx11extras/commit/c6c59d5d902db8be3661cab929be85a38fda0faa) |
| Qt5 Creator | 2017-08-09 | [commit](http://code.qt.io/cgit/qt-creator/qt-creator.git/commit/?h=4.3&id=a094841bdda5461ebeaeab4620dde8222fa8312d) |
| Qt4 | 2015-10-23 | [commit](http://code.qt.io/cgit/qt/qt.git/commit/?id=0a2f2382541424726168804be2c90b91381608c6) |
| cmake | 2017-07-18 | [v3.9.0](https://cmake.org/files/) |
| glibc | 2012 (installed via yum) | 2.17 |
| gcc | 2015 (installed via devtoolset-4) | [v5.3.1] |

<br>
<br>


**Dockerfile.vfxplatform2017**

| Software | Date | Details |
| -------- | ---- | --------------- |
| PySide2 | 2016-06-03 | [commit](https://codereview.qt-project.org/gitweb?p=pyside/pyside-setup.git;a=commit;h=8913156381b7dc51f903b9e459c143fb25097cab) |
| PySide | 2015-10-15 | [commit](https://github.com/pyside/pyside-setup/commit/7860bda363438e96fa9e810def0858635a9766cc) |
| SIP | 2016-07-25 | [v4.18.1](https://sourceforge.net/projects/pyqt/files/sip/) |
| PyQt5 | 2016-04-25 | [v5.6](https://sourceforge.net/projects/pyqt/files/PyQt5/) |
| PyQt4 | 2015-08-01 | [v4.11.4](https://sourceforge.net/projects/pyqt/files/PyQt4/) |
| Python 2.7 | 2015-12-05 | [v2.7.11](https://www.python.org/downloads/source/) |
| Python 3.4 | 2016-06-27 | [v3.4.5](https://www.python.org/downloads/source/) |
| Python 3.5 | 2015-12-07 | [v3.5.1](https://www.python.org/downloads/source/) |
| Qt5 | 2016-06-01 | [commit](http://code.qt.io/cgit/qt/qt5.git/commit/?h=v5.6.1&id=adf7bcc0b1785c451b06f13c049e5b946b393705) |
| Adsk Qt5 `qtbase` | 2016-06-28 | [commit](https://github.com/autodesk-forks/qtbase/commit/72e3fbb0d27e5d91b1676312ab6a7f6a979ed4e7) |
| Adsk Qt5 `qtx11extras` | 2016-06-28 | [commit](https://github.com/autodesk-forks/qtx11extras/commit/d86b59059f0340f3707dad008a8f632b070de4e6) |
| Qt5 Creator | 2016-06-09 | [commit](http://code.qt.io/cgit/qt-creator/qt-creator.git/commit/?h=v4.0.2&id=47b4f2c73834dd971a5ce418368b5d991d08a666) |
| Qt4 | 2015-10-23 | [commit](http://code.qt.io/cgit/qt/qt.git/commit/?id=0a2f2382541424726168804be2c90b91381608c6) |
| cmake | 2016-04-15 | [v3.5.2](https://cmake.org/files/) |
| glibc | 2010 (pre-installed in CentOS 6) | 2.12 |
| gcc | 2014-05-12 | [v4.8.3](ftp://ftp.gnu.org/pub/gnu/gcc/) |

