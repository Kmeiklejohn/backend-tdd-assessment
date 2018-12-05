#!/usr/bin/env python
# -*- coding: utf-8 -*-
import echo
import unittest
import subprocess

# Your test case class goes here
class TestEcho(unittest.TestCase):
    
    
    def setUp(self):
        self.parser = echo.create_parser()
    
    def test_help(self):
        """ Running the program without arguments should show usage. """

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        args_list = ["--u", "hello" ]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.upper)


        self.assertEqual(echo.main(args_list), "HELLO")

    def test_upper_long(self):
        args_list = ["--upper", "hello" ]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.upper)


        self.assertEqual(echo.main(args_list), "HELLO") 

    def test_lower(self):
        args_list = ["--l", "HELLO" ]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.lower)


        self.assertEqual(echo.main(args_list), "hello")   

    def test_lower_long(self):
        args_list = ["--lower", "HELLO"]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.lower)
        self.assertEqual(echo.main(args_list), "hello")
    
    def test_title(self):
        args_list = ["--t", "heLLo"]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.title)
        self.assertEqual(echo.main(args_list), "Hello")

    def test_title_long(self):
        args_list = ["--title", "heLLo"]
        args = self.parser.parse_args(args_list)
        self.assertTrue(args.title)
        self.assertEqual(echo.main(args_list), "Hello")

    
if __name__ == '__main__':
    unittest.main()
