import random


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.get_project_list()
    all_project = app.contact.get_project_list()
    project = random.choice(all_project)
    app.project.del_project(project.id)