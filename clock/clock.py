class Clock:
    def __init__(self, hours,mins):
        self.hours = hours
        self.mins = mins
        self.convert()

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.mins == other.mins)


    def __str__(self):
        return (self.form_hours() + ":" + self.form_mins())

    def add(self, add_mins):
        self.mins += add_mins
        self.convert()
        return self

    def convert(self):
        self.conv_mins()
        self.conv_hours()

    def conv_hours(self):
        self.hours = self.hours % 24

    def conv_mins(self):
        self.hours += self.mins // 60
        self.mins = self.mins % 60

    def form_hours(self):
        return str(self.hours).zfill(2)

    def form_mins(self):
        return str(self.mins).zfill(2)
