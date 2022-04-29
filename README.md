# SaveBread

Projekt zur Optimierung der Backwarenproduktion der Genuss Bäckerei

## Auftraggeber

Genuss-Bäckerei


## Auftragnehmer

Team „Der harte SaveBreadkern“

- Projektteam: Renato Fonseca, Lena Kleinschmidt, Stephanie Pleyer, Bernd Saurugger, Andreas Wimmer, Oiver Zeilerbauer


## Ausgangssituation und Projektkontext

In einer durchschnittlichen mittelständischen Bäckerei (ungefähr 40 Filialen) landen täglich 700 Brote, 1.500 Süßwaren und rund 10.000 Semmeln im Container. Was am Vortag nicht mehr verkauft wurde, kommt am nächsten Tag weg - obwohl die Brote und Backwaren einwandfrei sind. Das massenhafte Wegwerfen von Lebensmitteln ist in der Branche nichts Besonderes. Eine Retourenquote von 15 Prozent gilt als "gesund". Kunden können sich so bis spätabends über eine große Auswahl an Brotsorten und anderen Backwaren freuen. Alles andere wäre unternehmerisch nicht zu verantworten, davon sind viele Bäcker überzeugt. Denn angesichts leerer Regale würden die Kunden zu den Wettbewerbern abwandern, wo sie auch spätabends noch ihr Lieblingsbrot bekommen.

Kein Bäcker schmeißt gerne Brot weg und tatsächlich kooperieren einige Bäckereien mit Lebensmittelrettungsinitiativen wie den "Tafeln" oder "Foodsharing". Große Mengen von Altbrot landen auch im Schweinefutter. Wenngleich es ressourcenschonender ist als Backwaren in den Müll zu entsorgen, so ist es trotzdem keine besonders ökologische Lösung. Zudem haben Bäckereien durch den Stromverbrauch von Backöfen und komplexer Kühlungstechnik den höchsten Energiebedarf aller Handwerksgewerke überhaupt. Dazu kommen unnötig eingesetzte Arbeitszeit und Maschinenstunden. Für Schweinefutter kann seitens der Futtermittelproduzenten genauso gut Roh-Weizen oder Roggen verwendet werden. 

## Strategische Zielsetzung

Die Genuss Bäckerei hat es sich zum Ziel gesetzt sowohl regional, als auch nachhaltig mit ihren Produkten umzugehen. Oft fällt es den Bäckermeistern schwer die Bedarfsmenge an Backwaren für den nächsten Tag zu schätzen. Dieser hängt vom Wetter, dem Wochentag und vielen anderen Faktoren ab. Um konkurenzfähig zu bleiben hat die Genuss Bäckerei ein Softwareentwicklungsteam an Data Science Studenten der FH Kufstein beauftargt für sie eine Software zu planen und zu entwickeln, die die optimale Bedarfsmenge an Backwaren und die dafür benötigten Features bestimmt. Die Software wird agil entwickelt um in dem Prozess optimal auf die aktuellen und künftigen Anforderungen für die Software seitens der Genuss Bäckerei eingehen zu können. Es wird eine proaktive, dynamische und flexible Organisationsstruktur bereitgestellt, mit allen notwendigen Kompetenzen, Ressourcen und Visionen, um diesen Ambitionen zu entsprechen. Die Zusammenstellung des Projektteams ermöglicht ein hohes Maß an Flexibilität, um alle vorhersehbaren oder unvorhergesehenen Herausforderungen, die während des Projekts auftreten können, zu bewältigen.

## Requirements an das System (anhand Sophisten Regeln erstellt)

- Das Savebread System muss die Anmeldedaten der SaveBread Nutzer sowie dessen Status (Administrator, Manager oder normaler Nutzer) speichern
- Jeder SaveBread Nutzer kann nur entweder als Administrator, Manager oder normaler Nutzer gespeichert sein
- Der SaveBread Nutzer muss sein Passwort auf dem Anwendebildschirm der SaveBread Anwendung eingeben
- Hat ein SaveBread Nutzer kein Passwort so muss das SaveBread System dem Nutzer die Möglichkeit geben sich als Administrator, Manager oder normaler Nutzer zu registrieren
- Die Freigabe der Registrierung muss im Falle der Registrierung eines Managers oder Andministrators von einem Administartor erfolgen
- Die Freigabe der Registrierung eines normalen Nutzers sollte das SaveBread System atomatisch abwickeln
- Nach der optimierung der Bedarfsmenge sollte die optimale Bedarfsmenge sowie die Abfallreduktion allen SaveBread Nutzern graphisch dargestellt werden
- Der SaveBread Nutzer sollte in 10 Minuten mit dem SaveBread System vertraut sein
- Das SaveBread System sollte die errechnete optimale Bedarfsmenge speichern
- Das SaveBread System sollte jeden Speichervorgang täglich abschließen 
- Das SaveBread System sollte am Monatsende einen Report mit den ersparten Kosten an alle SaveBread Manager per Email senden
- Die in dem Report ersparten Kosten sollten graphisch dargestellt werden
- Die vom SaveBread generierten Reports und Graphiken sollten für mindestens 5 Jahre gespeichert werden und von den SaveBread Managern jederzeit abrufbar sein
- Das SaveBread System überprüft drurch Abgleich der Nutzerdaten ob der angemeldete Nutzer einen Manager ist. Wenn der angemeldete Nutzer kein Manager ist erlaubt das System die Einsicht nicht
- Das SaveBread System sollte jedem Administrator die Möglichkeit geben alle Eingaben zu sichern und die im SaveBread gespeicherten Daten jederzeit zu überprüfen

