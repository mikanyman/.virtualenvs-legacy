from fabric.api import local

def compile_messages():
    local("sudo chown -R mnyman.mnyman locale")
    local("python manage.py compilemessages")
    local("sudo apache2ctl restart")
    
def dump_fixtures():
    local("python manage.py dumpdata --format=json wiki > /home/mnyman/.virtualenvs/maisemapaikka/staging/maisemapaikka/apps/wiki/fixtures/wiki_data.json")
