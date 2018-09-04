import xml.etree.cElementTree as ET
import datetime
import config

def save(id, target, freeText, ptasks, appName):

    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id + ".xml"
    currentDT = datetime.datetime.now()

    root = ET.Element("root")
    details = ET.SubElement(root, "details")

    ET.SubElement(details, "ApplicationName").text = appName
    ET.SubElement(details, "TargetLocation").text = target
    ET.SubElement(details, "PreConditions").text = freeText
    ET.SubElement(details, "Date").text = currentDT.strftime("%d-%b-%Y")

    testcases = ET.SubElement(root, "TestCases")

    rowIndex = 1
    for ptask in ptasks:
        steps = ""
        for step in ptask['Steps']:
            steps = steps + step
            if(len(ptask['Steps']) > 1):
                steps = steps + ", "
        testcase = ET.SubElement(testcases, "TestCase")
        ET.SubElement(testcase, "SlNo").text = str(rowIndex)
        ET.SubElement(testcase, "Type").text = ptask['Type']
        ET.SubElement(testcase, "Step").text = steps
        ET.SubElement(testcase, "Result").text = ""
        rowIndex += 1

    tree = ET.ElementTree(root)
    tree.write(dest_filename)
