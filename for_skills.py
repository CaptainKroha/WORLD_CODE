class ISkill:
    def __init__(self, name, options=None, wordings=None):
        self.name = name
        self.options = {}
        if options:
            self.options = dict(options)
        self.wordings = []
        if wordings:
            self.wordings = list(wordings)

    def print(self):
        print(f'Skill_name: {self.name}, options = [')
        for item in self.options.items():
            print(item)
        print('], wordings = [')
        for word in self.wordings:
            print(word)
        print(']')


class CompProfile:
    def __init__(self, fk, filters):
        self.fk = fk
        self.filters = dict(filters)
        self.skills = []

    def add_skill(self, name, options=None, wordings=None):
        self.skills.append(ISkill(name, options, wordings))

    def get_skills_names(self) -> list:
        names_list = [skill.name for skill in self.skills]
        return names_list


class ITemplate:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = dict(filters)
        self.skills = []

    def add_skill(self, name, options=None, wordings=None):
        self.skills.append(ISkill(name, options, wordings))

    def get_me(self):
        print(self.name)
        for item in self.filters.items():
            print(item)
        for skill in self.skills:
            skill.print()

    def do_compare(self, comp_profile: CompProfile) -> float:
        rate = 0
        skills_names_list = comp_profile.get_skills_names()
        for skill in self.skills:
            if skill.name in skills_names_list:
                rate += skill.options['priority']
            else:
                for wording in skill.wordings:
                    if wording in skills_names_list:
                        rate += skill.options['priority']
        return rate


if __name__ == "__main__":
    templ = ITemplate('DevOps', {"workYears": 5})
    templ.add_skill("SQL", {"priority": 1}, ["Structured Query Language"])
    templ.add_skill("Microsoft Excel", {"priority": 1}, ["MS Excel", "Excel"])
    templ.add_skill("Jira", {"priority": 1}, ["Atlassian Jira"])
    templ.add_skill("Confluence", {"priority": 1}, ["Atlassian Confluence"])
    templ.add_skill("UML", {"priority": 1}, ["Unified Modeling Language"])
    templ.add_skill("BPMN", {"priority": 1}, ["Business Process Model and Notation"])
    templ.add_skill("Python", {"priority": 0.5}, [])
    templ.add_skill("Git", {"priority": 0.5}, ["Git version control", "GitHub", "GitLab", "Bitbucket"])
    templ.add_skill("SOAP/REST", {"priority": 0.5}, ["SOAP API", "REST API", "Web Services"])

    prof = CompProfile(100, {"workYears": 3})
    prof.add_skill("REST API")
    prof.add_skill("Unified Modeling Language")
    prof.add_skill("Git")
    prof.add_skill("C++")
    prof.add_skill("Jira")

    res_rate = templ.do_compare(prof)
    print(res_rate)

