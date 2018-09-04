import xml.etree.cElementTree as ET
import datetime
import config

def save(id, scenarioName, releaseName, tests):

    appName = scenarioName + "_" + releaseName
    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id + ".xml"
    currentDT = datetime.datetime.now()

    root = ET.Element("root")
    details = ET.SubElement(root, "details")

    ET.SubElement(details, "ScenarioName").text = scenarioName
    ET.SubElement(details, "ReleaseName").text = releaseName
    ET.SubElement(details, "Date").text = currentDT.strftime("%d-%b-%Y")

    testcases = ET.SubElement(root, "TestCases")

    filename = ""
    for test in tests:
        if(test['isheader'] == True):
            filename = test['filename']
        else:
            testcase = ET.SubElement(testcases, "TestCase", name=filename)
            ET.SubElement(testcase, "Type").text = test['type']
            ET.SubElement(testcase, "Step").text = test['step']
            ET.SubElement(testcase, "Data").text = test['data']
            ET.SubElement(testcase, "Result").text = test['result']
            ET.SubElement(testcase, "Comments").text = test['comments']

    tree = ET.ElementTree(root)
    tree.write(dest_filename)
