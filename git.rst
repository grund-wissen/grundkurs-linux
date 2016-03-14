.. index:: Versionskontrolle, git
.. _Git:

Versionskontrolle mit Git
=========================

Das Versionssystem Git ist bei den meisten Distributionen bereits
vorinstalliert. Möchte man Git mit einer graphischen Oberfläche benutzen, so
können wahlweise `giggle <https://wiki.gnome.org/Apps/giggle>`_, `gitk
<http://gitk.sourceforge.net/>`_, `qgit
<http://sourceforge.net/projects/qgit>`_, `git-gui
<https://www.kernel.org/pub/software/scm/git/docs/git-gui.html>`_ oder `git-cola
<https://git-cola.github.io/>`_ als Pakete nachinstalliert werden; zudem
existiert mit `tig <http://jonas.nitro.dk/tig/>`_ eine sehr konfigurierbare
textbasierte Bedienoberfläche:

.. code-block:: bash

    sudo aptitude install giggle gitk qgit git-gui git-cola tig

Die Bedienoberflächen können dann mittels ``giggle`` beziehungsweise ``gitk``,
``qgit``, ``git gui``, ``git-cola`` beziehungsweise ``tig`` gestartet werden.
Alle Programme können nach einer gewissen Einarbeitungszeit für ein schnelleres
Arbeiten und für eine graphisch ansprechende Darstellung der Entwicklungszweige
eines Projekts nützlich sein. Allerdings ist es auch bei Verwendung dieser
Programme hilfreich, die wichtigsten Git-Anweisungen und Konzepte zu kennen.

.. http://jonas.nitro.dk/tig/tigrc.5.html

Ausführliche englischsprachige Anleitungen zu den einzelnen Git-Anweisungen, die
im folgenden vorgestellt werden, finden sich in den Linux-Manpages und können
allgemein mit  ``man git-init``, ``man git-config``, ``man git-commit``, usw.
aufgerufen werden.

.. index:: git; init
.. _Einführung:

Einführung: Ein neues Git-Projekt erstellen
-------------------------------------------

Um testhalber ein neues Git-Projekt zu erstellen, kann man in einer Shell
folgendes eingeben:

.. code-block:: bash

    mkdir git-test  && cd git-test
    git init

Zunächst wird im obigen Beispiel ein neues Verzeichnis erstellt, anschließend
wird in diesem ein neues Projekt initiiert. Dabei wird automatisch ein
Unterverzeichnis ``.git`` angelegt; in diesem ist das gesamte Git-Repository
inklusive der kompletten Versionsgeschichte in komprimierter Form gespeichert.

.. rubric:: Konfiguration von Git

