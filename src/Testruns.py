import database as dbaa
from time import strftime

def get_releases(scenarioid):
	testruns = (dbaa.session.query(dbaa.Testruns).filter(dbaa.Testruns.scenario_id == scenarioid)).all()
	return [dict(id = testrun.id, extid = testrun.extid, scenarioid = testrun.scenario_id, date = testrun.date) for testrun in testruns]
 