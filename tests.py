import unittest

from botchecker.checker import check


class BotCheckerTests(unittest.TestCase):

    def test_check_false(self):
        is_bot, bot = check("emrebeyler")
        self.assertEqual(is_bot, False)

    def test_check_true(self):
        is_bot, bot = check("buildawhale")
        self.assertEqual(is_bot, True)

    def test_check_bot_type(self):
        is_bot, bot = check("jerrybanfield")
        self.assertEqual(is_bot, True)
        self.assertEqual(bot.type, 'bid_bot')

        is_bot, bot = check("minnowbooster")
        self.assertEqual(is_bot, True)
        self.assertEqual(bot.type, 'other_bot')

    def test_check_bot_account(self):
        is_bot, bot = check("postpromoter")
        self.assertEqual(bot.account, "postpromoter")


if __name__ == '__main__':
    unittest.main()