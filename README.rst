****************************
MR German plugin for unidown
****************************
|maintained| |programming language| |license|

|travis| |appveyor| |readthedocs| |requirements| |codacy| |codecov|

----

This program/script downloads all avaible ebooks from the german MobileRead wiki (http://wiki.mobileread.com/wiki/Free_eBooks-de/de)  
Dieses Programm/ Skript lädt alle verfügbaren eBooks von der deutschen MobileRead Wikiliste (http://wiki.mobileread.com/wiki/Free_eBooks-de/de) herunter.

----

Information - *English*
=======================

Installation
------------

Install Python 3 or greater, don't forget to use the correct architecture. (https://www.python.org/downloads/)
Download and unzip the latest release of this program/ script. (https://github.com/IceflowRE/MR-eBook-Downloader/releases/latest)
Run `InstallMissingModules.sh`. This will install additional required modules for Python.

Usage
-----

Run `Start.sh` (Linux) or `Start.bat` (Windows) or **better** run `StartDeDownload.py` from the command line!

Created data
------------

- `ebook` folder where all ebooks will downloaded.
- `temp` stores the temporary data. At the end this folder should be deleted.
- `udpate.data` saves data over the downloaded ebooks, do not **deleted!** If you want to update or download the ebooks again it will only download the new ones.
- `noEbookFound.txt` stores a list of threads where no ebook was found.
- `failedDownload.txt` stores a list of links where the download was failed. You can try a manual download, if you succeed you should not forget to add an entry to the update.data file.

Expert settings
---------------
Faster download: edit in `MrDeDownloader.py` the line `using_core = 4`, change the number to a higher count. Have in mind that this will strain your PC and the MR server.
Download only specific formats: edit in `MrDeDownloader.py` the line `format_list = ['epub', 'mobi', 'lrf', 'imp', 'pdf', 'lit', 'azw', 'azw3', 'rar', 'lrx']`, remove not needed formats.

Notes
-----
There will be some false positive for examples images or ebooks with wrong extensions e.g. `.pdb` which was a `.epub`.
Have in mind that you can be banned or something similar if you strained the MR server too much.

Information - *Deutsch*
=======================

Installation
------------
Installiere Python 3 oder höher, vergess dabei nicht die richtige Architektur zu wählen. (https://www.python.org/downloads/)
Downloade und entpacke die letzte Veröffentlichung von dem Downloader. (https://github.com/IceflowRE/MR-eBook-Downloader/releases/latest)
Führe `InstallMissingModules.sh` aus. Dies wird gegebenenfalls fehlende, benötigte Python Module installieren.

Benutzung
---------

Starte `Start.sh` (Linux) oder `Start.bat` (Windows) oder **besser**, starte `StartDeDownload.py` von der Kommandozeile aus.

Erstellte Daten
---------------

- `ebook` der Ordner wohin alle eBooks heruntergeladen werden.
- `temp` speichert temporär benötigte Daten. Diese sollten am Ende jedoch wieder gelöscht werden.
- `udpate.data` speichert Daten über die heruntergeladenen eBooks, nicht **löschen!** Falls der Donwloader nochmals ausgeführt wird, werden nur neue und aktualisierte eBooks heruntergeladen.
- `noEbookFound.txt` enthält eine List von Threads in welchen keine eBooks gefunden wurden.
- `failedDownload.txt` enthält eine List von Links wo der Download fehlgeschlagen ist. Ein manueller Download kann versucht werden. Sollte dies klappen sollte man den entsprechenden Eintrag in der update.data ergänzen.

Experteneinstellungen
---------------------

Schnellerer Download: ändere in der `MrDeDownloader.py` Datei die Zeile `using_core = 4`, zu einer höheren Zahl. Beachte dabei jedoch, dass dies den PC und den MR Server stärker belastet.
Nur bestimmte Formate herunterladen: entferne in der `MrDeDownloader.py` Datei, in der Zeile `format_list = ['epub', 'mobi', 'lrf', 'imp', 'pdf', 'lit', 'azw', 'azw3', 'rar', 'lrx']` die entsprechenden Formate.

Hinweis
-------

Es werden einige "falsche" Dateien heruntergeladen, beispielsweise Bilder oder Dateien mit einer falschen Dateiendung zum Beispiel `.pdb`, welche aber eine `.epub` darstellt.
Beachte auch, dass der MR Server stärker belastet wird und ein Ban oder ähnliche Maßnahmen erfolgen können.


----

Web
===

https://github.com/IceflowRE/unidown-mr_de

Credits
=======

- Developer
    - Iceflower S
        - iceflower@gmx.de

Third Party
-----------

nose2
    - Jason Pellerin
    - https://github.com/nose-devs/nose2
    - `BSD-2-Clause <https://github.com/nose-devs/nose2/blob/master/license.txt>`_
Packaging
    - Donald Stufft and individual contributors
    - https://github.com/pypa/packaging
    - `BSD-3-Clause, Apache-2.0 <https://github.com/pypa/packaging/blob/master/LICENSE>`_
Prospector
    - `landscapeio <https://github.com/landscapeio>`_
    - https://github.com/landscapeio/prospector
    - `GPL-2.0+ <https://github.com/landscapeio/prospector/blob/master/LICENSE>`_
Setuptools
    - Jason R Coombs / `Setuptools Developers <https://github.com/orgs/pypa/teams/setuptools-developers>`_
    - https://github.com/pypa/setuptools
    - `MIT <https://github.com/pypa/setuptools/blob/master/LICENSE>`_
tqdm
    - `noamraph <https://github.com/noamraph>`_
    - https://github.com/tqdm/tqdm
    - `MIT, MPL-2.0 <https://raw.githubusercontent.com/tqdm/tqdm/master/LICENCE>`_
twine
    - `various authors <https://github.com/pypa/twine/blob/master/AUTHORS>`_
    - https://github.com/pypa/twine
    - `Apache-2.0 <https://github.com/pypa/twine/blob/master/LICENSE>`_
urllib3
    - `Andrey Petrov and contributors <https://github.com/shazow/urllib3/blob/master/CONTRIBUTORS.txt>`_
    - https://github.com/shazow/urllib3
    - `MIT <https://github.com/shazow/urllib3/blob/master/LICENSE.txt>`_
wheel
    - `Charlie Denton <https://github.com/meshy>`_
    - https://github.com/meshy/pythonwheels
    - `BSD-2-Clause <https://github.com/meshy/pythonwheels/blob/master/LICENSE>`_

License
-------

.. image:: http://www.gnu.org/graphics/gplv3-127x51.png
   :alt: GPLv3
   :align: center

.. Badges.

.. |maintained| image:: https://img.shields.io/badge/maintained-yes-brightgreen.svg

.. |programming language| image:: https://img.shields.io/badge/language-Python_3.7-orange.svg
   :target: https://www.python.org/

.. |license| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |travis| image:: https://img.shields.io/travis/com/IceflowRE/unidown-mr_de/master.svg?label=Travis%20CI
   :target: https://travis-ci.org/IceflowRE/unidown-mr_de
   
.. |appveyor| image:: https://img.shields.io/appveyor/ci/IceflowRE/unidown-mr_de/master.svg?label=AppVeyor%20CI
    :target: https://ci.appveyor.com/project/IceflowRE/unidown_mr_de/branch/master

.. |readthedocs| image:: https://readthedocs.org/projects/unidown/badge/?version=latest
   :target: https://unidown.readthedocs.io/en/latest/index.html

.. |requirements| image:: https://requires.io/github/IceflowRE/unidown/requirements.svg?branch=master
   :target: https://requires.io/github/IceflowRE/unidown/requirements/?branch=master

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/7783e0b9e3734ee6ab43e142b43e9663
   :target: https://app.codacy.com/project/IceflowRE/unidown/dashboard
   
.. |codecov| image:: https://img.shields.io/codecov/c/github/IceflowRE/unidown/master.svg?label=coverage
   :target: https://codecov.io/gh/IceflowRE/unidown

---  

## License
![Image of GPLv3](http://www.gnu.org/graphics/gplv3-127x51.png)

Copyright  ©  Iceflower S

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.  
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  
You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/gpl.html>.