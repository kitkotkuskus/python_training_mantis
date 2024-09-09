import random
from model.project import Project


def test_del_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as("administrator")
    if len(app.project.get_project_list()) == 0:
        app.project.add_project()
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.del_project(project.id)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(old_projects, key=Project.id_or_max)











