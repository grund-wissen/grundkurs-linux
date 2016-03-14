.. index:: mutt
.. _Mutt:

Email-Verwaltung mit Mutt
=========================

Mutt ist ein textbasierter Email-Client, der sich durch eine hohe
Funktionalität und Konfigurierbarkeit auzeichnet. Er wird komplett
über die Tastatur gesteuert.


.. index:: fetchmail, procmail, msmtp, lynx
.. _Installation von Mutt und Hilfsprogrammen:

Installation von Mutt und Hilfsprogrammen
-----------------------------------------

Zur Installation von ``mutt`` sollten folgende Pakete installiert werden:

.. code-block:: bash

    sudo aptitude install fetchmail procmail mutt lynx msmtp

Das Hilfsprogramm ``fetchmail`` holt Emails von einem Email-Provider ab, das
Programm ``procmail`` leitet sie (gegebenenfalls mit selbst definierten
Spam-Filtern) an eine oder mehrere Mailboxen weiter. Mit ``mutt`` werden die
Emails und Mailboxen verwaltet, ``lynx`` dient zum Betrachten von HTML-Emails
und ``msmtp`` als Hilfsprogramm zum Verschicken eigener Emails.

Vor dem ersten Start sollte zunächst im Home-Verzeichnis ``~`` ein ``Mail``- und
ein ``.tmp``-Ordner für Mailboxen und temporäre Dateien angelegt werden:

.. code-block:: bash

    mkdir ~/Mail ~/.tmp


.. rubric:: Anpassen der Konfigurationsdateien

Anschließend sollten die Konfigurationsdateien der einzelnen Programme angelegt
und mit grundlegenden Inhalten gefüllt werden:

* In der Datei ``~/.fetchmailrc`` werden die zum Abholen der Emails nötigen
  Informationen abgelegt:

  .. code-block:: bash

      # Datei .fetchmailrc

      poll EMAIL-HOST protocol pop3 user "EMAIL@ADRESSE.DE" password "GEHEIM" ssl

  Der Email-Host ist beispielsweise ``pop.gmx.net``. Als Protokoll kann anstelle
  von ``pop3`` auch ``imap`` verwendet werden (mit passendem Host,
  beispielsweise ``imap.gmx.net``). In jeder Zeile der Konfigurationsdatei kann
  ein neuer Eintrag stehen, so dass ein zentrales Abholen der Emails von
  mehreren Konten leicht möglich ist.

  Da in der Datei ``.fetchmailrc`` das Email-Passwort im Klartext enthalten ist,
  darf die Datei nur Lese- und Schreibrechte für den Eigentümer haben. Dazu gibt
  man folgendes ein:

  .. code-block:: bash

      chown 600 ~/.fetchmailrc

  Ebenso ist es möglich, die Datei auf einer verschlüsselten Partition oder
  einem verschlüsselten USB-Stick abzulegen und im Home-Verzeichnis einen
  Symlink dorthin zu erstellen.

* In der Datei ``~/.msmtprc`` werden die zum Versenden der Emails nötigen
  Informationen angegeben:

  .. code-block:: bash

      # Datei .msmtprc

      defaults
      auth             on
      tls              on

      account default
      host EMAIL-HOST
      port 587
      from EMAIL@ADRESSE.de
      user EMAIL@ADRESSE.de
      password GEHEIM
      tls_trust_file /etc/ssl/certs/ca-certificates.crt
      auth login

  Der Email-Host ist beispielsweise ``mail.gmx.net``. Inzwischen verlangen viele
  Email-Provider eine SSL- oder TLS-Verschlüsselung für die Verbindung
  zwischen dem Host und dem Client; dies wird durch die obigen Konfigurationen
  als Standard festgelegt, wobei der genutzte Port bei verschiedenen Providern
  unterschiedlich sein kann (Infos hierzu sollten von jedem Provider angegeben
  sein). Für verschiedene Email-Konten können wiederum verschiedene
  Benutzer-Accounts angelegt werden.

  Auch in dieser Datei ist das Passwort im Klartext (allerdings ohne
  Anführungszeichen) enthalten. Auch diese Datei darf somit nur Lese- und
  Schreibrechte für den Eigentümer haben:

  .. code-block:: bash

      chown 600 ~/.msmtprc

