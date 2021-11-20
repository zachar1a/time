from datetime import datetime
from notifications import notifications
from record_time import record


class time_:

    def __init__(self):
        self.time = datetime.now()
        self.time_stamp = datetime.strptime(
            str(self.time).split('.')[0],
            "%Y-%m-%d %H:%M:%S")
        print(self.time_stamp.day)
        print(self.time_stamp.hour)
        print(self.time_stamp.minute)
        print(self.time_stamp.second)
        self.r = record()

    def notification(self):
        notifications(str(self.time))

    def record(self):
        self.r.createOrConnectDB()
        self.r.insertIntoDB(self.time_stamp.month,
                            self.time_stamp.day,
                            self.time_stamp.hour,
                            self.time_stamp.minute,
                            self.time_stamp.second)

    def readTime(self):
        self.r.readTime(self.time_stamp.month,
                        self.time_stamp.day,
                        self.time_stamp.hour,
                        self.time_stamp.minute,
                        self.time_stamp.second)
        pass


def main():
    t = time_()
    t.notification()
    t.record()

if __name__ == '__main__':
    main()
