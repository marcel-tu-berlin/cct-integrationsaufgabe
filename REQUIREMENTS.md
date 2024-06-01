# Anforderungen

## User Stories

- [ ] Es soll aus mehreren zur Wahl stehenden Personen gewählt werden können.
- [ ] Es soll eine Übersicht über das aktuelle Ergebnis geben
- [ ] Es soll eine Person im System angelegt werden können. Hierbei soll zwischen nicht wählbar und wählbar unterschieden werden.
- [ ] Der Benutzer soll sich vor der Wahl einloggen müssen.

### Optional

- [ ] Es sollen verschiedene Wahlsysteme unterstützt werden (z.B. mehrstufige Wahlsysteme, Präferenzwahl, etc.)

## Technische Anforderungen

- [x] Frontend mit Vue.js 3
- [x] Backend mit Python FastAPI

### Frontend

- [ ] Eine Seite, um eine Person im System anzulegen. Diese Seite muss Eingabemöglichkeiten für alle Daten der Person haben (welche das sind, bleibt dir überlassen). Außerdem solltest du darauf achten, dass jede Person nur einmal angelegt werden kann.
- [ ] Eine Seite zum Auswählen einer Person. Diese Seite sollte alle wählbaren Personen anzeigen und die Möglichkeit bieten, die Wahl nach dem Wahlsystem die Wahl durchzuführen. (Implementiere hier das Wahlsystem, das dir am geeignetsten erscheint). Es kann immer nur eine Wahl gleichzeitig stattfinden.
- [ ] Eine Seite zur Anzeige der aktuellen Wahlergebnisse. Diese Seite soll die Personen mit dem jeweiligen aktuellen Wahlergebnis in % anzeigen.
- [ ] Eine Login-Seite zum Einloggen mit Benutzername und Passwort. Nur eingeloggte Benutzer können wählen. Das Wahlergebnis muss für alle sichtbar sein.

### Backend

- [ ] Ein Endpoint zum Einloggen. (Du musst nichts so kompliziertes wie Oauth2 implementieren).
- [ ] Ein Endpoint für die Personenverwaltung
- [ ] Ein Endpoint für die Wahlen
