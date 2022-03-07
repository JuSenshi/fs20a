# Aufgabe 1
SELECT * FROM ticket;

# Aufgabe 2
SELECT Problembeschreibung FROM ticket;

# Aufgabe 3
SELECT Anfrageart, Problembeschreibung FROM ticket WHERE Anfrageart = "Stoerungsfall";

# Aufgabe 4
SELECT Anfrageart, Problembeschreibung FROM ticket WHERE Anfrageart LIKE 'S%';

# Aufgabe 5  /  Rechtschreibfehler
SELECT Ticketnummer FROM ticket WHERE Anfrageart = 'Stoerungsfall' AND Dringklichkeit = 1;

# Aufgabe 6
SELECT Anfrageart, Dringklichkeit FROM ticket ORDER BY Dringklichkeit;

# Aufgabe 7
SELECT Anfrageart, Dringklichkeit FROM ticket ORDER BY Dringklichkeit DESC;

# Aufgabe 8
SELECT Ticketnummer FROM ticket WHERE Dringklichkeit IN (1,2);
#ALTERNATIVE
SELECT Ticketnummer FROM ticket WHERE Dringklichkeit = 1 or Dringklichkeit = 2;

# Aufgabe 9
SELECT Ticketnummer FROM ticket WHERE Dringklichkeit != 1;

# Aufgabe 10
SELECT Ticketnummer FROM ticket WHERE STATUS IS null;
#ALTERNATIVE
SELECT Ticketnummer FROM ticket WHERE STATUS NOT LIKE '?%';

# Aufgabe 11
SELECT Ticketnummer FROM ticket WHERE STATUS IS NOT null;
#ALTERNATIVE
SELECT Ticketnummer FROM ticket WHERE STATUS LIKE '?%';

# Aufgabe 12
SELECT Ticketnummer, Problembeschreibung FROM ticket WHERE Problembeschreibung LIKE '%Drucker%';

# Aufgabe 13
SELECT min(Dringklichkeit) as 'Eilt nicht' FROM ticket;

# Aufgabe 14
SELECT MAX(Dringklichkeit) as 'DIE HÜTTE BRENNT' FROM ticket;

# Aufgabe 15
SELECT Dringklichkeit FROM ticket GROUP BY Dringklichkeit;

# Aufgabe 16
SELECT COUNT(Ticketnummer) FROM ticket;

# Aufgabe 17
SELECT Ticketnummer, Erstellungsdatum FROM ticket WHERE Erstellungsdatum > '2022-01-10'

# Aufgabe 18
SELECT Ticketnummer, Erstellungsdatum FROM ticket WHERE Erstellungsdatum BETWEEN '2022-01-10' AND '2022-01-15';