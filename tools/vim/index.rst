.. index:: Vim
.. _Vim-Tool:

Vim
===

`Vim <http://www.vim.org>`_ ist einer der vielseitigsten Text-Editoren aller
Zeiten. Man kann damit nicht nur elegant programmieren, sondern auch Webseiten
erstellen, Emails schreiben, Notizen verwalten, Briefe und Bücher verfassen, und
vieles mehr. 

In allen Bereichen kann durch praktische Tastenkombinationen (insbesondere mit
Snippets) die Tipparbeit, die zum Verfassen, Setzen und Verwalten von Texte
nötig ist, deutlich reduziert werden; nach einer gewissen Eingewöhnungsphase
wird das Arbeitstempo so spürbar höher. Bei täglicher Benutzung gelingen
einzelne Editierungsschritte im Lauf der Zeit mitunter so schnell und
"automatisch", dass sie nur noch im Unterbewusstsein ablaufen und
überhaupt keine Aufmerksamkeit mehr erfordern.. ;-)

.. _Vim-Installation:

.. rubric:: Installation

Auf fast allen Linux-System ist ``vi``, der "kleine Bruder" von Vim, bereits in
der Grundversion enthalten. Bei intensiver Nutzung empfielt es sich allerdings,
eine umfangreichere Version des Vim zu installieren: [#]_


.. code-block:: bash

    sudo aptitude install vim-common vim-runtime vim-gnome vim-scripts \
                          vim-latexsuite ncurses-term


.. toctree::
    :maxdepth: 2

    bedienung.rst
    konfiguration.rst
    plugins.rst
    links.rst

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Vim läuft auch unter Windows- und Apple-Systemen. Hierfür finden sich auf
    der `Vim-Projektseite <http://www.vim.org>`_ unter der Rubrik "Downloads"
    entsprechende Pakete bzw. selbst entpackende Installationsdateien.  


