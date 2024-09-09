from fixture.project import Project


def test_add_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as("administrator")
    project = Project(name=app.project.random_name(), status="development",
                      view_status="public", description="test description 1245")
    old_projects = app.soap.get_project_list(username, password)
    app.project.add_project(project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)