## Veränderungen der Requirements die wahrscheinlich eitreten könnten

Folgende Requirements könnten sich ändern:
- Die Nutzerrechte an System 
  - Mehrfachauswahl
  - Neue Kathegorie
- Die Technologie der Übermittlung der Reporte
- Der Inhalt der Reporte 
- Die Technologie der Anmeldung 
- Die Frequenz der Optimierung (zB auf halbtäglich)

## Glossary

| Term  | Bedetung                                                                                                                                                                                                                                                                           | 
|-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SaveBread System** | Name des Produktes zur Optimierung der Backwarenproduktion der Genuss Bäckerei.  |
| **Administrator**     | Administratoren planen, installieren, konfigurieren und pflegen die IT-Infrastruktur. Als Operatoren führen sie die zum laufenden Betrieb der Computeranlagen erforderlichen manuellen Tätigkeiten aus.           |
| **Manager**      | Als Eigentümer tätige Person, die Managementaufgaben in der Organisation wahrnimmt. Ihre wichtigsten Aufgaben sind Planung, Organisation, (Unternehmens-)Führung und Kontrolle..                |
| **normaler Nutzer**     | Sonstige Nutzer des Systems, die keine erweiterten Nutzungsrechte haben (zB Mitarbeiter im Betrieb).           |
| **Registrierung**     | Der Prozess des Anlegens neuer Nutzer.           |
| **Report**     | Der Begriff Report beschreibt den systematisch erstellten  Bericht auf Basis relevanter Unternehmensdaten und Informationen. Wichtigstes Ziel des Reportings ist die Unterstützung der Führungs- und Entscheidungsprozesse in den verschiedenen Unternehmensbereichen.           |
| **Speichervorgang**     | Der Prozess der Sicherung von Daten die zu einem späteren Zeitpunkt wieder abgerufen werden können .           |
| **muss**     | Das Wort muss wird für verplichtende Anforderungen verwendet. Sie sind rechlich  bindend und müssen daher auch umgesetzt werden. Die Abnahme des Produktes kann verweigert werden sollten diese Anforderungen nicht umgesetzt werden.           |
| **sollte**     | Das Wort sollte wird für gewünschte Anforderungen verwendet. Sie sind rechlich weder bindend und müssen daher nicht umgesetzt werden. Sie dienen der Kollaboration zwischen Stakeholdern und den Programmierern (MoU)           |



## Kosten der Produktion

Die Entwicklung der Software wird im Zuge der Lehrveranstaltung Softwareentwicklung 2 der FH Kufstein Tirol durchgeführt. Die Planung ind Entwicklung erfolgt unentgeltlich von teilnehmenden Studenten. Im Gegenzug erklrärt sich die Genuss Bäckerei dazu bereit die Software Open Access zur Verfügung zu stellen.


## Impact und Inhalte

SaveBread trägt maßbehend an die Optimierung der Produktionsmengen von Lebensmitteln bei. Es sorgt sowohl für eine Reduktion der wegeschmissenen Backwaren, als auch zu einer Kostenersparnis beim Wareneinsatz der Genuss Bäckerei. Nicht zuletzt profitiert auch die Öffentlichkeit an dem Projekt. Nachhaltikeit in der Lebensmittelindustrie ist auch ein aktuelles politisches Thema, so trägt das Projekt SaveBread entscheidend an der Umsetzung des Zieles der Vereinten Nationen "Agenda 2030 für nachhaltige Entwicklung" bei, in der es um die Reduktion vermeidbarer Lebensmittelverluste und die Bekämpfung von Hunger und Fehlernährung in der Welt geht.

