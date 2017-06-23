#!/usr/bin/env python

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from parse import parse
import argparse
import time
import os

parser = argparse.ArgumentParser(description='Create Anki/Mnemosyne importable csv/txt files from Quinterest')
parser.add_argument('-c','--category', help='All, Literature, History, Science, Fine Arts, Religion, Mythology, Philosophy, Social Science, Geography, Current Events, Trash', required=True)
parser.add_argument('-d','--difficulty', help='All, MS, HS, College, Open', required=True)
parser.add_argument('-f','--file', help='Name of file you want to save your clues to', required=True)
args = vars(parser.parse_args())

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("http://quinterest.org/")

select = Select(driver.find_element_by_id('optionCategory'))
select.select_by_value(args['category'])
select = Select(driver.find_element_by_id('optionDifficulty'))
select.select_by_value(args['difficulty'])
select = Select(driver.find_element_by_id('optionQType'))
select.select_by_value("Tossups")

driver.find_element_by_id("searchButton").click()

driver.find_element_by_id("loadAllTossupsButton").send_keys("\n")

time.sleep(10) 

text = driver.find_element_by_id("searchResults").text

driver.close()

tmpQ = open("tmpQ.txt","w")
tmpQ.write(text)

parse("tmpQ.txt", args["file"])

os.remove("tmpQ.txt")