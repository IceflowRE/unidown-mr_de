**********************************
MR german books plugin for unidown
**********************************
|maintained| |programming language| |license|

|travis| |appveyor| |requirements| |codacy|

----

This program/script downloads all available ebooks from the german MobileRead wiki (https://wiki.mobileread.com/wiki/Free_eBooks-de/de)
Dieses Programm lädt alle verfügbaren eBooks von der deutschen MobileRead Wikiliste (https://wiki.mobileread.com/wiki/Free_eBooks-de/de) herunter.

----

Information - *English*
=======================

Installation
------------

Install Python 3 or greater. (https://www.python.org/downloads/)

Open a terminal and install with:

.. code-block:: shell

    pip install unidown-mr_de

Usage
-----

Open a terminal:

.. code-block:: shell

    unidown -p mr_de

Options
-------

There are some optional options you can choose from:

delay
    Delay (seconds) between the downloads (default: 2s).
format
    Download only the specified format (default: all formats).

Example:

.. code-block:: shell

    unidown -p mr_de delay=4 format=epub,mobi,lrf,imp,pdf,lit,azw,azw3,rar,lrx

Donwloaded files
----------------

By default the program creates a downloads folder in the executing directory. So the ebooks are in `./downloads/mr_de`.

Notes
-----
There will be some false positive for examples images or ebooks with wrong extensions e.g. `.pdb` which was a `.epub`.

You should have in mind that the MR server was not intended for this automatically/ machine usage.

Information - *Deutsch*
=======================

Installieren
------------

Installiere Python 3 or höher. (https://www.python.org/downloads/)

Öffne ein Terminal und installiere es mit:

.. code-block:: shell

    pip install unidown-mr_de

Benutzen
--------

Öffne ein Terminal:

.. code-block:: shell

    unidown -p mr_de

Optionen
--------

Es können verschieden optionale Optionen hinzugefügt werden.

delay
    Verzögerung (Sekunden) zwischen den Downloads (Standard: 2s).
format
    Lädt nur die spezifizierten Formate herunter (Standard: jedes Format).

Beispiel:

.. code-block:: shell

    unidown -p mr_de delay=4 format=epub,mobi,lrf,imp,pdf,lit,azw,azw3,rar,lrx

Heruntergeladene Dateien
------------------------

Standardmäßig erstellt das Programm in dem Ordner, von wo es ausgeführt wurde einen Downloadordner, so sind die eBooks dann in `./downloads/mr_de`.

Hinweis
-------

Du solltest beachten, dass die MR Server nicht für diese automatische/ maschinelle Benutzung gedacht sind.

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
    - `BSD-2-Clause <https://github.com/nose-devs/nose2/blob/master/license.txt>`__
Packaging
    - Donald Stufft and individual contributors
    - https://github.com/pypa/packaging
    - `BSD-3-Clause, Apache-2.0 <https://github.com/pypa/packaging/blob/master/LICENSE>`__
Prospector
    - `landscapeio <https://github.com/landscapeio>`_
    - https://github.com/landscapeio/prospector
    - `GPL-2.0+ <https://github.com/landscapeio/prospector/blob/master/LICENSE>`__
Setuptools
    - Jason R Coombs / `Setuptools Developers <https://github.com/orgs/pypa/teams/setuptools-developers>`_
    - https://github.com/pypa/setuptools
    - `MIT <https://github.com/pypa/setuptools/blob/master/LICENSE>`__
tqdm
    - `noamraph <https://github.com/noamraph>`_
    - https://github.com/tqdm/tqdm
    - `MIT, MPL-2.0 <https://raw.githubusercontent.com/tqdm/tqdm/master/LICENCE>`__
twine
    - `various authors <https://github.com/pypa/twine/blob/master/AUTHORS>`_
    - https://github.com/pypa/twine
    - `Apache-2.0 <https://github.com/pypa/twine/blob/master/LICENSE>`__
urllib3
    - `Andrey Petrov and contributors <https://github.com/shazow/urllib3/blob/master/CONTRIBUTORS.txt>`_
    - https://github.com/shazow/urllib3
    - `MIT <https://github.com/shazow/urllib3/blob/master/LICENSE.txt>`__
wheel
    - `Charlie Denton <https://github.com/meshy>`_
    - https://github.com/meshy/pythonwheels
    - `BSD-2-Clause <https://github.com/meshy/pythonwheels/blob/master/LICENSE>`__

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
   :target: https://travis-ci.com/IceflowRE/unidown-mr_de
   
.. |appveyor| image:: https://img.shields.io/appveyor/ci/IceflowRE/unidown-mr-de/master.svg?label=AppVeyor%20CI
    :target: https://ci.appveyor.com/project/IceflowRE/unidown-mr-de/branch/master

.. |requirements| image:: https://requires.io/github/IceflowRE/unidown-mr_de/requirements.svg?branch=master
   :target: https://requires.io/github/IceflowRE/unidown-mr_de/requirements/?branch=master

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/8b542926cd9e445c97545f2245aac712
   :target: https://www.codacy.com/app/IceflowRE/unidown-mr_de

---  

## License
![Image of GPLv3](http://www.gnu.org/graphics/gplv3-127x51.png)

Copyright  ©  Iceflower S

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.  
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  
You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/gpl.html>.
