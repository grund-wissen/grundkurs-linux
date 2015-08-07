.. index:: tmux
.. _tmux:

Der Terminal-Multiplexer tmux
=============================

``tmux`` erlaubt es (ebenso wie sein Vorgänger :ref:`screen <screen>`), aus
einem einzelnen Shell-Fenster eine ganze Shell-Session mit mehreren Fenstern und
Unterfenstern zu erstellen. Ein wesentliche Weiterentwicklung gegenüber ``screen``
ist die verbesserte Konfigurierbarkeit.

Mittels :ref:`aptitude <aptitude>` kann ``tmux`` über das gleichnamige Paket
installiert werden:

.. rubric:: Installation und Einführung

Tmux kann via :ref:`aptitude <apt>` über das gleichnamige Paket ``tmux``
installiert werden:

.. code-block:: bash

    sudo aptitude install tmux

Gibt man anschließend in einem Shell-Fenster ``tmux`` ein, so wird eine neue
``tmux``-Session gestartet. Am unteren Rand des Shell-Fensters wird dabei eine
(standardmäßig) grüne Informationsleiste eingeblendet, die als eine Art
"Tableiste" angesehen werden kann. Zunächst ist nur ein Fenster geöffnet, wobei
die Nummerierung in ``tmux`` (standardmäßig) mit Null beginnt.

Um ein weiteres Fenster zu erstellen, kann entweder ``tmux new-window``
eingegeben werden oder -- bei den Standard-Einstellungen -- ``Ctrl b`` und
anschließend ``c`` ("create") gedrückt werden. In der Infoleiste werden nun zwei
Fenster aufgelistet, zwischen denen mit ``Ctrl b`` und ``n`` beziehungsweise
``p`` ("next" beziehungsweise "previous") gewechselt werden kann.

.. tab-completion: https://superuser.com/questions/579545/how-to-tab-completion-when-typing-command-in-tmux

.. _Konfiguration von tmux:

Konfiguration von tmux
----------------------

Standardmäßig leitet ``Ctrl b`` eine ``tmux``-Anweisung ein; es kann allerdings
auch jede andere Tastenkombination hierfür verwendet werden. Dazu wird eine
Datei ``~/.tmux.conf`` angelegt:

.. code-block:: bash

    touch ~/.tmux.conf

In diese Datei kann beispielsweise folgender Eintrag aufgenommen werden, um den
``tmux``-Hotkey auf ``Ctrl d`` festzulegen:

.. code-block:: bash

    # Neu-Definition der Präfix-Taste:
    set-option -g prefix C-d

Damit dieser Eintrag wirksam wird, muss die Konfigurationsdatei neu geladen
werden. Dies erfolgt mittels ``tmux source``:

.. code-block:: bash

    tmux source ~/.tmux.conf

Um einfacher mit der Konfigurationsdatei ``.tmux.conf`` zu experimentieren und
die dortigen Einträge unmittelbar "live" testen zu können, empfiehlt es sich,
dort eine Tastenkombination für das Neuladen der Konfigurationen zu definieren:

.. code-block:: bash

    # Tastenkürzel zum Laden der Konfigurationsdatei:
    bind-key r source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."

Wird die Konfigurationsdatei noch einmal mit ``tmux source ~/.tmux.conf`` neu
geladen, so kann man künftig dafür auch einfacher ``Ctrl d`` und ``r`` eingeben.

.. rubric:: Tastenkürzel ohne Präfix

Mit ``bind-key`` lassen sich auch Tastenkürzel definieren, die ohne den
tmux-Hotkey auskommen. Dies kann beispielsweise verwendet werden, um mittels
``Shift Links`` und ``Shift rechts`` zwischen den offenen Tabs zu wechseln,
mit ``Shift unten`` einen neuen Tab zu erzeugen und mit ``Shift oben`` dem
aktuellen Tab manuell einen festen Namen zu geben. Die entsprechenden Einträge
in der Konfigurationsdatei lauten:

.. code-block:: bash

    # Schnelles Öffnen und Umbenennen von Fenstern:
    bind-key -n S-Down new-window
    bind-key -n S-Up command-prompt -I "rename-window "

    # Schnelles Navigieren zwischen Fenstern:
    bind-key -n S-Left previous-window
    bind-key -n S-Right next-window

Die Option ``-n`` bedeutet dabei, dass das Tastenkürzel nicht den tmux-Hotkey
als Präfix erwartet. In gleicher Weise kann definiert werden, dass mittels
``Ctrl Shift Links`` beziehungsweise ``Ctrl Shift Rechts`` das aktuelle Fenster
in der Infoleiste nach links beziehungsweise rechts verschoben wird:

.. code-block:: bash

    # Schnelles Verschieben von Fenstern
    bind-key -n C-S-Left swap-window -t -1
    bind-key -n C-S-Right swap-window -t +1

