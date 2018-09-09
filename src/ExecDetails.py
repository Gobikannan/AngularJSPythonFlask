import database as dbaa

def get_testexecdetails(testrunid):
    testexecs = (dbaa.session.query(dbaa.Execdetails).filter(dbaa.Execdetails.testrun_id == testrunid)).all()

    stepsResult = []
    prevFileId = ""

    for testexec in testexecs:
        if prevFileId == "" or prevFileId != testexec.file_id:
            file = dbaa.session.query(dbaa.File).filter(dbaa.File.id == testexec.file_id).first()
            stepsResult.append(dict(isheader=True, filename = file.name))    
        testexecResult = dict(isheader=False, id=testexec.id, type=testexec.T, step=testexec.step, data=testexec.D2, result=testexec.passfail, comments=testexec.comments, file_id=testexec.file_id)
        stepsResult.append(testexecResult)
        prevFileId = testexec.file_id

    return stepsResult
