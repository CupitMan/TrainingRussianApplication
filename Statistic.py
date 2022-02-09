class Statistic:

    def __init__(self, name: str, start_time: int, end_time: int, all_count: int, right_count: int, wrong_count: int):
        self.items = {
            "name": name,
            "timeStart": start_time,
            "timeEnd": end_time,
            "allCount": all_count,
            "rightCount": right_count,
            "wrongCount": wrong_count
        }

    def PercentsResultTest(self):

        all = self.items["allCount"]
        rights = self.items["rightCount"]

        result = round((rights / all) * 100, 2)

        if result == int(result):
            return int(result)
        else:
            return result

    def GetTimeTest(self):

        seconds = self.items["timeEnd"] - self.items["timeStart"]

        hours = str(seconds // 3600)
        minutes = str(seconds % 3600 // 60)
        seconds = str(seconds % 3600 % 60)

        hours = hours.rjust(2, '0')
        minutes = minutes.rjust(2, '0')
        seconds = seconds.rjust(2, '0')

        return ':'.join([hours, minutes, seconds])