Soll ein Fenster geschlossen werden, kann entweder ``Ctrl d x`` oder ``exit``
eingegeben werden. Entstehen durch das Schließen von Fenstern "Lücken" in der
Nummerierung der Fenster, so kann für eine automatische Re-Nummerierung ``tmux
move-window -r`` aufgerufen werden oder in der Konfigurationsdatei ein
entsprechendes Tastenkürzel definiert werden, beispielsweise ``bind-key m
move-window -r``.

.. rubric:: Weitere Optionen

Folgende Optionen für die Konfigurationsdatei können ebenfalls nützlich sein:

.. code-block:: bash

    # Anzahl an History-Einträgen auf 10000 erhöhen:
    set-option -g history-limit 10000

    # Nummerierung der Fenster und Teilfenster jeweils mit 1 beginnen:
    set-option -g base-index 1
    set-window-option -g pane-base-index 1

    # Pfeiltasten sofort nach Fenster-Wechsel freigeben:
    set-option -g repeat-time 0

    # Maus-Unterstützung aktivieren:
    set-window-option -g mode-mouse on
    set-option -g mouse-select-window on
    set-option -g mouse-select-pane on
    set-option -g mouse-resize-pane on

    # Farb-Optionen für Shell-Fenster:
    set-option -g default-terminal screen-256color

    # Inhalt der Infoleiste ändern:
    set -g status-interval 2
    set -g status-left '[#S]'
    set -g status-right '%l:%M'
    set -g status-utf8 on
    set-option -g status-justify left
    set-window-option -g window-status-current-format '#I:#W#F'
    set-window-option -g window-status-format '#I:#W#F'

    # Aussehen der Infoleiste ändern:
    set-option -g status on
    set-option -g status-bg blue
    set-option -g status-fg white
    set-window-option -g window-status-current-bg magenta

    # Aussehen der Kommandozeile ändern:
    set -g message-fg white
    set -g message-bg black
    set -g message-attr bright

    # Aussehen von Teilfenstern ("Panes") anpassen:
    set -g pane-border-fg green
    set -g pane-border-bg black
    set -g pane-active-border-fg green
    set -g pane-active-border-bg black

    # Aktive Shell-Fenster visuell hervorheben:
    setw -g monitor-activity on
    set -g visual-activity on

    # Automatische Neu-Nummerierung der Fenster aktivieren:
    # (Beispielsweise nach dem Schließen eines Fensters)
    set -g renumber-windows on


Bei Verwendung der ``zsh`` sollten zudem die folgenden Beiträge in der Datei
``.tmux.conf`` stehen, um ein automatisches Umbenennen von Fenstern bei einem
Programmaufruf oder einem Verzeichniswechsel zu verhindern:

.. code-block:: bash

    set-window-option -g automatic-rename off
    set-option -g allow-rename off



Mit den obigen Einstellungen können zum einen Fenster in der Infoleiste auch
mit der Maus ausgewählt werden, zum anderen wird das Aussehen der Infoleiste
angepasst: Die Hintergrundfarbe wird auf allgemein auf blau, die Farbe des
aktuellen Fensters auf magenta festgelegt; andere aktive Fenster werden in
weißer Farbe markiert. Die Nummerierung der Fenster beginnt von nun an mit
``1``, rechts wird die aktuelle Uhrzeit angezeigt.

Die Verwendung von Teilfenstern wird im Abschnitt :ref:`Teilfenster ("Panes")
<Fenster und Teilfenster>` näher beschrieben.

.. rubric:: Tab-Vervollständigung

