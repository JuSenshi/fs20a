# Aufgabe 1
SELECT * FROM mitarbeiter;

# Aufgabe 2
SELECT Nachname, WohnWohnort FROM mitarbeiter;

# Aufgabe 3
SELECT Nachname, Supportlevel, Kenntnisse FROM mitarbeiter;

# Aufgabe 4
SELECT SUM(Gehalt) FROM mitarbeiter;

# Aufgabe 5
SELECT COUNT(Personalnummer) FROM mitarbeiter;

# Aufgabe 6
SELECT MAX(Gehalt) FROM mitarbeiter;

# Aufgabe 7
SELECT MIN(Gehalt) FROM mitarbeiter;

# Aufgabe 8
SELECT AVG(Gehalt) FROM mitarbeiter;

# Aufgabe 9
SELECT Gehalt FROM mitarbeiter GROUP BY Gehalt;

# Aufgabe 10
SELECT COUNT(Personalnummer), Supportlevel FROM mitarbeiter GROUP BY Supportlevel;

# Aufgabe 11
SELECT COUNT(Personalnummer), Wohnort FROM mitarbeiter GROUP BY Wohnort;

# Aufgabe 12
SELECT COUNT(Personalnummer) FROM mitarbeiter WHERE Wohnort = 'Dortmund';

# Aufgabe 13
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE Wohnort = 'Essen';

# Aufgabe 14
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE Gehalt > 5000;

# Aufgabe 15
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE Gehalt BETWEEN 1000 AND 2000;

# Aufgabe 16
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE Vorname IN ('Jonas', 'Peter');

# Aufgabe 17
SELECT Vorname, Nachname FROM mitarbeiter WHERE Supportlevel IS NULL;

# Aufgabe 18
SELECT Vorname, Nachname FROM mitarbeiter WHERE Supportlevel IS NOT NULL;

# Aufgabe 19
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE  Wohnort = 'Dortmund' AND Supportlevel = 2 AND Kenntnisse LIKE '%CISCO%';

# Aufgabe 20
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE  Wohnort = 'Dortmund' AND Supportlevel = 2 AND Kenntnisse LIKE '%Cisco%';

# Aufgabe 21
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE  Kenntnisse LIKE '%Drucker%';

# Aufgabe 22
SELECT Personalnummer, Vorname, Nachname FROM mitarbeiter WHERE  Gehalt > 2000 AND Supportlevel IN (2,3);