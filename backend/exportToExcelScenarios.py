from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles.borders import Border, Side
import config
import database as dbaa

def save(id, scenarioName, releaseName, tests):
    
    appName = scenarioName + "_" + releaseName
    wb = Workbook()
    dest_filename = config.FILE_CONFIG['folderPath'] + appName + "_" + id +".xlsx"
    ws1 = wb.active
    ws1.title = appName
    
    ws1['A1'].font = ws1['B1'].font = ws1['A2'].font = ws1['B2'].font = Font(bold=True)
    ws1['A1'] = "Scenario Name"
    ws1['B1'] = scenarioName

    ws1['A2'] = "Release Name"
    ws1['B2'] = releaseName

    ws1['A4'].font = ws1['B4'].font = ws1['C4'].font = ws1['D4'].font = ws1['E4'].font = Font(bold=True)

    ws1['A4'] = "Type"
    ws1['B4'] = "Step"
    ws1['C4'] = "Data"
    ws1['D4'] = "Result"
    ws1['E4'] = "Comments"
    
    rowIndex = 5
    for test in tests:
        if(test['isheader'] == True):
            ws1['A' + str(rowIndex)] = test['filename']
        else:
            ws1['A' + str(rowIndex)] = test['type']
            ws1['B' + str(rowIndex)] = test['step']
            ws1['C' + str(rowIndex)] = test['data']
            ws1['D' + str(rowIndex)] = test['result']
            ws1['E' + str(rowIndex)] = test['comments']
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

    wb.save(filename = dest_filename)