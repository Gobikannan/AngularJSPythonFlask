from openpyxl import Workbook
from openpyxl.styles import Font
import datetime
import config
import database as dbaa


def save(id, target, freeText, ptasks, appName):

    wb = Workbook()
    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id + ".xlsx"
    ws1 = wb.active

    ws1.title = appName

    ws1['A1'].font = ws1['B1'].font = ws1['A3'].font = ws1['A2'].font = ws1['B2'].font = ws1['B3'].font = Font(bold=True)
    ws1['A1'] = "Application Name"
    ws1['B1'] = appName
    ws1['A2'] = "Target/Location"
    ws1['B2'] = target

    ws1['A3'] = "Pre-Conditions, Environment Details"
    ws1['B3'] = freeText

    currentDT = datetime.datetime.now()
    # https://tecadmin.net/get-current-date-time-python/
    # print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
    ws1['D5'] = currentDT.strftime("%d-%b-%Y")

    ws1['A6'].font = ws1['B6'].font = ws1['C6'].font = ws1['D6'].font = ws1['D5'].font = Font(bold=True)

    ws1['A6'] = "Sl #"
    ws1['B6'] = "Type"
    ws1['C6'] = "Step"
    ws1['D6'] = "Result"

    rowIndex = 7
    for ptask in ptasks:
        steps = ""
        for step in ptask['Steps']:
            steps = steps + step
            if(len(ptask['Steps']) > 1):
                steps = steps + ", "
        ws1['A' + str(rowIndex)] = rowIndex - 6
        ws1['B' + str(rowIndex)] = ptask['Type']
        ws1['C' + str(rowIndex)] = steps
        ws1['D' + str(rowIndex)] = ''
        rowIndex += 1

    for col in ws1.columns:
     max_length = 0
     column = col[0].column # Get the column name
     for cell in col:
         try: # Necessary to avoid error on empty cells
             if len(str(cell.value)) > max_length:
                 max_length = len(cell.value)
         except:
             pass
     adjusted_width = (max_length + 2) * 1.2
     ws1.column_dimensions[column].width = adjusted_width

    wb.save(filename=dest_filename)
