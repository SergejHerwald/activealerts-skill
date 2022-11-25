from mycroft import MycroftSkill, intent_file_handler


class Activealerts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('activealerts.intent')
    def handle_activealerts(self, message):
        crit_counter = ''
        info_counter = ''
        warn_counter = ''

        self.speak_dialog('activealerts', data={
            'info_counter': info_counter,
            'crit_counter': crit_counter,
            'warn_counter': warn_counter
        })


def create_skill():
    return Activealerts()

