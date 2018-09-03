from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
import datetime
import config

def save(id, scenarioName, releaseName, tests):

    appName = scenarioName + "_" + releaseName
    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id + ".pdf"
    doc = SimpleDocTemplate(dest_filename, pagesize=letter)
    elements = []

    currentDT = datetime.datetime.now()
    headers = [("Scenario Name", scenarioName),
                ("Release Name", releaseName),
                ("Date", currentDT.strftime("%d-%b-%Y"))]

    headerTable = Table(headers)
    headerTable.setStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])
    elements.append(headerTable)

    elements.append(Spacer(1, 25))

    data = [("Type", "Step", "Data", "Result", "Comments")]
    for test in tests:
        if(test['isheader'] == True):
            data.append(("Script Name - " + test['filename'], "", "", "", ""))
        else:
            data.append((test['type'], test['step'], test['data'], test['result'], test['comments']))

    t = Table(data)
    t.setStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

    elements.append(t)
    doc.build(elements)
