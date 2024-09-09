from model.project import Project
import random
import string


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def random_name(self):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(4)])

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("status").click()
        wd.find_element_by_css_selector("option[value='10']").click()
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_css_selector("option[value='10']").click()
        wd.find_element_by_name("description").send_keys("test description 1245")
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_project(self, project_id):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(project_id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def select_project_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'project_id=%s')]" % project_id).click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            project_cache = []
            table = wd.find_element_by_xpath("//table[3]/tbody")
            rows = table.find_elements_by_tag_name("tr")
            for row in rows[2:]:
                cells = row.find_elements_by_tag_name("td")
                project = cells[0].find_element_by_css_selector("a[href*='project_id=']")
                id = project.get_attribute("href").split("project_id=")[1]
                name = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                project_cache.append(Project(id=id, name=name, status=status,
                                             view_status=view_status, description=description))
            return list(project_cache)

