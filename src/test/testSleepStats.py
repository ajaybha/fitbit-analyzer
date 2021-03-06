import unittest

from resources import RESOURCE_PATH
from stats import sleepStats
from util import utils
import datetime

class SleepStatsTestCase(unittest.TestCase):
    def test_firstMinuteAsleep(self):
        filepath =  RESOURCE_PATH + "\\unittest\\test_sleepStats.csv"
        data = utils.loadIntradayData(filepath)
        firstMinuteAsleep = sleepStats.getFirstMinuteAsleep(data)
        self.assertEqual(firstMinuteAsleep, 8)

        firstMinuteAsleep = sleepStats.getFirstMinuteAsleep(data, 10)
        self.assertEqual(firstMinuteAsleep, 8)

        firstMinuteAsleep = sleepStats.getFirstMinuteAsleep(data, 11)
        self.assertEqual(firstMinuteAsleep, 19)

        firstMinuteAsleep = sleepStats.getFirstMinuteAsleep(data, 500)
        self.assertEqual(firstMinuteAsleep, None)

    def test_basicStats(self):
        filepath =  RESOURCE_PATH + "\\unittest\\test_sleep_basic01.csv"
        data1 = utils.loadIntradayData(filepath)
        filepath =  RESOURCE_PATH + "\\unittest\\test_sleep_basic02.csv"
        data2 = utils.loadIntradayData(filepath)
        stats = sleepStats.generateBasicStats([data1, data2])

        self.assertEqual(stats.iloc[0].name, datetime.date(2016, 3, 21))
        self.assertEqual(stats.iloc[1].name, datetime.date(2016, 3, 22))

    def test_intradayStats(self):
        filepath =  RESOURCE_PATH + "\\unittest\\test_sleep_basic01.csv"
        data1 = utils.loadIntradayData(filepath)
        filepath =  RESOURCE_PATH + "\\unittest\\test_sleep_basic02.csv"
        data2 = utils.loadIntradayData(filepath)
        stats = sleepStats.generateIntradayStats([data1, data2])

        self.assertEqual(stats.iloc[0].name, datetime.date(2016, 3, 21))
        self.assertEqual(stats.iloc[1].name, datetime.date(2016, 3, 22))


if __name__ == '__main__':
    unittest.main()