| Impact  | Messbare Ergebnisse                                                                                                                                                                                                                                                                           | 
|-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Abfallreduktion** | Durch die Implementierung der Software soll es der Genuss Bäckerei ermöglicht werden die Produtionesmengen zu opimieren und somit ihren Anteil an weggeworfenen Lebensmitteln um 80% zu senken.  |
| **Kostenersparnis**     | Durch besagte Optimierung wird auch der Wareneinsatz verbessert, zudem fallen dem Unternehmen signifikant weniger Overheadkosten an.           |
| **Gesamtwirtschaftliche Effekte**      | Durch die Open Access Puplication der Software wird die Öffentlichkeit über Lebensmitteverschwenung aufgeklärt. Des weiteren wird davon ausgegganen dass innerhalb der nächsten 5 Jahre durch das re-usen des Codes eine gesamtwirschaftliche Kostenersparnis von 2Mrd Euro erzielht werden kann.                                                       | 


## Meilensteine
1. Software-Projekte in Data Science Requirements-Engineering (start: 22.04.2022, end: 29.04.2022)
2. Data Science Deployment + Basics of the Web (start: 29.04.2022, end: 06.05.2022)
3. Software Design + Dev-Tipps (start: 06.05.2022, end: 13.05.2022)
4. Architektur (start: 13.05.2022, end: 20.05.2022)
5. Data Science Architektur (start: 20.05.2022, end: 03.06.2022)
6. Outlook + MLOps (start: 03.06.2022, end: 12.07.2022)
7. Die Übernahme der Software erfolgt am 12.07.2022 


## Stakeholder

1. Administratoren der SaveBread Software
2. Manager der Genuss Bäckerei
3. Mitarbeiter der genuss Bäckerei
4. General Public: Especially Data Scientists, Researchers and Citizen Scientists who are re-useing the openly available code


## Risiken

| Risk (P:"Likelyhood", S:"Severity")  | Mitigation                                                                                                                                                                                                                                                                           | 
|-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Verfügbrkeit von relevanten Daten die für die Umsetzung der Software benötigt werden (P:Low, S:High)** | Bei der Wahl der Datenquelle ist die long-term-availability ein maßgebendes Kriterium. So werden zB Wetterdaten direkt von der Zentralanstalt für Meteorologie und Geodynamik (ZAMG) bezogen. Die ZAMG ist der staatliche meteorologische und geophysikalische Dienst Österreichs. Die ZAMG wurde 1851 gegründet und ist damit der älteste staatliche Wetterdienst der Welt. |
| **Die entwickelte Software ist nicht Nutzerfreundlich (P:Medium, S:Low)**     | Es wergen Schulungen und Trainings angeboten um potentielle Nutzer mit den Skills zur richtigen Verwendung der Software anzureichern.           |
| **Die Genussbäckerei geht aufgrund zu hoher Wareneinsatzkösten in Konkurs bevor die rettende Software übergeben werden kann (P:Medium, S:High)**      | Die entwickelte Software kann auch für andere Betriebe adaptiert werden.  |   
| **Die entwickelte Software wird nicht gewartet (P:High, S:High)**     | Die Software wird im Zuge der Lehrveranstaltung Softwareentwicklung 2 ausgerollt. Eine Wartung darüber hinaus ist nicht vorgesehen. Nachdem die Studenten der FH Kufstein unentgeltlich und freiwillig daran arbeiten sind sie auch nicht bereit ein Service Level Agreement (SLA) zu unterfertigen. Somit sind Leistungsumfang, Reaktionszeit und Schnelligkeit der Bearbeitung nicht garantiert.            | 


## Reporting / Projektsitzungen

 - Die Umsetzung des Projekts soll agil erfolgen. Hier sollen die Ergebnisse eines Sprints in die Projektdokumentation aufgenommen werden, die zu Reportingszwecke an Lukas Huber fließen wird. Die Dokumentation erfolgt über [Issues] (https://gitlab.web.fh-kufstein.ac.at/lena.kleinschmidt/savebread/-/issues?sort=created_date&state=opened) und das [Wiki] (https://gitlab.web.fh-kufstein.ac.at/lena.kleinschmidt/savebread/-/wikis/home).
 - Sprints werden über [Issues] (https://gitlab.web.fh-kufstein.ac.at/lena.kleinschmidt/savebread/-/issues?sort=created_date&state=opened) in Gitlab organisiert und gesteuert.
 - Die agilen Projektsitzungen umfassen sowohl das Sprint-Planning zum Sprintanfang, sowie das Backlog Grooming mindestens einmal während des Sprints. Zum Sprintende erfolgen Review mit dem Stakeholder und eine Retrospektive innerhalb des Teams.
