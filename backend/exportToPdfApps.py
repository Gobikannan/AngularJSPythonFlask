from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
import datetime
import config

def save(id, target, freeText, ptasks, appName):
    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id + ".pdf"
    doc = SimpleDocTemplate(dest_filename, pagesize=letter)
    elements = []

    currentDT = datetime.datetime.now()
    # https://tecadmin.net/get-current-date-time-python/
    # print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))

    headers = [("Application Name", appName), 
                ("Target/Location", target),
                ("Pre-Conditions, Environment Details", freeText),
                ("Date", currentDT.strftime("%d-%b-%Y"))]
    
    headerTable = Table(headers)
    headerTable.setStyle([('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])
    elements.append(headerTable)
    
    elements.append(Spacer(1, 25))

    data = [("Sl #", "Type", "Step", "Result")]
    rowIndex = 1
    for ptask in ptasks:
        steps = ""
        for step in ptask['Steps']:
            steps = steps + step
            if(len(ptask['Steps']) > 1):
                steps = steps + ", "
        data.append((str(rowIndex), ptask['Type'], steps, ""))
        rowIndex += 1
    t = Table(data)
    t.setStyle([('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])
    elements.append(t)
    doc.build(elements)
