from python_training_mantis.fixture.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    project = Project(name=app.project.random_name(), status="development",
                      view_status="public", description="test description 1245")
    old_projects = app.project.get_project_list()
    app.project.add_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)