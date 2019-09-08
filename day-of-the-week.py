# coding=utf-8


weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

default_year = 1999
default_month = 7
default_day = 18


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # 以 1999-7-18 为标准 Sunday
        # if year == default_year and month == default_month and day == default_day:
        #     return weeks[0]

        after_days = 0
        if year > default_year:
            for i in range(default_year, year):
                if self.isLeapYear(i+1):
                    after_days += 366
                else:
                    after_days += 365
        else:
            for i in range(year, default_year):
                if self.isLeapYear(i+1):
                    after_days -= 366
                else:
                    after_days -= 365

        if month > default_month:
            for i in range(default_month, month):
                after_days += months[i-1]
        else:
            for i in range(month, default_month):
                if self.isLeapYear(year):
                    after_days -= leap_months[i-1]
                else:
                    after_days -= months[i-1]

        if day > default_month:
            after_days += day - default_day
        else:
            after_days -= default_day - day

        return weeks[after_days % 7]


    # 这样写下来真的太累了，过于复杂
    #     if year > default_year or (year == default_year and month > default_month) or (year == default_year and month == default_month and day > default_day):
    #         return self.after_day(day, month, year)
    #     return self.before_day(day, month, year)
    #
    # def after_day(self, day, month, year):
    #     # 不能按照每四年一轮回计算，因为 闰年不是 每四年一轮回
    #     # after_year = (year - 1999) % 4
    #
    #     # 到 后面某年的 7月18日 这一天
    #     after_days = 0
    #     for i in range(default_year, year):
    #         if self.isLeapYear(i+1):
    #             after_days += 366
    #         else:
    #             after_days += 365
    #
    #     # 到后面某年某月的 18 日这一天
    #     if month >= default_month:
    #         for i in range(default_month, month):
    #             after_days += month[i+1]
    #
    #         if day > default_day:
    #             after_days += day - default_day
    #         else:
    #             after_days += default_day - day
    #
    #         return weeks[after_days % 7]
    #     else:
    #         for i in range(default_month, month, -1):
    #             after_days -= month[i-1]
    #
    #
    #
    #
    #
    #     return
    #
    # def before_day(self, day, month, year):
    #     return

    def isLeapYear(self, year):
        return bool((not year % 4 and year % 100) or (not year % 400))


if __name__ == '__main__':
    s = Solution()
    print s.dayOfTheWeek(31, 8, 2019)
    print s.dayOfTheWeek(18, 7, 1999)
    print s.dayOfTheWeek(15, 8, 1993)