* In der Datei ``~/.procmailrc`` sind die zum Verteilen ("processing") der
  Emails nötigen Informationen gespeichert:

  .. code-block:: bash

      # Datei .procmailrc

      MAILDIR=$HOME/Mail/
      LOGFILE=$HOME/.procmaillog
      LOGABSTRACT=no
      VERBOSE=off
      FORMAIL=/usr/bin/formail
      NL=''

      # Doppelt gesendete Mails mittels formail abfangen
      :0 Whc: .msgid.  lock
      | $FORMAIL -D 16384 .msgid.cache
      :0 a
      $MAILDIR/duplicates


      # Spam nach Absender aussortieren
      :0
      * ^Sender:.*(video|price|addme)
      $MAILDIR/spam

      #Spam nach Betreff aussortieren
      :0
      * ^Subject:.*(credit|cheap|cash|money|debt|sale|loan)
      $MAILDIR/spam


      # Alle anderen Emails in die default-Mailbox ablegen:
      :0
      * .*
      default

  Durch ``:0`` wird jeweils eine Filterregel eingeleitet. Anschliessend wird die
  eingehende Email auf ein Muster geprüft; beispielsweise würde ``* ^From:
  .*Max Mustermann`` bedeuten, dass für alle Emails mit "Max Mustermann" im
  Absender die darauf folgende Aktions-Zeile ausgeführt wird. [#]_

..  http://www.gentoo.org/doc/de/guide-to-mutt.xml

* In der Datei ``~/.muttrc`` wird das Verhalten von Mutt über eine Vielzahl
  möglicher Konfigurationen festgelegt. Dabei können Pfade, Tastenbelegungen,
  Farben, Verschlüsselungs-Einstellungen usw. angepasst werden. Die Datei
  kann beispielsweise so aussehen:

  .. only:: html

      .. code-block:: bash

          # Datei .muttrc

          # ---------------------------------------------------------------------------------------
          # PFADEINSTELLUNGEN
          # ---------------------------------------------------------------------------------------

          # Pfad für Adressbuch-Datei festlegen:
          set alias_file=     "~/.mutt/addressbook"
          source              "~/.mutt/addressbook"

          # Standard-Mailbox für eingehende Emails:
          set spoolfile='+default'

          # Gelesene Emails nach "inbox-JAHR" im Mail-Ordner verschieben
          # (beispielsweise "inbox-2014" für Emails aus dem Jahr 2014)
          set mbox="+inbox-`date +%Y`"

          # Gesendete Emails nach "sent-JAHR" im Mail-Ordner verschieben
          set record="+sent-`date +%Y`"

          # Email-Entwürfe in der Mailbox "Entwuerfe" speichern:
          set postponed="+Entwuerfe"

          # Pfad für temporäre Dateien festlegen:
          set tmpdir=~/.tmp

          # ---------------------------------------------------------------------------------------
          # TASTENKOMBINATIONEN
          # ---------------------------------------------------------------------------------------

          # Mails durch Drücken von "A" vom Provider abholen und dort löschen:
          macro index,pager A "!fetchmail -m 'procmail -d %T'\r"

          # Alternativ: Mails durch Drücken von "A" vom Provider abholen und dort belassen (keep and verbose):
          # #macro index,pager A "!fetchmail -kv -m 'procmail -d %T'\r"

          bind browser <Enter> view-file

          # HTML-Mails durch Drücken von "l" mit lynx betrachten:
          macro pager,attach l "<pipe-entry>lynx -stdin -force_html<enter>"

          # Emails durch Drücken von "f" weiterleiten
          bind index,pager f forward-message

          # An alle Empfänger einer Email antworten
          bind index,pager R group-reply


          # ---------------------------------------------------------------------------------------
          # ALLGEMEINE EINSTELLUNGEN
          # ---------------------------------------------------------------------------------------

          # Alle Header-Infos grundsätzlich ausblenden:
          ignore *

          # Folgende Header-Infos jedoch erlauben:
          unignore	from: subject to cc mail-followup-to \
              date x-mailer x-url list-id

          # Format für das Zitieren der Original-Mail in einer Antwort-Email
          # ("Am DATUM schrieb ABSENDER:")
          set attribution="* %n <%a> [%(%d.%m.%Y %H:%M)]:"

          set nobeep                # Keine akustischen Signale bei neuen Nachrichten
          set copy=yes              # Gesendete Emails immer speichern
          set delete=yes            # Als gelöscht markierte Emails beim Beenden löschen (ohne Nachfrage)
          set editor='vim'          # Oder ein anderer Editor, beispielsweise 'gedit'
          set fast_reply            # Beim Antworten auf eine Email sofort den Editor öffnen
          set followup_to           # In Betreff und Email-Header "Follow up"-Markierungen setzen
          set help=no               # Hilfe-Zeilen ausblenden
          set include=ask-yes       # Nachfragen, ob Original-Mail in Antwort zitiert werden soll

          set move=yes              # Gelesene Nachrichten in die obige mbox verschieben
          set nosave_empty          # Keine leeren Email-Entwürfe speichern
          set pager_index_lines=6   # Beim Lesen von Emails 6 Zeilen für Pager reservieren
          set pager_stop            # Beim Lesen von Emails nicht in die nächste Email scrollen
          set read_inc=25           # Fortschritts-Anzeige beim Lesen von Mailboxen einblenden
          set reply_to              # Antwort-Emails automatisch erkennen

          set reply_regexp="^((re([\[^-][0-9]+\]?)*|Re|aw|antwort|antw|wg):[ \t]*)+"

          set reverse_alias         # Namen von Email-Absendern anhand Adress-Liste anzeigen

          set send_charset="us-ascii:iso-8859-1:iso-8859-15:iso-8859-2:utf-8"

          set smart_wrap            # Besserer Zeilenumbruch
          set sort=threads          # Emails nach in Thread-Reihenfolge anzeigen
          set sort_aux=date-sent    # Emails innerhalb von Threads nach dem Datum sortieren
          set strict_threads        # Bei Threading auf In-Reply-To-Header achten, nicht auf Betreff
          set weed=yes              # Standard.. :)
          set wrap_search=yes       # Im Index-Modus Suche erneut von vorne zulassen

          auto_view text/html


          # ---------------------------------------------------------------------------------------
          # PERSOENLICHE EINSTELLUNGEN
          # ---------------------------------------------------------------------------------------

          my_hdr From:        "VORNAME NACHNAME" <EMAIL@ADRESSE.de>
          my_hdr Reply-To:    "VORNAME NACHNAME" <EMAIL@ADRESSE.de>
          set realname=       "VORNAME NACHNAME"
          set signature=      "+.signature"

          # Einstellungen für den Standard-Ordner:
          folder-hook . "set from='VORNAME NACHNAME  <EMAIL@ADRESSE.de>'"
          folder-hook . "set index_format='%4C %Z %{%b %d} %-15.15L (%4l) %s'"
          folder-hook . "set sendmail='/usr/bin/msmtp --account=default'"


          # ---------------------------------------------------------------------------------------
          # FARBEN
          # ---------------------------------------------------------------------------------------

          # Aussehen von Mutt:

          color     tree            brightmagenta     default
          color     attachment      magenta           default
          color     error           red               default
          color     header          brightyellow      default   "^Subject: "
          color     header          white             default   "^To:"
          color     hdrdefault      yellow            default
          color     indicator       black             white
          color     markers         brightblue        default
          color     message         white             default
          color     normal          white             default
          color     quoted          yellow            default
          color     quoted1         green             default
          color     quoted2         cyan              default
          color     quoted3         red               default
          color     signature       brightblack       default
          color     status          brightyellow      blue
          color     search          default           green

          # Highlighting von Emails (abhängig von der "Punktezahl" einer Email):

          # Mögliche Muster zur Punktevergabe:
          # ~f ABSENDER     : Betrifft alle Emails, die vom ABSENDER geschickt wurden ("from")
          # ~t EMPFAENGER   : Betrifft alle Emails, die an EMPFAENGER geschickt wurden ("to")
          # ~s BETREFF      : Betrifft alle Emails, die BETREFF in der Betreff-Zeile enthalten ("subject")

          # Reguläre Ausdrücke als Suchmuster:
          # .       : Ein beliebiges Zeichen
          # *       : Der vorherige Ausdruck Null mal oder beliebig oft
          # [aA]    : Eines der in der Klammer enthaltenen Zeichen (a oder A)


          # Alle Emails bekommen zunächst 0 Punkte:
          unscore *

          # Beispiel 1: 10 Punkte an alle Emails vergeben, die "grund-wissen" im Empfänger-Namen enthalten:
          score '~t .*@grund-wissen.*' +10

          # Beispiel 2: 25 Punkte an alle Emails vergeben, die "sphinx" in der Betreff-Zeile enthalten:
          score '~s .*sphinx.*'      +25


          # Zum Beispiel 1: Alle Emails mit einer Punktezahl von 10-20 hellrot hervorheben:
          color index brightred default '~n 10-20'

          # Zum Beispiel 2: Alle Emails mit einer Punktezahl von 25-29 blau hervorheben:
          color index blue default      '~n 25-29'

  .. only:: latex

      .. code-block:: bash

          # Datei .muttrc

          # --------------------------------------------------------------------
          # PFADEINSTELLUNGEN
          # --------------------------------------------------------------------

          # Pfad für Adressbuch-Datei festlegen:
          set alias_file=     "~/.mutt/addressbook"
          source              "~/.mutt/addressbook"

          # Standard-Mailbox für eingehende Emails:
          set spoolfile='+default'

          # Gelesene Emails nach "inbox-JAHR" im Mail-Ordner verschieben
          # (beispielsweise "inbox-2014" für Emails aus dem Jahr 2014)
          set mbox="+inbox-`date +%Y`"

          # Gesendete Emails nach "sent-JAHR" im Mail-Ordner verschieben
          set record="+sent-`date +%Y`"

          # Email-Entwürfe in der Mailbox "Entwuerfe" speichern:
          set postponed="+Entwuerfe"

          # Pfad für temporäre Dateien festlegen:
          set tmpdir=~/.tmp

          # --------------------------------------------------------------------
          # TASTENKOMBINATIONEN
          # --------------------------------------------------------------------

          # Mails durch Drücken von "A" vom Provider abholen und dort löschen:
          macro index,pager A "!fetchmail -m 'procmail -d %T'\r"

          # Alternativ: Mails durch Drücken von "A" vom Provider abholen und
          # dort belassen (keep and verbose):
          # #macro index,pager A "!fetchmail -kv -m 'procmail -d %T'\r"

          bind browser <Enter> view-file

          # HTML-Mails durch Drücken von "l" mit lynx betrachten:
          macro pager,attach l "<pipe-entry>lynx -stdin -force_html<enter>"

          # Emails durch Drücken von "f" weiterleiten
          bind index,pager f forward-message

          # An alle Empfänger einer Email antworten
          bind index,pager R group-reply


          # --------------------------------------------------------------------
          # ALLGEMEINE EINSTELLUNGEN
          # --------------------------------------------------------------------

          # Alle Header-Infos grundsätzlich ausblenden:
          ignore *

          # Folgende Header-Infos jedoch erlauben:
          unignore	from: subject to cc mail-followup-to \
              date x-mailer x-url list-id

          # Format für das Zitieren der Original-Mail in einer Antwort-Email
          # ("Am DATUM schrieb ABSENDER:")
          set attribution="* %n <%a> [%(%d.%m.%Y %H:%M)]:"

          set nobeep                # Keine akustischen Signale bei neuen
                                    # Nachrichten
          set copy=yes              # Gesendete Emails immer speichern
          set delete=yes            # Als gelöscht markierte Emails beim Beenden
                                    # löschen (ohne Nachfrage)
          set editor='vim'          # Oder ein anderer Edigor, z.B. 'gedit'
          set fast_reply            # Beim Antworten auf eine Email sofort den
                                    # Editor öffnen
          set followup_to           # In Betreff und Email-Header "Follow up"-
                                    # Markierungen setzen
          set help=no               # Hilfe-Zeilen ausblenden
          set include=ask-yes       # Nachfragen, ob Original-Mail in Antwort
                                    # zitiert werden soll

          set move=yes              # Gelesene Nachrichten in die obige mbox
                                    # verschieben
          set nosave_empty          # Keine leeren Email-Entwürfe speichern
          set pager_index_lines=6   # Beim Lesen von Emails 6 Zeilen für Pager
                                    # reservieren
          set pager_stop            # Beim Lesen von Emails nicht in die nächste
                                    # Email scrollen
          set read_inc=25           # Fortschritts-Anzeige beim Lesen von
                                    # Mailboxen einblenden
          set reply_to              # Antwort-Emails automatisch erkennen

          set reply_regexp="^((re([\[^-][0-9]+\]?)*|Re|aw|antwort|antw|wg):[ \t]*)+"

          set reverse_alias         # Namen von Email-Absendern anhand
                                    # Adress-Liste anzeigen

          set send_charset="us-ascii:iso-8859-1:iso-8859-15:iso-8859-2:utf-8"

          set smart_wrap            # Besserer Zeilenumbruch
          set sort=threads          # Emails nach in Thread-Reihenfolge anzeigen
          set sort_aux=date-sent    # Emails innerhalb von Threads nach dem Datum
                                    # sortieren
          set strict_threads        # Bei Threading auf In-Reply-To-Header achten,
                                    # nicht auf Betreff
          set weed=yes              # Standard.. :)
          set wrap_search=yes       # Im Index-Modus Suche erneut von vorne
                                    # zulassen

          auto_view text/html


          # --------------------------------------------------------------------
          # PERSOENLICHE EINSTELLUNGEN
          # --------------------------------------------------------------------

          my_hdr From:        "VORNAME NACHNAME" <EMAIL@ADRESSE.de>
          my_hdr Reply-To:    "VORNAME NACHNAME" <EMAIL@ADRESSE.de>
          set realname=       "VORNAME NACHNAME"
          set signature=      "+.signature"

          # Einstellungen für den Standard-Ordner:
          folder-hook . "set from='VORNAME NACHNAME  <EMAIL@ADRESSE.de>'"
          folder-hook . "set index_format='%4C %Z %{%b %d} %-15.15L (%4l) %s'"
          folder-hook . "set sendmail='/usr/bin/msmtp --account=default'"


          # --------------------------------------------------------------------
          # FARBEN
          # --------------------------------------------------------------------

          # Aussehen von Mutt:

          color     tree            brightmagenta     default
          color     attachment      magenta           default
          color     error           red               default
          color     header          brightyellow      default   "^Subject: "
          color     header          white             default   "^To:"
          color     hdrdefault      yellow            default
          color     indicator       black             white
          color     markers         brightblue        default
          color     message         white             default
          color     normal          white             default
          color     quoted          yellow            default
          color     quoted1         green             default
          color     quoted2         cyan              default
          color     quoted3         red               default
          color     signature       brightblack       default
          color     status          brightyellow      blue
          color     search          default	        green

          # Highlighting von Emails (abhängig von der "Punktezahl" einer Email):

          # Mögliche Muster zur Punktevergabe:
          # ~f ABSENDER     : Betrifft alle Emails, die vom ABSENDER
          #                   geschickt wurden ("from")
          # ~t EMPFAENGER   : Betrifft alle Emails, die an EMPFAENGER
          #                   geschickt wurden ("to")
          # ~s BETREFF      : Betrifft alle Emails, die BETREFF
          #                   </EMAIL@ADRESSE>in der Betreff-Zeile enthalten
          #                   ("subject")

          # Reguläre Ausdrücke als Suchmuster:
          # .       : Ein beliebiges Zeichen
          # *       : Der vorherige Ausdruck Null mal oder beliebig oft
          # [aA]    : Eines der in der Klammer enthaltenen Zeichen (a oder A)


          # Alle Emails bekommen zunächst 0 Punkte:
          unscore *

          # Beispiel 1: 10 Punkte an alle Emails vergeben, die "grund-wissen"
          # im Empfänger-Namen enthalten:
          score '~t .*@grund-wissen.*' +10

          # Beispiel 2: 25 Punkte an alle Emails vergeben, die "sphinx"
          # in der Betreff-Zeile enthalten:
          score '~s .*sphinx.*'      +25


          # Zum Beispiel 1: Alle Emails mit einer Punktezahl von 10-20
          # hellrot hervorheben:
          color index brightred default '~n 10-20'

          # Zum Beispiel 2: Alle Emails mit einer Punktezahl von 25-29
          # blau hervorheben:
          color index blue default      '~n 25-29'

In der obigen Beispiel-Konfigurationsdatei sollten die in Großbuchstaben
gesetzten Variablen durch eigene Angaben ersetzt werden; zudem sollte der
zum Schreiben von Emails bevorzugte Editor festgelegt werden.

Damit die Mailboxen im Verzeichnis ``~/Mail`` automatisch erkannt werden, sollte
zudem folgender Eintrag zu den Pfadeinstellungen hinzugefügt werden:

.. code-block:: bash

    # Mailboxen automatisch finden:
    mailboxes $(find ~/Mail/ -maxdepth 0 -type d -printf "%p)

Dieser Eintrag befindet sich bei mir genau so in meiner eigenen ``~/.muttrc``;
leider wird jedoch in der Druckversion durch diese Zeile das Highlighting der
gesamten Konfigurationsdatei deaktiviert.. anscheinend ein Fehler von Pygments,
dem ansonsten echt prima funktionierenden Syntax-Highlighting-Tool.

Durch eine Vergabe von Punkten auf bestimmte Muster im Absenderfeld oder in der
Betreffzeile von Emails ist es möglich, Emails von einzelnen Personen,
Unternehmen oder Mailinglisten gezielt farblich hervorzuheben. Als Farben sind
``red``, ``green``, ``blue``, ``yellow``, ``cyan``, ``magenta`` möglich, wobei
durch die Nachrichten bei einem davor gestellten ``bright`` zusätzlich fett
gedruckt erscheinen (beispielsweise steht ``brightgreen`` für grün und
fettgedruckt).

Das Prinzip der Punktevergabe ist eigentlich simpel, man sollte lediglich darauf
achten, dass die einkommenden Emails nicht mehrfach Punkte erhalten,
beispielsweise weil sie das Wort "Python" sowohl in der Emailadresse wie auch in
der Betreffzeile enthalten. Sollten beide Muster beispielsweise mit 5 Punkten
gewertet werden, so bekäme die Email insgesamt 10 Punkte und könnte dadurch
gegebenenfalls eine andere Farbe bekommen..


.. mailcap-path?
.. weed-option?

..  Achtung bei möglicher mehrfacher Vergabe von Punkten!

.. _Bedienung von Mutt:

Bedienung von Mutt
------------------

Startet man Mutt (durch Eingabe von ``mutt`` in einer Shell), so werden bei
Verwendung der obigen Einstellungen die Emails der ``~/Mail/default``-Mailbox
aufgelistet. Dieser Ansichtsmodus von Mutt wird "Index" genannt. Wird Mutt zum
ersten Mal gestartet, ist die Index-Ansicht normalerweise leer.

.. rubric:: Index-Modus

Im Index-Modus können folgende Funktionen durch Drücken der jeweiligen Taste
aufgerufen werden:

* Email abrufen und zwischen Emails navigieren:

  .. list-table::
      :name: tab-index-navigation
      :widths: 50 50

      * - ``A``
        - Emails vom Provider abrufen
      * - ``a``
        - Absender der Email unter dem Cursor ins Adressbuch aufnehmen
      * - ``?``
        - Hilfe einblenden
      * - :math:`\downarrow` oder ``j``
        - Zur nächsten Email gehen
      * - :math:`\uparrow` oder ``k``
        - Zur vorherigen Email gehen
      * - ``HOME``
        - Zur ersten Email gehen
      * - ``END``
        - Zur letzten Email gehen
      * - ``q``
        - Mutt beenden ("quit")

  Zudem kann man mit ``PageUP`` und ``PageDown`` die Emails seitenweise
  durchblättern.

* Emails schreiben, beantworten und weiterleiten:

  .. list-table::
      :name: tab-index-mail
      :widths: 15 50

      * - ``m``
        - Neue Email verfassen ("mail")
      * - ``r``
        - Auf Email unter dem Cursor antworten (nur dem Absender) ("reply")
      * - ``R``
        - Auf Email unter dem Cursor antworten (allen Empfängern) ("group reply")
      * - ``f``
        - Email unter dem Cursor weiterleiten ("forward")

  Zum Schreiben der Emails wird automatisch der in der Konfigurationsdatei
  festgelegte Editor geöffnet. Speichert man dort die verfasste Email und
  beendet den Editor, kehrt man automatisch zu Mutt zurück.

* Emails markieren, löschen, verschieben, kopieren:

  .. only:: html

      .. list-table::
          :name: tab-index-move
          :widths: 15 50

          * - ``d``
            - Email unter dem Cursor löschen ("delete")
          * - ``u``
            - Löschmarkierung unterhalb des Cursor aufheben  ("undelete")
          * - ``t``
            - Email unter dem Cursor mit einer Markierung versehen ("tag")
          * - ``D``
            - Emails nach bestimmtem Muster löschen ("delete by pattern")
          * - ``U``
            - Löschmarkierungen nach bestimmtem Muster aufheben  ("undelete by pattern")
          * - ``T``
            - Emails nach bestimmtem Muster mit einer Markierung versehen ("tag by pattern")
          * - ``w``
            - | Status der Email-Adresse anpassen
              | (``O``: Old, ``N``: New, ``D``: Delete, ``r``: Responded , ``*``: Tagged, ``!`` : Important)
          * - ``C``
            -  Email unter dem Cursor in eine andere Mailbox kopieren ("copy")
          * - ``s``
            -  Email unter dem Cursor in andere Mailbox abspeichern/verschieben ("save")

  .. only:: latex

      .. list-table::
          :name: tab-index-move-latex
          :widths: 15 50

          * - ``d``
            - Email unter dem Cursor löschen ("delete")
          * - ``u``
            - Löschmarkierung unterhalb des Cursor aufheben  ("undelete")
          * - ``t``
            - Email unter dem Cursor mit einer Markierung versehen ("tag")
          * - ``D``
            - Emails nach bestimmtem Muster löschen ("delete by pattern")
          * - ``U``
            - Löschmarkierungen nach bestimmtem Muster aufheben  ("undelete by pattern")
          * - ``T``
            - Emails nach bestimmtem Muster mit einer Markierung versehen ("tag by pattern")
          * - ``w``
            - Status der Email-Adresse anpassen
              (``O``: Old, ``N``: New, ``D``: Delete, ``r``: Responded , ``*``: Tagged, ``!`` : Important)
          * - ``C``
            -  Email unter dem Cursor in eine andere Mailbox kopieren ("copy")
          * - ``s``
            -  Email unter dem Cursor in andere Mailbox abspeichern/verschieben ("save")

  Ist die Option ``set move=yes`` in der Konfigurationsdatei aktiviert, werden
  gelesene Emails automatisch beim Beenden von Mutt von der ``default``-Mailbox
  in die ``mbox``-Mailbox (bei obigen Einstellungen: ``inbox-2014``) verschoben.
  Möchte man eine Email jedoch noch in der (meist deutlich kleineren) Mailbox
  ``default`` behalten, so kann man sie mittels ``w o`` wieder als ungelesen
  markieren.

  Um mehrere Emails auf einmal in eine andere Mailbox zu verschieben, markiert
  man mittels ``t`` zunächst die einzelnen Emails. Anschließend kann man
  mittels Eingabe von ``;`` den darauf folgenden Befehl auf alle markierten
  Emails anwenden; beispielsweise können durch ``;s`` alle markierten Emails in
  eine auszuwählende Mailbox verschoben werden.

..  http://dev.mutt.org/doc/manual.html#tags

* Emails durchsuchen:

  .. list-table::
      :name: tab-index-search
      :widths: 15 50

      * - ``/``
        - Nach Emails suchen
      * - ``n``
        - Zur nächsten Email gehen, auf welche die Suche zutrifft
      * - ``N``
        - Rückwärts zur nächsten Email gehen, auf welche die Suche zutrifft

  Bei der Suche mittels ``/`` werden die Email-Header, also insbesondere das
  Absenderfeld und die Betreffszeile durchsucht. Möchte man auch den Inhalt der
  Mails durchsuchen, kann man ``/ ~b Suchbegriff`` eingeben ("search bodies").

* Mit ``c`` kann man zwischen verschiedenen Mailboxen wechseln.

Bei mehreren der obigen Funktionen wird vom Benutzer eine weitere Eingabe von
Text in der Eingabezeile (unten am Bildschirm) erwartet. Um diesen
"Eingabe-Modus" abzubrechen und wieder zum normalen Index zurückzukehren, muss
man (etwas gewöhnungsbedürftig) ``Ctrl g`` drücken.


..  http://heather.cs.ucdavis.edu/~matloff/Mutt/NotesMutt.NM.html

..  In the search command, you have various choices concerning WHAT is to be searched. For example

..  / xyz

..  will search for "xyz" in the message headlines, while

..  / ~b xyz

..  will search for that string in the message bodies


.. _Pager-Modus:

.. rubric:: Pager-Modus

Drückt man im Index-Modus ``Leertaste`` oder ``Enter``, so wird der Inhalt der Email
im so genannten Pager-Fenster angezeigt. In diesem kann man mit den Pfeiltasten
oder ``PageUp`` und ``PageDown`` durch den Inhalt der Email scrollen. Durch
Drücken von ``q`` gelangt man zurück in den Index-Modus. Mittels ``r`` kann
man die aktuelle Email unmittelbar beantworten oder mittels ``d`` löschen; Mutt
zeigt dann automatisch die nächste Email im Pager an.

Anhänge von Emails können im Pager-Modus mittels ``v`` angezeigt werden. Mit den
Cursor-Tasten kann dann ein Anhang ausgewählt und mittels ``s`` gespeichert
werden. Mutt speichert den Anhang dabei in dem Verzeichnis, aus dem heraus Mutt
aufgerufen wurde; es kann allerdings auch manuell ein anderer Pfad angegeben
werden.

Der in Mutt integrierte Pager unterstützt von sich aus keine HTML-Emails. Man
kann sich jedoch leicht behelfen, indem man ``lynx`` als Pager für HTML-Emails
nutzt. Bei den obigen Einstellungen kann die aktuelle Email vom Pager aus mit
``lynx`` durch Drücken von ``l`` betrachtet werden. Dabei kann ``PageUp`` und
``PageDown`` für ein seitenweises Durchblättern der Email, oder ``Ctrl p`` und
``Ctrl n`` für ein zeilenweises Scrollen verwendet werden. Mit ``Q`` oder ``q``
wird ``lynx`` wieder beendet. [#]_ Als Alternative dazu kann eine HTML-Email
auch wie ein Anhang gespeichert und mit Firefox oder einem anderen Webbrowser
geöffnet werden.

.. _Compose-Modus:

.. rubric:: Compose-Modus

Hat man mit dem Editor eine Email verfasst und den Editor wieder beendet, so
gelangt man in das so genannte "Compose"-Fenster. Hier können folgende
Funktionen durch Drücken der jeweiligen Taste aufgerufen werden:

.. list-table::
    :name: tab-mutt-compose
    :widths: 50 50

    * - ``s``
      - Text in Betreffszeile ändern ("subject")
    * - ``Esc f``
      - Text im Absender-Feld ändern ("from")
    * - ``c``
      - Weitere für alle sichtbare Empfänger hinzufügen ("copy")
    * - ``b``
      - Versteckte Empfänger hinzufügen ("blind copy")
    * - ``p``
      - PGP-Verschlüsselungs-Einstellungen vornehmen
    * - ``a``
      - Anhänge an die Email hinzufügen ("append")
    * - :math:`\downarrow` oder ``j``
      - Zum nächsten Anhang gehen
    * - :math:`\uparrow` oder ``k``
      - Zum vorherigen Anhang gehen
    * - ``Enter``
      - Emailtext beziehungsweise Anhang im Pager betrachten
    * - ``e``
      - Emailtext beziehungsweise Anhang mit Editor öffnen ("edit")
    * - ``D``
      - Als Anhang vorgesehene Datei wieder löschen ("delete")
    * - ``y``
      - Email versenden

Durch Drücken der ``Tab``-Taste werden eingegebene Email-Adressen jeweils anhand
des Adressbuchs vervollständigt, mittels ``Ctrl g`` kann die Eingabe abgebrochen
werden.

..  durch Drücken von ``a`` Anhänge an die Email hinzugefügt werden oder durch
..  Drücken von ``p`` PGP-Verschlüsselungs-Einstellungen vorgenommen werden.

..  Auch zu diesem Zeitpunkt kann noch mittels ``s`` die Betreffszeile ("subject")
..  und mittels ``Esc f`` das Absender-Feld ("from") angepasst werden. Mittels ``c``
..  können weitere für alle sichtbare Empfänger ("copy") oder mit ``b``
..  versteckte Empfänger ("blind copy") angegeben werden. Durch Drücken der
..  ``Tab``-Taste werden eingegebene Email-Adressen jeweils anhand des Adressbuchs
..  vervollständigt, mittels ``Ctrl g`` kann die Eingabe abgebrochen werden.

..  Die Email sowie die Anhänge können durch Drücken von Enter ``Enter`` im Pager
..  betrachtet oder mittels ``e`` editiert werden. Als Anhänge vorgesehene Dateien
..  lassen sich mittels ``D`` wieder löschen.



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Eine ausführliche Beschreibung von Filterregeln findet sich beispielsweise
    auf der Seite http://www.trash.net/wissen/e-mail-2/procmail-howto/

.. [#] Mag man Text aus einer HTML-Email in der Antwort-Email zitieren, so muss
    dieser von Hand in die Zwischenablage kopiert und in die Antwort-Email
    eingefügt werden. Meist werden Emails allerdings in reiner Textform oder in
    gemischter Text- und HTML-Form verschickt; bei diesen Emails funktioniert
    das automatische Zitieren der Original-Email in der Antwort problemlos.

..  Das Flag ``a`` bedeutet, dass zusätzlich die Aktionszeilen der vorherigen Regel
..  erfolgreich abgeschlossen worden sein muss.


