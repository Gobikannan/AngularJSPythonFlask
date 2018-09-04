from flask import Flask, request, jsonify
from flask_cors import CORS

import database as dba
import File as files
import Ptask as ptasks
import Scenario as scenario
import Testruns as testruns
import ExecDetails as execdetails
import exportToExcelApps as xclapps
import exportToDocsApps as docxapps
import exportToXmlApps as xmlapps
import exportToExcelScenarios as xclscenarios
import exportToXmlScenarios as xmlscenarios
import exportToPdfApps as pdfapps
import exportToPdfScenarios as pdfScenarios
import exportToDocsScenarios as docxScenarios

app = Flask(__name__)
CORS(app)

@app.teardown_request
def remove_session(ex=None):
    dba.session.close()

@app.route("/")
def hello():
    return "<h1>Welcome..</h1>"

# endpoint to show all applications from the file table
@app.route("/applications", methods=["GET"])
def get_all_applications():
    all_applications = files.get_files()
    return jsonify(all_applications)

# endpoint to show particular application with test cases
@app.route("/application/<id>", methods=["GET"])
def get_application(id):
    stepsResult = ptasks.get_test_cases(id)
    return jsonify(stepsResult)

# endpoint to save particular application with test cases in the file
@app.route("/application/<id>", methods=["POST"])
def save_application(id):
    fileFormat = request.json['fileFormat']
    target = request.json['target']
    freeText = request.json['freeText']
    ptasks = request.json['ptasks']
    appName = request.json['appName']

    files.update_file(id, freeText, target)

    if(fileFormat == 'XLS'):
        xclapps.save(id, target, freeText, ptasks, appName)
    elif(fileFormat == 'DOC'):
        docxapps.save(id, target, freeText, ptasks, appName)
    elif(fileFormat == 'PDF'):
        pdfapps.save(id, target, freeText, ptasks, appName)
    elif(fileFormat == 'XML'):
        xmlapps.save(id, target, freeText, ptasks, appName)

    return jsonify({ 'result' : 'success' })

# endpoint to show all scenarios from the file table
@app.route("/scenarios", methods=["GET"])
def get_all_scenarios():
    all_scenarios = scenario.get_scenarios()
    return jsonify(all_scenarios)

# endpoint to show all releases by scenario id linked to testruns
@app.route("/releases/<id>", methods=["GET"])
def get_all_releases(id):
    results = testruns.get_releases(id)
    return jsonify(results)

# endpoint to show all releases by scenario id linked to testruns
@app.route("/testexecdetails/<testrunid>", methods=["GET"])
def get_testexecdetails(testrunid):
    results = execdetails.get_testexecdetails(testrunid)
    return jsonify(results)

# endpoint to save particular testexecdetails in the file
@app.route("/testexecdetails/<testrunid>", methods=["POST"])
def save_scenario_tests(testrunid):
    fileFormat = request.json['fileFormat']
    scenarioName = request.json['scenarioName']
    releaseName = request.json['releaseName']
    tests = request.json['tests']

    if(fileFormat == 'XLS'):
        xclscenarios.save(testrunid, scenarioName, releaseName, tests)
    elif(fileFormat == 'DOC'):
        docxScenarios.save(testrunid, scenarioName, releaseName, tests)
    elif(fileFormat == 'PDF'):
        pdfScenarios.save(testrunid, scenarioName, releaseName, tests)
    elif(fileFormat == 'XML'):
        xmlscenarios.save(testrunid, scenarioName, releaseName, tests)

    return jsonify({ 'result' : 'success' })

if __name__ == '__main__':
    app.run(debug=True)

