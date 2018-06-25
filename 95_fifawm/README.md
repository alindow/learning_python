# FIFA WM 2018

Datenbankbasiertes WM Programm für die Fußball-WM 2018

## SQLite
  1. Connection Python to DB
  2. Create DB Structure
        * Ordner C:\sqlite\db
        * cd c:\sqlite
        * sqlite3 db/pythonsql.db
  3. Load Data
        * Nationen mit IAAF Codes
        * Encoding erstmal ausgeklammert
        * Gruppen geladen
        * Spiele geladen
  4. Show Data
        * Gruppen angezeigt
        * Spiele angezeigt
  5. Fair Play Data
        + gelbe und rote Karten an Spiel

<pre>
select spiel.nation1, spiel.nation2, tore1, tore2,gelb1,gelb2,rot1,rot2 from spiel join nation on spiel.nation1 = nation.iaaf join gruppe on gruppe.nation1 = nation.iaaf or gruppe.nation2 = nation.iaaf or gru
ppe.nation3 = nation.iaaf or gruppe.nation4 = nation.iaaf where gruppe.name = 'A';
</pre>
  
(1) http://www.sqlitetutorial.net/sqlite-python/creating-database/

(2) https://de.wikipedia.org/wiki/Liste_der_IAAF-L%C3%A4nder-Codes