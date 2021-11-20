from notifypy import Notify


class notifications:

    def __init__(self, time: object):
        notification = Notify()
        notification.application_name = 'Work'
        notification.title = "Start"
        notification.message = '{0}'.format(time)
        notification.send()
