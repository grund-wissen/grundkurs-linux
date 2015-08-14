.. index:: Verschlüsselung
.. _Verschlüsselung mit LUKS:

Exkurs: Verschlüsselung mit LUKS
================================

.. index:: cryptsetup, LUKS
.. _Die Partitions-Verschlüsselung:

Die Partitions-Verschlüsselung
------------------------------

Die Verschlüsselung einer Partition -- auf internen wie auf externen
Datenträgern -- mit `Cryptsetup und LUKS <http://wiki.ubuntuusers.de/LUKS>`_
funktioniert in einem `Shell-Fenster <http://wiki.ubuntuusers.de/Terminal>`_
immer nach dem gleichen Schema:

#. Herausfinden, welche Device-Stelle einem Datenträger bzw. einer Partition
   zugeordnet ist:

   .. code-block:: bash

       sudo fdisk -l

   Angenommen, in einem Rechner ist eine Festplatte enthalten, auf der sich drei
   Partitionen befinden: Eine Partition für das Basis-System ``/``, eine für das
   Home-Verzeichnis ``/home`` und eine als Swap (erweiterter Arbeitsspeicher).
   Der obige Befehl würde die Partitionen dann als ``/dev/sda1``, ``/dev/sda1``
   und ``/dev/sda3`` anzeigen.

   Weitere Festplatten, USB-Sticks usw. erhalten fortlaufend die Bezeichnung
   ``/dev/sdb``, ``/dev/sdc``, ``/dev/sdd``, usw. Die angehängte Nummer gibt die
   Partitionsnummer auf dem Datenträger an. Die gewünschte Partition erkennt man
   an ihrer Größe (angegeben in Menge an Datenblöcken).

#. Falls nur ein Teil eines Datenträgers oder freien Bereichs genutzt werden
   soll: Erstellen einer neuen Partition mit einem Partitions-Programm
   (Empfehlung: `GParted <http://wiki.ubuntuusers.de/GParted>`_).

#. Einrichten einer LUKS-Partition mit ``cryptsetup``:

   .. code-block:: bash

       sudo cryptsetup -c aes-xts-plain -y -s 512 luksFormat /dev/sd<Partition>
       sudo cryptsetup luksOpen /dev/sd<Partition> crypt_name
       sudo mkfs.ext4 /dev/mapper/crypt_name

   Anstelle ``mkfs.ext4`` kann auch ``mkfs.vfat`` verwendet werden, um ein mit
   Windows-Systemen kompatibles Dateisystem einzurichten.

#. Einbinden der neuen Partition in einen beliebigen Verzeichnispfad.

   .. code-block:: bash

       sudo mkdir /media/crypt
       sudo mount /dev/mapper/crypt_name /media/crypt

Die Partition kann von diesem Moment an über den entsprechenden Verzeichnispfad
(im Beispiel ``/media/crypt``) wie ein großer Daten-Ordner genutzt werden.

.. _Einbinden bestehender LUKS-Partitionen:

.. rubric:: Einbinden bestehender LUKS-Partitionen

Moderne Linux-Systeme wie Linux Mint erkennen automatisch verschlüsselte
Datenträger (z.B. USB-Sticks oder externe Festplatten) und öffnen ein
entsprechendes Dialog-Fenster zur Passworteingabe.

Von Hand lässt sich eine bestehende LUKS-Partition nach folgendem Schema in ein
laufendes System einbinden ("mounten"):

.. code-block:: bash

    sudo cryptsetup luksOpen /dev/sdb1 crypt_name
    sudo mount /dev/mapper/crypt_name /media/crypt

Sowohl der beim Öffnen der Partition vergebene Crypt-Name als auch der beim
Mounten festgelegte Einhänge-Punkt sind frei wählbar.

Das Aushängen einer -- von keinem Programm benutzten -- LUKS-Partition erfolgt
durch ein Anklicken des Datenträger-Icons auf dem Desktop mit der rechten
Maustaste oder in einem Shell-Fenster nach folgendem Schema:

.. code-block:: bash

    sudo umount /media/crypt
    sudo cryptsetup luksClose /dev/mapper/crypt_name

Ein Herunterfahren des Systems bewirkt ebenfalls ein Aushängen und
Verschließen aller eingehängten Partitionen.

Wird eine Partition ausschließlich von einem Nutzer verwendet, so empfiehlt sich
als Mount-Pfad anstelle ``/media/crypt`` am besten ein Ordner im
Home-Verzeichnis, beispielsweise ``/home/tux/crypt``. Der Benutzer hat dann auch
ohne Root-Rechte vollen Lese- und Schreibzugriff auf alle Daten der Partition.