Jedes ``.git``-Verzeichnis enthält unter anderem eine Konfigurationsdatei namens
``config``, die standardmäßig folgenden Inhalt hat::

    [core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true

Die Datei sollte bei einer erstmaligen Verwendung von Git um folgenden Eintrag
ergänzt werden::

    [user]
        name="Vorname Nachname"
        email="email@adresse.de"

Möchte man Git für eigene Projekte häufiger verwenden, ist eine "globale"
Konfiguration sinnvoll, die nicht nur für das aktuelle Projekt, sondern für alle
Projekte des Benutzers gilt. Derartige Einstellungen werden in der Datei
``~/.gitconfig`` gespeichert. Die Konfigurationen können entweder mittels eines
Texteditors direkt in dieser Datei vorgenommen werden, oder in entsprechender
Weise mittels ``git config`` gesetzt werden:

.. code-block:: bash

    git config --global user.name "Vorname Nachname"
    git config --global user.email "email@adresse.de"

Mit ``git config -l`` können die bestehende Einstellungen angezeigt werden.


.. index:: git; add

.. rubric:: Veränderungen speichern

Nimmt man innerhalb des Projektverzeichnisses eine Änderung vor, erstellt
beispielsweise mittels ``touch README`` eine leere Datei, so kann man
anschließend mittels ``git add README`` die neue Datei, oder einfacher ``git add
.`` alle neuen Dateien im Verzeichnis in den Index der zu berücksichtigenden
Dateien hinzufügen:

.. code-block:: bash

    git add .

Bei Benutzung von ``git add`` kann ein beliebiges Dateimuster angegeben werden,
beispielsweise würden durch ``git add *.txt`` alle Dateien mit der Endung
``.txt`` in den Index der zu versionierenden Dateien aufgenommen.

.. index:: git; commit

Die Änderungen können dann mittels ``git commit`` gespeichert werden:

.. code-block:: bash

    git commit -a -m "Initial Commit: Adding a README file."

Die beiden angegebenen Optionen ``-a`` und ``-m`` haben folgende Bedeutung:

* Die Option ``-a`` steht für ein automatisches Speichern aller veränderten
  Daten; mittels dieser Option kann ein Aufruf von ``git add *`` unmittelbar vor
  dem Commit ersetzt werden.
* Die Option ``-m "Beschreibung"`` fügt eine obligatorische Nachricht dem hinzu,
  die kurz den Grund des Commits beschreibt; Lässt man diese Option weg, so wird
  durch die ``commit``-Anweisung automatisch der durch die Shell-Variable
  ``$EDITOR`` festgelegte Standard-Texteditor zur Eingabe einer Commit-Nachricht
  geöffnet.

Statt ``git commit -a -m`` kann auch kürzer ``git commit -am`` geschrieben
werden.


.. index:: git; log

.. rubric:: Status und Veränderungen anzeigen

Den bisherigen Versionsverlauf kann man sich mit ``git log`` anzeigen lassen.
Dieser sieht nach dem ersten Commit etwa wie folgt aus: [#]_

.. code-block:: bash

    git log

    # Ergebnis:

    # commit 9812b1b0121ac9159e745ba87a0cd31c9306e3bc
    # Author: Bernhard Grotz <info@grund-wissen.de>
    # Date:   Sun Mar 29 10:43:03 2015 +0200

    # Initial commit: Adding a README file.

.. index:: git; tag

Jeder Commit wird in Git durch eine 40 Zeichen lange Hash-ID-Zeichenkette
symbolisiert. Möchte man einen bestimmten Commit besonders hervorheben, um
beispielsweise auf eine neue Funktion in einem Software-Projekt hinzuweisen, so
kann man den Commit mit einem "Tag" versehen:

.. code-block:: bash

    git tag -a tagname -m "Add a comment here."

.. index:: git; status

Um anzuzeigen, inwiefern sich der aktuelle Stand des Projekts vom Stand des
letzten Commits unterscheidet, kann ``git status`` aufgerufen werden. Wurde noch
keine weitere Veränderung vorgenommen, so zeigt diese Anweisung folgendes an:

.. code-block:: bash

    git status

    # Ergebnis:

    # Auf Branch master
    # nichts zu committen, Arbeitsverzeichnis unverändert

Ändert man die README-Datei etwas ab, beispielsweise mittels ``echo "Hallo Git!"
> README``, so zeigt ``git status`` folgendes an:

.. code-block:: bash

    git status

    # Ergebnis:

    # Auf Branch master
    # Änderungen, die nicht zum Commit vorgemerkt sind:
    #   (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
    #   (benutzen Sie "git checkout -- <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)

    #     geändert:               README

    # keine Änderungen zum Commit vorgemerkt (benutzen Sie "git add" und/oder "git commit -a")

Um die Änderungen in die Versionierung zu übernehmen, kann man wiederum ``git
commit -am "Beschreibung"`` aufrufen.

.. index:: gitignore
.. _gitignore:
.. _kDateien ignorieren:

.. rubric:: Dateien ignorieren

Bei Verwendung von Git gibt es zwei Möglichkeiten, Dateien von der Versionierung
auszunehmen:

* In einer Datei ``.gitignore`` im Projektverzeichnis werden Dateien oder
  Dateimuster festgelegt, die innerhalb des lokalen Verzeichnisses von Git
  ignoriert werden sollen.

* In der Datei ``~/.git/info/exclude`` können Dateien oder Dateimuster angegeben
  werden, die unabhängig von einem konkreten Projekt stets von Git ignoriert
  werden sollen. [#]_

In einer Ignore-Datei können die in der Shell üblichen Dateimuster genutzt
werden:

.. code-block:: bash

    # Alle Dateien in "_build"-Verzeichnis ignorieren:
    _build/

    # Dateimuster ignorieren:
    *.pyc
    *.o
    *.aux
    *.swp
    *.log
    *.tmp

Sollen Dateien oder Verzeichnisse nur dann ignoriert werden, wenn sich diese
unmittelbar im Projektverzeichnis, aber nicht in einem Unterverzeichnis
befinden, so kann vor den Datei- beziehungsweise Verzeichnisnamen ein ``/``
vorangestellt werden. Git interpretiert dies als Zeichen für die erste Ebene des
Projektverzeichnisses, nicht wie die Shell als Quelle des Verzeichnisbaums.

Soll eine Datei oder ein Verzeichnis explizit beachtet werden, obwohl es auf ein
Ignore-Muster zutrifft, kann unmittelbar vor das Muster (ohne Leerzeichen
dazwischen) ein ``!`` geschrieben werden.

Ausführliche Beschreibungen zu ``.gitignore``-Dateien und Shell-Dateimustern
kann man in den Manualseiten mittels ``man gitignore`` beziehungsweise ``man
glob`` oder unter https://git-scm.com/docs/gitignore nachlesen.

Arbeitsverzeichnis, Index und Objektspeicher
--------------------------------------------

In Git wird ein Projektverzeichnis mitsamt allen Versionen der verwalteten
Dateien als Repository bezeichnet. In jedem solchen Repository gibt es drei
verschiedene Speicher-Ebenen:

* Als Arbeitsverzeichnis ("working directory") wird das Projektverzeichnis in
  der aktuellen Version bezeichnet; Dateien früherer Versionen sind darin nicht
  unmittelbar sichtbar.

* Als Index ("stage") wird die Zwischenebene bezeichnet, die beim nächsten
  Aufruf von ``git commit`` die nächste Instanz des Arbeitsverzeichnisses
  ausmacht. Dateien, die sich im Index befinden, werden als "staged" bezeichnet.
  Veränderte Dateien werden allgemein mittels ``git add`` in den Index
  übernommen.

* Als Objektspeicher bezeichnet man die Datenbank, in welcher auch die
  vergangenen Versionen des Repositorys gespeichert sind. Durch ``git commit``
  werden die Änderungen aus dem Index in den Objektspeicher übernommen.

.. todo::

    Mittels git checkout oder git reset können Dateien wieder aus dem
    Objektspeicher ins Arbeitsverzeichnis geladen werden.

.. rubric:: Der "Lebenszyklus" von versionierten Dateien

Dateien, die in einem Projektverzeichnis neu erstellt werden, werden von Git
nicht automatisch in die Versionierung aufgenommen -- sie sind "unstaged" und
müssen erst mittels ``git add`` explizit in den Index aufgenommen werden.
Anschließend werden so hinzugefügte Dateien als "unmodified" angesehen. Diesen
Status haben ebenso alle Dateien, die seit dem letzten Commit nicht verändert
wurden.

Werden bestehende, von Git berücksichtigte Dateien verändert, so ändert sich ihr
Status in "modified". Mittels ``git add`` können sie zum Index hinzugefügt
werden. Nach einem Commit sind all diese Dateien (in der neu gespeicherten
Version) wiederum "unmodified".

Sollen die Änderungen einer Datei beim Commiten unberücksichtigt bleiben, so
kann die Datei mittels ``git rm --cached dateiname`` wieder aus dem Index
gelöscht werden; die Datei bleibt dann als "unstaged" im Arbeitsverzeichnis
bestehen. Wird die Option ``--cached`` weggelassen, wird die Datei sowohl aus
dem Index wie auch aus dem Arbeitsverzeichnis gelöscht.



.. index:: git; branch
.. _Arbeiten mit Entwicklungszweigen:
.. _Branch:

Arbeiten mit Entwicklungszweigen (Branching)
--------------------------------------------

Nach dem ersten Commit wird von Git automatisch ein Entwicklungszweig ("Branch")
namens ``master`` eingerichtet. Möchte man nun am bestehenden Projekt
experimentieren, beispielsweise neue Funktionen ausprobieren, so kann man dies
mittels eines neuen Entwicklungszweigs tun, ohne dass dies Auswirkungen auf den
eigentlichen ``master``-Branch hat.

Ein neuer Branch wird mittels ``git branch`` angelegt:

.. code-block:: bash

    # Entwicklungszweig des Projekts erstellen:
    git branch dev

Wird ``git branch`` ohne weitere Argumente aufgerufen, so werden alle Branches
des Projekts aufgelistet, wobei der aktuell ausgewählte Entwicklungszweig mit
einem ``*``-Zeichen markiert ist.

.. code-block:: bash

    # Branches anzeigen:
    git branch

    # Ergebnis:

        dev
      * master

.. index:: git; checkout

Ein Wechsel zwischen den einzelnen  Entwicklungszweigen ist mittels ``git
checkout`` möglich:

.. code-block:: bash

    # In den dev-Branch wechseln:
    git checkout dev

.. index:: git; stash

Git erlaubt nur dann einen Checkout eines anderen Branches, wenn der aktuelle
Branch "clean" ist, also keine Änderungen zum Committen anstehen. Möchte man
dennoch ohne neuen Commit einen Branch verlassen, so können die in der
Zwischenzeit vorgenommenen Änderungen mittels ``git stash`` zwischengespeichert
werden. Mittels ``git stash list`` kann angezeigt werden, ob aktuell in einem
Entwicklungszweig Änderungen zwischengespeichert wurden; im jeweiligen
Entwicklungszweig können mittels ``git stash apply`` die zwischengespeicherten
Änderungen wiederum übernommen werden.


Im Projektverzeichnis ist immer nur ein einzelner Branch "aktiv". Hat man
beispielsweise den Branch ``dev`` ausgewählt und führt dort einen Commit durch,
so ist dieser Commit nur für diesen Branch wirksam. Wenn dann bei einer neueren
Version im ``dev``-Branch Dateien im Projektverzeichnis erstellt zur
Versionierung hinzugefügt wurden, so werden diese ebenfalls nur dann im
Arbeitsverzeichnis angezeigt, wenn der zugehörigen Entwicklungsbranch aktiv ist.
Git speichert die Dateien intern im Objektspeicher, löscht sie gegebenenfalls
beim Verlassen den Entwicklungsbranches und fügt sie automatisch wieder ins
Arbeitsverzeichnis ein, wenn der Entwicklungsbranch wieder aktiviert wird. [#]_

Branches kann man sich allgemein als Zeiger auf einzelne Commits vorstellen. Sie
helfen dabei, ein Projekt in logische Teile zu untergliedern. Man sollte
allgemein *früh* und *oft* neue Branches bei der Entwicklung eines Projekts
anlegen.

.. todo: Release-Branches
.. todo: git flow!!
.. http://nvie.com/posts/a-successful-git-branching-model/

.. index:: git; merge
.. _Zusammenführen von Entwicklungszweigen:
.. _Merge:

Zusammenführen von Entwicklungszweigen (Merging)
------------------------------------------------

Um die Entwicklungen eines Branches in einen anderen Branch zu übernehmen, wird
zunächst mittels ``git checkout`` der Zielbranch ausgewählt. Von diesem aus wird
dann ``git merge`` unter Angabe des einzubindenden Entwicklungsbranches
aufgerufen.

Angenommen, im ``master``-Branch befindet sich eine Datei ``file.txt``. Nach dem
Erstellen und Auswählen eines entsprechenden Branches soll die Datei im neuen
Entwicklungszweig geändert werden:

.. code-block:: bash

    # Branch erstellen und eine Datei ändern:
    git branch test
    git checkout test
    echo "Test Test Test" > file.txt

Sollten die Datei ``file.txt`` oder andere Dateien im Entwicklungszweig beim
Aufruf von ``git status`` als "untracked" angezeigt werden, so kann mittels
``git addremove`` der Index komplett aktualisiert werden -- neue Dateien Dateien
werden dabei zum Index hinzugefügt, manuell gelöschte Dateien entfernt.

.. TODO: Vorsicht!

Nach einem ``git commit`` im neuen ``test``-Branch eilt dieser dem
``master``-Branch in der Entwicklung voraus, wie man mittels ``git log``
erkennen kann. Sollen die Änderungen in den ``master``-Branch übernommen werden,
gibt man folgendes ein:

.. code-block:: bash

    # master-Branch auswählen und Änderungen übernehmen:
    git checkout master
    git merge test

Sofern sämtliche Entwicklungen im Entwicklungsbranch -- wie im obigen Beispiel
-- aktueller sind als im Zielbranch, funktioniert ein Merge stets ohne Probleme:
Die Änderungen werden im Zielbranch übernommen und die Version des Zielbranches
automatisch angepasst.

.. rubric:: Konkurrierende Änderungen verwalten

Konflikte können auftreten, wenn nach dem Erstellen eines neuen Branches
Veränderungen sowohl im ``master``- wie auch im Entwicklungsbranch vorgenommen
werden:

.. code-block:: bash

    # Änderung im test-Branch vornehmen:
    git checkout test
    echo "La La La" >> file.txt

    git commit -am "changing file.txt"

    # Änderung im master-Branch vornehmen:
    git checkout master
    echo "Ha Ha Ha" >> file.txt

    git commit -am "changing file.txt"

Versucht man nun im ``master``-Branch mittels ``git merge`` die Änderungen aus
dem Entwicklungsbranch zu übernehmen, so bekommt man eine Fehlermeldung
angezeigt, da Git nicht weiß, in welche Richtung die Änderungen übernommen
werden sollen:

.. code-block:: bash

    git merge test

    # Ergebnis:
    # Automatisches Zusammenfügen von file.txt
    # KONFLIKT (Inhalt): Merge-Konflikt in file.txt
    # Automatischer Merge fehlgeschlagen; beheben Sie die Konflikte und committen Sie dann das Ergebnis.

.. index:: git; mergetool

Eine einfache Methode, um einen solchen aus konkurrierenden Änderungen
resultierenden Konflikt zu beheben, ist der Aufruf von ``git mergetool``. Ist
kein Standard-Werkzeug durch eine Option vorgegeben (beispielsweise mittels
``git config --global merge.tool vimdiff``), so kann ein zur Verfügung stehendes
Werkzeug zum Anzeigen der konkurrierenden Änderungen ausgewählt werden.

Die zu ändernden Stellen werden von Git folgendermaßen gekennzeichnet::

    <<<<<<< HEAD:file.txt
    Diese Änderungen wurden im master-Branch vorgenommen
    =======
    Diese Änderungen wurden im test-Branch vorgenommen
    >>>>>>> test:file.txt

Um das Merging abzuschließen, muss manuell eine der konkurrierenden Stellen
ausgewählt oder eine andere Änderung vorgenommen werden; die Marker müssen dabei
ebenfalls entfernt werden, da erst dann die Konflikte von Git als bereinigt
angesehen werden.

Anschließend können die Änderungen mit  ``git commit -am "Beschreibung"`` dem
Index hinzugefügt und gespeichert werden.

.. _Arbeiten mit externen Repositories:

Arbeiten mit externen Repositories
----------------------------------

Git als Versionskontrollsystem wurde vorrangig entwickelt, um die Zusammenarbeit
zwischen mehreren Entwicklern zu erleichtern. Ein Gedanke dabei war und ist,
dass ein gemeinschaftlich bearbeitetes Projekt auf einem zentralen Server liegt,
die einzelnen Entwickler sich Kopien dieses Projekts herunterladen können, lokal
Entwicklungen vornehmen und diese schließlich wieder in das zentral gespeicherte
Projekt einfließen lassen.

.. index:: git; clone

.. _Externe Repositories herunterladen:

.. rubric:: Externe Repositories herunterladen

Um ein existierendes Repository von einem externen Server, beispielsweise von
`GitHub <https://www.github.com>`_  oder `Bitbucket <https://bitbucket.org/>`_
herunterzuladen, gibt man in der Shell folgende Anweisung an:

.. code-block:: bash

    # Allgemein: git clone https://github.com/UserName/RepositoryName.git

    # Beispiel:
     git clone https://github.com//grund-wissen/grundkurs-linux.git

Die ``clone``-Anweisung bewirkt, dass eine vollständige Kopie des Repositorys
(mitsamt Versionsgeschichte) heruntergeladen und als neuer Unterordner im
aktuellen Verzeichnis gespeichert wird. Mit dieser Kopie des Repositorys kann
lokal wie in jedem anderen Repository gearbeitet werden.

.. index:: git; push
.. _Eigene Repositories hochladen:

.. rubric:: Eigene Repositories hochladen

Die am meisten verwendete Methode, um Repositories anderen Entwicklern auf einem
zentralen Server zugänglich zu machen, ist die Nutzung von `GitHub
<https://www.github.com>`_  oder `Bitbucket <https://bitbucket.org/>`_. Auf
beiden Webseiten wird kostenloser Speicherplatz für öffentliche Repositories
angeboten (private Repositories sind oftmals kostenpflichtig). Auf beiden
Webseiten muss entsprechend der Angaben auf der jeweiligen Webseite ein
Nutzer-Account unter Angabe eines Benutzernamens, eines Passworts und einer
Emailadresse erstellt werden.

Innerhalb des Nutzer-Accounts von beispielsweise GitHub wird mittels der
Web-Oberfläche ein neues Repository angelegt. Es ist empfehlenswert, aber nicht
zwingend notwendig, dieses ebenso zu nennen wie das lokale Projektverzeichnis.
Das auf diese Weise neu angelegte Repository wird dann folgendermaßen als Quelle
("origin") des lokalen Repositorys festgelegt:

.. code-block:: bash

    # Allgemein: git add origin https://github.com/UserName/RepositoryName.git

    # Beispiel:
    git remote add origin https://github.com/grund-wissen/grundkurs-linux.git

Ist das lokale Repository ein Clon eines externen Repositorys, so ist die
``origin``-Variable bereits gesetzt. Mit ``git remote -v`` werden die
entsprechenden Adressen und Branches angezeigt.

Die zu einem Remote-Namen gehörende Adresse kann bei Bedarf folgendermaßen
geändert werden:

.. code-block:: bash

    git remote set-url origin https://github.com/new-name

Bevor das lokale Repository hochgeladen wird, sollte noch eine Datei
``README.rst`` oder ``README.md`` (wahlweise mit `ReStructuredText
<https://de.wikipedia.org/wiki/ReStructuredText>`_ oder `MarkDown
<https://de.wikipedia.org/wiki/Markdown>`_ -Syntax) für eine kurze
Projektbeschreibung sowie eine ``LICENSE``-Datei mit Lizenz-Hinweisen
hinzugefügt werden. Auch eine ``AUTHORS``-Datei mit einer Auflistung der aktiv
am Projekt beteiligten Entwickler ist durchaus üblich.

Das Hochladen funktioniert mittels der Anweisung ``git push``:

.. code-block:: bash

    git push -u origin master

Die ``push``-Anweisung bewirkt, dass alle lokal neu hinzugekommenen Commits in
das externe Repository übernommen werden. Die Option ``-u`` bewirkt eine
Synchronisierung beider Repositories und sollte immer dann verwendet werden,
wenn möglicherweise mehrere Entwickler am gleichen Branch arbeiten.


.. index:: git; pull
.. index:: git; fetch
.. _Lokale Repositories aktualisieren:

.. rubric:: Lokale Repositories aktualisieren

Um neue Commits von einem externen Reposotory in ein zugehöriges lokales
Repository zu übernehmen, können die Anweisungen ``git pull`` oder ``git fetch``
verwendet werden:

* ``git pull`` holt die Änderungen aus dem externen Repository und fügt diese
  dem Index der beim nächsten Commit zu berücksichtigenden Dateien hinzu.

* ``git fetch`` führt zunächst ``git pull`` aus, gefolgt von ``git merge``.


Voraussetzung für beide Anweisungen ist wiederum (wie im letzten Abschnitt
beschrieben), dass ein externes Repository als ``origin`` festgelegt ist. Gibt
es konkurrierende Änderungen, so müssen diese wiederum, wie im Abschnitt
:ref:`Merging <Merge>` beschrieben, manuell beispielsweise mit ``git mergetool``
in Einklang gebracht werden.


.. _Forks und Pull Requests:

.. rubric:: Forks und Pull Requests

GitHub bietet unter der Bezeichnung "Fork" eine komfortable Methode,
Repositories von einem anderen Entwickler als Clone in den eigenen
Benutzeraccount zu übernehmen. Dazu genügt ein Klick auf den Fork-Button im
entsprechenden Repository.

An diesem "Fork" des Original-Projekts kann man nun arbeiten und entwickeln
werden, ohne Angst haben zu müssen, im Original etwas kaputt machen zu können.
Hat man einen Teil des Codes ergänzt oder verbessert, so kann man durch einen
Klick auf den entsprechenden Button im geforkten Repository dem Maintainer des
Originals einen "Pull Request" senden, durch den dieser eine Benachrichtigung
über die neue Entwicklung erhält. Der Maintainer kann dann entscheiden, ob er
diese Änderungen des Codes übernimmt oder nicht.

Bei der Arbeit mit der lokalen Kopie des Repositories gibt es nun allerdings
*zwei* externe Repositories, mit denen der Clon in Kontakt steht: Das
Haupt-Repository und den Fork. Praktischerweise richtet man sich dafür eine
zweite Remote-Adresse ein, die man beispielsweise "upstream" nennt, weil sie die
Hauptquelle angibt; "origin" sollte dann entsprechend auf den Fork zeigen.

.. code-block:: bash

    git remote add upstream https://github.com/path-to-main-repository
    git remote set-url origin https://github.com/path-to-fork-repository

Mit diesen Einstellungen können nun neue Commits aus dem ``upstream``-Repository
geholt und mit den lokalen Änderungen gemerged werden; das Ergebnis kann
wiederum in das ``origin``-Repository gepushed werden.


.. rubric:: Links

* `Git Tutorial 1
  <http://www.online-tutorials.net/programmierung/git/tutorials-t-3-263.html>`_
* `Git Tutorial 2 <http://blog.cnlpete.de/2010/10/git-tutorial/>`_
* `Git Tutorial 3 <http://wiki.siduction.de/index.php?title=GIT-Tutorial:_Übersicht>`_
* `Git Tutorial 4 <http://www.hameister.org/Git.html>`_
* `Git Tutorial 5 <http://www.ralfebert.de/tutorials/git/>`_

* `Learning Git Branching <https://pcottle.github.io/learnGitBranching/>`_

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Log-Nachrichten können in einer übersichtlicheren Version ausgegeben
    werden (einzeilig, mit abgekürzten Commit-Hashes und Syntax-Highlighting),
    indem man sich folgende Abkürzung ("Alias") definiert:

    ``git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset
    -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
    --abbrev-commit --date=relative"``

    Nach dieser Definition wird in allen Repositories des Benutzers ``git lg``
    als neue Abkürzung erkannt und dabei.

    (Dieser Hinweis stammt ursprünglich von `Filipe Kiss
    <https://coderwall.com/p/euwpig/a-better-git-log>`_).

.. [#] Es kann anstelle von ``~/.git/info/exclude`` auch eine andere Datei als
    "globale" Ignore-File festgelegt werden. Die Syntax hierfür lautet
    beispielsweise ``git config --global core.excludesfile ~/.gitignore``.

.. [#] Git speichert beim Commits und Branches nicht den gesamten Inhalt aller
    Dateien, sondern (in komprimierter Form) nur die jeweiligen Änderungen relativ
    zur vorhergehenden Version.


