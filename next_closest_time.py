
class Solution:
    def string_to_int(self, time):
        hours, minutes = int(time[:2]), int(time[3:])
        return hours * 60 + minutes

    def int_to_string(self, minutes):
        hours, minutes = minutes // 60, minutes % 60
        return '{}{}:{}{}'.format(
            hours // 10, hours % 10, minutes // 10, minutes % 10
        )

    def is_valid(self, candidate, digits):
        s = self.int_to_string(candidate)
        return (
            s[0] in digits and s[1] in digits and
            s[3] in digits and s[4] in digits
        )

    def nextClosestTime(self, time):
        digits = {time[0], time[1], time[3], time[4]}
        base = self.string_to_int(time)

        for i in range(1, 24 * 60 + 1):
            candidate = (base + i) % (24 * 60)
            if self.is_valid(candidate, digits):
                return self.int_to_string(candidate)


if __name__ == '__main__':
    s = Solution()
    for time in [
        '19:34',
        '23:59',
        '11:11',
    ]:
        print(time, s.nextClosestTime(time))