..
    Um die obigen Befehle nicht bei jedem Einbinden erneut eingeben zu müssen,
    können sie in eine Textdatei kopiert und diese unter
    ``/home/benutzername/bin/kurzer-befehlsname`` abgelegt werden..

    * `Encrypt an partition with cryptsetup
      <http://www.2030.tk/wiki/Encrypt_an_partition_with_cryptsetup>`_

.. _Die System-Verschlüsselung:

Die System-Verschlüsselung
--------------------------

Mittels `Cryptsetup und Luks <http://wiki.ubuntuusers.de/LUKS>`_ können nicht
nur USB-Sticks und Festplatten oder Partitionen verschlüsselt werden. Es ist bei
Neu-Installationen via Live-CD bzw. Live-USB-Stick auch möglich das gesamte
System bis auf einen notwendigen Boot-Bereich zu verschlüsseln. [#]_ Grundlegende
Linux- bzw. Kommandozeilen-Kenntnisse sollten dabei allerdings vorhanden sein.


.. _Nötige Partitionen erstellen und verschlüsseln:

.. rubric:: Nötige Partitionen erstellen und verschlüsseln

Vor der Installation werden zwei primäre Partitionen angelegt. Sie lassen sich
beispielsweise bei einer `Linux Mint <http://linuxmint.com/>`_-Installation
mittels des graphischen, leicht bedienbaren und bereits auf der Live-CD
enthaltenen Programms ``gparted`` erstellen:

.. list-table::
    :widths: 20 20 20

    * - Partition
      - Name
      - Größe
    * - eine Boot-Partition
      - ``/dev/sda1``
      - 300 bis 500 MB
    * - eine restliche Partition
      - ``/dev/sda2``
      - min. 15 GB

Die obigen Partitionsnamen können auch vertauscht sein, entscheidend ist zu
wissen, welche jeweils gemeint ist. Als Formatierung verwende ich am liebsten
das schnelle, sichere und wartungsarme Dateisystem ``ReiserFS``. In Anlehnung an
die erprobte `Original-Anleitung (en.)
<http://aptosid.com/index.php?module=wikula&tag=FullDiskEncryptionTheDebianWay>`_
werden nun in einem Terminal als Superuser (``su`` eingeben!) nacheinander
folgende Schritte durchlaufen:

#. Formatierung der Boot-Partition:

   .. code-block:: bash

     mkfs.reiserfs -l boot /dev/sda1

#. Anlegen eines verschlüsselten System-Devices:

   .. code-block:: bash

       cryptsetup luksFormat --cipher aes-cbc-essiv:sha256 /dev/sda2
       cryptsetup luksOpen /dev/sda2 sda2_crypt

#. Aufteilung des Crypt-Devices in zwei Bereiche (``logical volume``): Einen
   ``swap``-Bereich, welcher dem System zur Auslagerung von Dateien dient
   (erweiterter Arbeitsspeicher, 1 bis 4 GB), sowie die eigentliche
   Systempartition ``root`` mit dem restlichen Festplattenspeicher:

   .. code-block:: bash

       pvcreate /dev/mapper/sda2_crypt
       vgcreate cryptVG /dev/mapper/sda2_crypt
       lvcreate -n swap -L 4G cryptVG
       lvcreate -n root -l 100%FREE cryptVG

#. Formatierung der neuen Bereiche:

   .. code-block:: bash

       mkswap -L swap /dev/cryptVG/swap
       mkfs.reiserfs -l root /dev/cryptVG/root


.. _Installations-Routine und nachträgliche Anpassungen:

.. rubric:: Installations-Routine und nachträgliche Anpassungen

Nun kann der Installations-Assistent gestartet werden. Hierzu klickt man das
entsprechende Icon auf dem Desktop an und füllt die nötigen Felder (gewünschter
Benutzername, Passwörter, Zeitzone, Tastaturlayout, etc.) aus. Im
Partitions-Auswahlmenü ist darauf zu achten, dass die Bereiche richtig
eingebunden werden:

    .. list-table::
        :widths: 25 25

        * - Partition
          - Einhängepunkt
        * - ``/dev/mapper/cryptVG-root``
          - ``/``
        * - ``/dev/sda1``
          - ``/boot``

Nach dieser Basis-Installation, die Abhängig von der Hardware-Geschwindigkeit
zwischen 15 und 30 Minuten dauert, müssen noch folgende Anpassungen vorgenommen
werden:

#. Einbinden des neuen Systems:

   .. code-block:: bash

       mkdir /media/sidux
       mount /dev/cryptVG/root /media/sidux
       mount /dev/sda1 /media/sidux/boot

#. Drei Dateien müssen nun mit einem Texteditor erstellt bzw. angepasst werden:

   - Die Datei ``/media/sidux/etc/crypttab`` muss folgendes Schema aufweisen::

       # target    source_device                           key_file  options
       sda2_crypt  /dev/disk/by-uuid/[UUID of /dev/sda2]   none      luks

     Die UUID einer Partition bekommt man in einem separaten Terminal-Fenster im
     Verzeichnis ``/dev/disk/by-uuid`` mittels ``ls -l`` (long list) angezeigt.
     Sie sieht ungefähr so aus: ``550e8400-e29b-11d4-a716-446655440000``. Es
     genügt, die passende UUID mit der Maus zu markieren, um sie im anderen
     Fenster per mittlerem Mausklick an gewünschter Stelle einfügen zu können.

   - In der ``/media/sidux/etc/initramfs-tools/conf.d/cryptroot`` (die Datei
     existiert noch nicht!) muss folgendes eingetragen werden::

       target=sda2_crypt,source=UUID=[UUID of your /dev/sda2],lvm=cryptVG-root

   - Die Datei ``/etc/initramfs-tools/modules`` muss noch um folgende Einträge
     (einen je Zeile) ergänzt werden::

       aes-i586
       aes-x86_64
       xts
       gf128
       sha256

#. Nun kann man die Installation durch folgende Kommandos abschließen:

   .. code-block:: bash

       chroot /media/sidux
       mount -t proc proc /proc
       mount -t sysfs sysfs /sys
       update-initramfs -u
       umount proc
       umount sys
       exit
       reboot

Nach einem Reboot wird nun beim Start ein Passwort verlangt, bevor das
System wie gewohnt hochfährt.


.. _Login von Live-Disk:

.. rubric:: Login von Live-Disk

Sollte beim Starten des PCs die verschlüsselte Partition nicht erkannt werden
(und damit ein Booten unmöglich sein), so kann das System dadurch zum Laufen
gebracht werden, indem man mittels einer Live-Disk (oder einem Live-Stick)
bootet und als Superuser folgende Zeilen in einer Shell eingibt:

.. code-block:: bash

    cryptsetup luksOpen /dev/sda2 root
    mkdir /media/root
    pvscan
    lvscan
    vgscan
    vgchange -ay

Damit werden die vorhandenen Partitionen erkannt und aktiviert. Anschließend
können sie gemountet werden:

.. code-block:: bash

    mount /dev/cryptVG/root /media/root
    mount /dev/sda1 /media/root/boot
    mount --bind /dev /media/root/dev
    mount --bind /proc /media/root/proc
    mount --bind /sys /media/root/sys

Nun kann man den Root-Pfad des laufendes Systems auf die gemountete
Festplatten-Partition umstellen:

.. code-block:: bash

    chroot /media/root                  # ins Filesystem der Festplatte wechseln..

Liegt der Fehler an einer fehlerhaften Einstellung des Bootloaders ``grub``, so
kann das Problem mit folgender Routine automatisch behoben werden:

.. code-block:: bash

    grub-install --recheck /dev/sda     # neues Einrichten des GRUB
    update-grub                         # Partitionen werden erkannt
    grub-mkconfig > /boot/grub/menu.lst # Bootmenü wird neu geschrieben


Nach einem Reboot sollte der PC wie gewohnt hochfahren. Das Verfahren, mittels
der obigen ``chroot``-Routine von einem Live-System aus auf das installierte
System zu wechseln, kann übrigens auch auf nicht verschlüsselte Systeme
angewendet werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#] Eine Verschlüsselung des Betriebsystems mach wohl nur dannn wirklich
    Sinn, wenn ein Angriff mit physischem Zugang zum jeweiligen Rechner zu
    befürchten ist. Ist ein mit dieser Methode verschlüsselter Rechner
    ausgeschaltet, so ist er wohl bestmöglich geschützt. Erlangt ein Angreifer
    allerdings im laufenden Betrieb Administrator-Rechte, beispielsweise durch
    mögliche Sicherheitslücken bei Server-Anwendungen, so hilft auch die (im
    laufenden Zustand bereits geöffnete) System-Verschlüsselung nicht weiter.

    Persönlich nutze ich daher lieber die bereits beschriebene Methode der
    :ref:`Partitions-Verschlüsselung <Die Partitions-Verschlüsselung>`
    und/oder sichere private Daten auf Offline-Speichermedien; auch ist das
    Programm ``keepassx`` zur geschützten Verwaltung von Passwörtern sehr zu
    empfehlen. Die obige Methode zeigt allerdings einmal mehr, was für "Tricks"
    auf Linux-Systemen grundsätzlich möglich sind..


