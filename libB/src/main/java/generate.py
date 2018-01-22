import os, shutil

packageNum = 20
classPerPackage = 20
prefix = "B"


pNum = 0
for pNum in range(packageNum):
	dirName = "package_"+prefix+"_"+str(pNum)
	try:
	    shutil.rmtree(dirName)
	except:
	    print("asd")
	os.mkdir(dirName)
	cNum = 0
	for cNum in range(classPerPackage):
		fileName = dirName+"/"+"Foo_"+prefix+"_"+str(pNum)+str(cNum)+".kt"
		fH = open(fileName,"w+")
		fH.write("package "+dirName+"\n")
		if cNum == 0 and pNum > 0:
		    fH.write("import package_"+prefix+"_"+str(pNum-1)+".Foo_"+prefix+"_" +str(pNum-1)+str(classPerPackage-1)+"\n")
		fH.write("class Foo_"+prefix+"_"+str(pNum)+str(cNum)+" {\n")
		fH.write("fun foo0() {\n")
		fH.write("var i=0\n")
		lNum = 0
		for lNum in range(20):
			fH.write("i+=Math.random().toInt()\n")
		if cNum > 0:
			fH.write("Foo_"+prefix+"_"+str(pNum)+str(cNum-1)+"().foo0()\n")
		elif pNum > 0:
		    fH.write("Foo_"+prefix+"_"+str(pNum-1)+str(classPerPackage-1)+"().foo0()\n")
		fH.write("}\n")
		fH.write("}")
		fH.close()
