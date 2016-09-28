#! /usr/bin/python

# Llibreries
import cgi, os, re, sys, string, time, csv

# Constants

ADMIN = "admin"
PASS = "I'mGod"

# Programa principal

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

camps_requerits = ('userid', 'password')

for i in camps_requerits:
	if not form.has_key(i):
		print "<h1>INFORMACIÓ INCOMPLETA!!</h1>"
		sys.exit()

if form["userid"].value == ADMIN and form["password"].value == PASS:
	cr = csv.reader(open("MYFILE.csv", "rb"))
	i = 0
	for row in cr:
		print "<p>Registre ", i, ":</p>"
		print "<p>Model: ", row[0]
		print "<p>Motor: ", row[1]
		print "<p>Dies: ", row[2]
		print "<p>Unitats: ", row[3]
		print "<p>Descompte: ", row[4]
		print "<p>Preu total: ", row[5]
		print "<p>______________________________"
		i++
else:
	print "<H1>USER o PASS incorrectes</H1>"
