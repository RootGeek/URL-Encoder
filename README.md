Funktionsweise
Zunächst wird eine ASCII Art dargestellt, die am Anfang des Skripts definiert ist.

Die Hauptfunktion url_decoder(url) nimmt eine verkürzte URL als Eingabe und gibt den entschlüsselten Original-Link zurück.

Die Funktion url_decoder verwendet die "requests" Bibliothek, um eine HEAD-Anfrage an die verkürzte URL zu senden. Mit der Option allow_redirects=True wird sichergestellt, dass eventuelle Weiterleitungen automatisch gefolgt werden, um den endgültigen Ziel-Link zu erhalten.

Wenn die Anfrage erfolgreich ist und eine Weiterleitungs-URL vorhanden ist, wird diese URL als entschlüsselte URL zurückgegeben.

Falls es Probleme bei der Verbindung zum Shortener-Dienst gibt (z. B. aufgrund einer fehlerhaften URL oder Netzwerkproblemen), wird eine entsprechende Fehlermeldung zurückgegeben.

Im __name__ == "__main__"-Block wird die Hauptfunktionalität des Skripts aufgerufen. Hier wird ein Beispiel einer verkürzten URL short_url definiert und das Ergebnis der Entschlüsselung ausgegeben.

Verwendung
Speichere den obigen Python-Code in einer Datei mit der Erweiterung ".py", z. B. "url_decoder.py".

Stelle sicher, dass Python 3.x auf deinem System installiert ist.

Installiere die erforderliche Bibliothek "requests", falls sie noch nicht vorhanden ist.

Führe das Skript aus, indem du in der Kommandozeile in das Verzeichnis navigierst, in dem die Datei gespeichert ist, und den folgenden Befehl ausführst:
