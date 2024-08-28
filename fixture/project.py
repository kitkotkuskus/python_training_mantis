from python_training_mantis.model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form()
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def fill_project_form(self):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("test1")
        wd.find_element_by_name("status").click()
        wd.find_element_by_css_selector("option[value='10']").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_css_selector("option[value='10']").click()
        wd.find_element_by_name("description").send_keys("test description 1245")

    def del_project(self, id):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_elements_by_css_selector("//td[@id='%s']" % id).click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_project_page()
        for element in wd.find_elements_by_css_selector("tr[class^='row-']"):
            cells = element.find_elements_by_tag_name('td')
            # id = element.find_element_by_css_selector("a[href*='project_id']").
            name = cells[0].text
            status = cells[1].text
            enabled = cells[2].text
            view_status = cells[3].text
            description = cells[4].text
            print(name)
            print(status)
            print(enabled)
            print(view_status)
            print(description)
        return Project(name=name, status=status, enabled=enabled,
                        view_status=view_status, description=description)


