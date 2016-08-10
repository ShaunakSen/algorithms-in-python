# MAGIC METHODS !!!

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time

    def __eq__(self, other_time):
        if self.second == other_time.second and self.minute == other_time.minute and self.hour == other_time.hour:
            return True
        else:
            return False

    def __lt__(self, other_time):
        if self.hour < other_time.hour:
            return True
        elif self.hour > other_time.hour:
            return False
        else:
            if self.minute < other_time.minute:
                return True
            elif self.minute > other_time.minute:
                return False
            else:
                if self.second < other_time.second:
                    return True
                elif self.second > other_time.second:
                    return False
                else:
                    return "Both are same"


def main():
    time1 = Time(2, 50, 40)
    print "Time 1", time1
    time2 = Time(2, 50, 40)
    time_temp = Time(time2.hour, time2.minute, time2.second)
    print "Time 2", time2
    time3 = time2 + time1
    print "Time 3", time3
    # print time_temp
    print time1 == time_temp
    print time2
    print "{} < {}: {}".format(time2, time1, time2 < time1)


main()
