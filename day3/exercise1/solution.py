
def navigate(lines,probeRight, probeDown):
	treeIdentifier = "#"
	startRow = probeDown
	startColumn = probeRight
	realIndex = startColumn

	treesNr = 0

	while startRow < len(lines):  
	
		currentLine = lines[startRow]
		maxSize = len(currentLine)-1

		if currentLine[startColumn] == treeIdentifier :
			treesNr +=1
			
		print(f"currentLine : '{currentLine}' startRow : {startRow} startColumn : {startColumn} realIndex : {realIndex} field : {currentLine[startColumn]}")

		startRow += probeDown
		startColumn = (startColumn + probeRight) % maxSize
		realIndex += probeRight

	return treesNr

f = open("..\input.txt", "r")
lines = f.readlines()

trees1 = navigate(lines,1,1)
trees2 = navigate(lines,3,1)
trees3 = navigate(lines,5,1)
trees4 = navigate(lines,7,1)
trees5 = navigate(lines,1,2)

print(trees1)
print(trees2)
print(trees3)
print(trees4)
print(trees5)

print(trees1 *trees2 *trees3 *trees4 *trees5)