Bei Verwendung der ``bash``-Shell ist für ``tmux`` leider keine
Tab-Vervollständigung der einzelnen möglichen Anweisungen vordefiniert.
Beispielsweise kann in einer Shell nicht ``tmux bi<TAB>`` eingegeben werden, um
eine Vervollständigung zu ``tmux bind-key`` zu erhalten. Dieses nützliche
Feature kann man für die ``bash``-Shell allerdings durch das folgende Skript
erhalten: [#]_

:download:`tmux-completion.sh <tmux-completion.sh>`

Speichert man diese Datei beispielsweise im Verzeichnis ``~/bin``, so sollte man
folgenden Eintrag in der Datei ``~/.bashrc`` hinzufügen, damit die
Vervollständigung automatisch geladen wird:

.. code-block:: bash

    # Tmux-Completion laden:
    source ~/bin/tmux-completion.sh

Anschließend können in einem neuen Shell-Fenster tmux-Anweisungen automatisch
mit ``Tab`` ergänzt oder, falls keine eindeutige Ergänzung möglich ist, durch
Drücken von ``Tab Tab`` alle möglichen Ergänzungen eingeblendet werden.

.. _Sitzungen, Fenster und Teilfenster:

Sitzungen, Fenster und Teilfenster
----------------------------------

Am linken Rand der Infoleiste wird bei Verwendung der im vorherigen Abschnitt
beschriebenen Konfiguration der Name der tmux-Session angezeigt. Wird ``tmux``
ohne weitere Argumente aufgerufen, so werden die einzelnen Sessions automatisch
durchnummeriert. Wird allerdings ``tmux new -s myname`` aufgerufen, so wird eine
neue Session mit der Bezeichnung ``myname`` erzeugt. Dies ist insbesondere
nützlich, wenn ein tmux-Fenster beispielsweise für das Vim-Vicle-Plugin als
"Code-Empfänger" verwendet werden soll.

Auch aus einem anderen Grund sollten tmux-Sessions benannt werden: Wird
beispielsweise das Shell-Hauptfenster geschlossen, das die tmux-Session
beinhaltet, so ist die tmux-Session nicht verloren, sondern hat lediglich den
status "deattached". Gibt man in einem anderen Shell-Fenster ``tmux
list-sessions`` ein, so werden alle Sessions aufgelistet. Hieß die vermeintlich
geschlossene tmux-Session beispielsweise ``myname`` genannt, so kann sie
folgendermaßen wieder reaktiviert ("attached") werden:

.. code-block:: bash

    tmux attach-session -t myname

Die Option ``-t`` gibt hierbei die Zielsession ("target") an. Die Session wird
so mitsamt allen Fenstern und Teilfenstern wieder geladen. Auf diese Weise kann
zum Beispiel ein Shell-Fenster weiter aktiv bleiben, auch wenn der Benutzer
abgemeldet ist.

.. Umgekehrt: "Spiegeln" einer Session auf zwei PCs via ssh?


.. _Panes:
.. _Fenster und Teilfenster:

.. rubric:: Fenster und Teilfenster ("Panes")

Jedes tmux-Fenster kann bei Bedarf in zwei oder mehrere Unterfenster ("Panes")
aufgeteilt weden. Dazu sind folgende Tastenkürzel-Definitionen in der
Konfigurationsdatei ``~/.tmux.conf`` nützlich:

.. code-block:: bash

    bind - split-window -v # Horizontales Halbieren des aktuellen Fensters
    bind | split-window -h # Vertikales Halbieren des aktuellen Fensters


.. _Templates für neue Tmux-Sitzungen:

Templates für neue Tmux-Sitzungen
---------------------------------

Tmux-Sitzungen können leider nicht gespeichert werden, wenn der Computer
ausgeschaltet wird. Es gibt allerdings mit `Tmuxinator
<http://aokolish.me/blog/2013/02/12/using-tmux-and-tmuxinator/>`_ ein
ergänzendes Programm, mit dem auf einfache Weise Templates für neue
``tmux``-Sitzungen erstellt werden können.

Zur Installation von ``tmuxinator`` gibt man in einem Shell-Fenster folgende
Zeile ein:

.. code-block:: bash

    sudo gem install tmuxinator

Um ein neues Template für beispielsweise eine Sitzung mit Namen ``work`` zu
erzeugen, gibt man folgendes ein:

.. code-block:: bash

    tmuxinator new work

Hierdurch wird im Ordner ``~/.tmuxinator`` eine Datei ``top.yml`` angelegt, die
eine Beispiel-Struktur sowie in auskommentierter Form mögliche Optionen mitsamt
Beschreibung enthält. Beispielsweise kann so festgelegt werden, welche Fenster
in der Sitzung vorkommen sollen, welche Verzeichnisse in den einzelnen Fenstern
aktiv und welche Programme ausgeführt werden sollen:

.. code-block:: bash

    # ~/.tmuxinator/work.yml

    name: work
    root: ~/data/homepage/work

    windows:
      - linux: vim
        root: ~/data/homepage/work/linux
      - python:
        root: ~/data/homepage/work/informatik/python
      - mc: mc

Eine gemäß diesem Beispiel definierte neue ``tmux``-Sitzung umfasst drei
Fenster, die ``linux``, ``python`` und ``mc`` genannt sind. Im ersten Fenster
soll dabei ``vim`` aufgerufen werden, im dritten ``mc``; die
aktiven Arbeitsverzeichnisse können entweder explizit angegeben werden oder
entsprechen dem angegebenen ``root``-Pfad.

Die Sitzung kann folgendermaßen erzeugt:

.. code-block:: bash

    tmuxinator work

    # oder kürzer:

    mux work

Da beim Start der Sitzungen beispielsweise auch Dienste gestartet und innerhalb
der Fenster optional weitere Unterfenster erzeugt werden können, kann
``tmuxinator`` ein Speichern der ``tmux``-Sitzungen zumindest weitgehend
ersetzen.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#] Bei Verwendung der ``zsh`` mit der ``oh-my-zsh``-Konfiguration
    funktioniert die ``tmux``-Vervollständigung automatisch.
