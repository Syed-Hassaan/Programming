def writeHTML():
	with open("filename.html","w") as html:
		html.write("<!DOCTYPE html>\n")
		html.write("<html>\n")
		html.write("<head>\n")
		html.write("<meta charset=\"UTF-8\">\n")
		html.write("<style>\n")
		html.write("table, th, td {\n")
		html.write("border: 1px solid black;\n")
		html.write("border-collapse: collapse;\n")
		html.write("}\n")
		html.write("</style>\n")
		html.write("<title>Title of the document</title>\n")
		html.write("</head>\n")
		html.write("<body>\n")
		html.write("<h2>Header title</h2>\n")
		html.write("<table>\n")
		with open("scores.csv","r") as students:
			students.readline()
			html.write("<tr>\n")
			html.write("<th>Header 1</th>\n")	
			html.write("<th>Header 2</th>\n")
			html.write("<th>Header 3</th>\n")
			html.write("<th>Header 4</th>\n")
			html.write("<th>Header 5</th>\n")
			html.write("</tr>\n")
		
			reader = csv.reader(csv_table)

			for row in reader:
				html.write("<tr>\n" + elm + "</td>\n")
			time = int(row[0])
			latitude = int(row[1])
			longitude = int(row[2])
			depth = int(row[3])
			mag = int(row[4])
		
		html.write("</table>\n")
		html.write("</body>\n")
		html.write("</html>\n")
