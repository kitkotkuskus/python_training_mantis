from python_training_mantis.model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.add_project()