import database as dbaa

def get_test_cases(id):
    ptasks = (dbaa.session.query(dbaa.Ptask).filter(dbaa.Sentence.file_id == id).filter(dbaa.Ptask.sentence_id == dbaa.Sentence.id)).all()

    stepsResult = []
    prevStepType = ""

    for x in ptasks:
        if prevStepType == x.T:
            print(x.step)
            prevStep = stepsResult[-1]
            if prevStep:
                prevStep['Steps'].append(x.step)
        else:
            prevStepType = x.T
            currentStep = []
            currentStep.append(x.step)
            currentStepResult = { 'Type': x.T, 'Steps': currentStep }
            stepsResult.append(currentStepResult)
    
    return stepsResult
