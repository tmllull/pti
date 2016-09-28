#! /usr/bin/python

# Llibreries
import cgi, os, re, sys, string, time, csv

# Programa principal

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

camps_requerits = ('model_vehicle', 'sub_model_vehicle', 'dies_lloguer', 'num_vehicles', 'descompte')

for i in camps_requerits:
	if not form.has_key(i):
		print "<h1>INFORMACIÓ INCOMPLETA!!</h1>"
		print "<h3>Plena tots els camps, si us plau</h3>"
		sys.exit()

model = form["model_vehicle"].value
sub_model = form["sub_model_vehicle"].value
num_dies = form["dies_lloguer"].value
num_vehicles = form["num_vehicles"].value
desc = form["descompte"].value
preu_total = int(model)*int(num_dies)*int(num_vehicles)*(1 - float(desc)/100)

c = csv.writer(open("MYFILE.csv", "a"))
c.writerow([model, sub_model, num_dies, num_vehicles, desc, preu_total])

print "<p>Model vehicle: ", model
print "<p>Motor: ", sub_model
print "<p>Dies llogats: ", num_dies
print "<p>Número vehicles llogats: ", num_vehicles
print "<p>Descompte(%): ", desc
print "<p>Import total: ", preu_total 

