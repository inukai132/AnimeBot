import unittest, requests
from Bot import *

class NyaaTests(unittest.TestCase):
    def testConnect(self):
        r = requests.get('https://nyaa.si')
        self.assertEqual(r.status_code,200,"nyaa.si is down or could not be reached")

    def testSearch(self):
        rows = Bot.nyaaSearch("Naruto")
        self.assertGreater(len(rows),0)

    def testUrl(self):
        url = Bot.makeNyaaUrl("TEST",1)
        self.assertEqual(url,"https://nyaa.si/?f=0&c=1_2&q=TEST&p=1")

    def testUrlSpaces(self):
        url = Bot.makeNyaaUrl("TEST QUERY",1)
        self.assertEqual(url,"https://nyaa.si/?f=0&c=1_2&q=TEST%20QUERY&p=1")

    def testGetSeeds(self):
        self.fail("Not implemented")

    def testGetMagnet(self):
        self.fail("Not implemented")

    def testGetQuality(self):
        self.fail("Not implemented")

    def testGetSize(self):
        self.fail("Not implemented")


class PantsuTests(unittest.TestCase):
    def testConnect(self):
        r = requests.get('https://nyaa.pantsu.cat')
        self.assertEqual(r.status_code,200,"nyaa.pantsu.cat is down or could not be reached")

    def testSearch(self):
        self.fail("Not implemented")

    def testUrl(self):
        self.fail("Not implemented")

    def testGetSeeds(self):
        self.fail("Not implemented")

    def testGetMagnet(self):
        self.fail("Not implemented")

    def testGetQuality(self):
        self.fail("Not implemented")

    def testGetSize(self):
        self.fail("Not implemented")


class DatabaseTests(unittest.TestCase):
    def testConnect(self):
        self.fail("Not implemented")

    def testAddTorrent(self):
        self.fail("Not implemented")

    def testAddShow(self):
        self.fail("Not implemented")

    def testAddEpisode(self):
        self.fail("Not implemented")

    def testCleanup(self):
        self.fail("Not implemented")

class TorrentTests(unittest.TestCase):
    def testConnect(self):
        self.fail("Not implemented")

    def testAddTorrent(self):
        self.fail("Not implemented")

    def testAddLabel(self):
        self.fail("Not implemented")

    def testGetRealSeeds(self):
        self.fail("Not implemented")

    def testDownloadLocation(self):
        self.fail("Not implemented")

    def testCleanup(self):
        self.fail("Not implemented")

    def testConnect(self):
        self.fail("Not implemented")

    def testConnect(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
