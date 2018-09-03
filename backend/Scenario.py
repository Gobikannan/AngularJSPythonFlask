import database as dbaa

def get_scenarios():
	fs = dbaa.session.query(dbaa.Scenarios).all()
	return [dict(id = f.id, name = f.name, envt = f.envt) for f in fs]
