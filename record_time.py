import sqlite3
import pathlib


class record:
    def __init__(self):
        ROOTDIR = pathlib.Path(__file__).parent.absolute()
        db = f'{ROOTDIR}/time.db'
        self.con = sqlite3.connect(db)

    def __del__(self):
        self.con.close()

    def createOrConnectDB(self):
        curr = self.con.cursor()
        curr.execute(
            '''
            CREATE TABLE IF NOT EXISTS time(
            month INT NOT NULL,
            day   INT NOT NULL,
            hour  INT NOT NULL,
            min   INT NOT NULL,
            sec   INT NOT NULL
            )
            '''
        )

    def insertIntoDB(self, _month: int, _day: int, _hour: int, _min: int, _sec: int):
        curr = self.con.cursor()
        command = 'INSERT INTO time VALUES({0},' \
            '{1}, {2}, {3}, {4})'.format(_month, _day, _hour, _min, _sec)
        print(command)
        curr.execute(command)

    def readTime(self, _month: int, _day: int, _hour: int, _min: int, _sec: int):
        curr = self.con.cursor()
        command = 'SELECT * FROM time WHERE' \
                  '(month={0} ' \
                  'and day={1} ' \
                  'and hour={2} ' \
                  'and min={3} ' \
                  'and sec={4})'.format(_month, _day, _hour, _min, _sec)

        res = curr.execute(command).fetchall()
        for r in res:
            print(r)

    def returnHoursWorkedInWeek(self, _month: int, _day: int):
        # TODO
        # need to figure out a way that I can
        # find when the begining of the week was based
        # on what the date that is entered in
        #
        # ex. today is 11-20-21
        # if the date entered in is 11-23-21
        # how will I know that 11-23 is not monday
        # but is tuesday and I need to include monday?
        curr = self.con.cursor()
        command = 'SELECT * FROM time WHERE' \
                  '(month={0} )' \
                  'and day={1}'.format(_month, _day)
        res = curr.execute(command).fetchall()
