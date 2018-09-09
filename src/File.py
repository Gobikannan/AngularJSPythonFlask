import database as dbaa

def get_files():
	fs = dbaa.session.query(dbaa.File).all()
	return [dict(id=f.id, name=f.name, target=f.target, setting=f.setting, content=f.content) for f in fs]

def update_file(id, setting, target):
    fs = dbaa.session.query(dbaa.File).filter(dbaa.File.id == id).first()
    fs.target = target
    fs.setting = setting
    dbaa.session.commit()
    return True
