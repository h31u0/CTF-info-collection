from bs4 import BeautifulSoup
import requests
import html

class CTF:
	def __init__(self):
		self.name = ""
		self.date = ""
		self.location = ""
		self.url = ""
		self.organizer = ""
		self.format = ""
		self.online = False
		
	def __str__ (self):
		return "CTF:" + self.name + self.date + self.format + "ONLINE" if self.online else "" + self.organizer + self.location + self.url

	def __getitem__(self, i):
		return [self.name, self.date, self.format, self.online, self.organizer, self.location, self.url][i]

import feedparser
class CtftimeProducer:
    def __init__(self):
        pass
    def get_data(self):
        """
        get ctf data from ctftime via rss.

        self.ctflist will be cleaned and filled with new elements

        Returns:
            return self.ctflist: a list of CTF instance
        """
        data = feedparser.parse("https://ctftime.org/event/list/upcoming/rss/", 30)
        self.ctflist = []
        for rss_data in data.entries:
            ctf_entry = html.unescape(rss_data.description).split("<br />")
            ctf = CTF()
            ctf.name = BeautifulSoup(ctf_entry[0], features="html.parser").get_text().split(":",1)[-1].strip()
            ctf.date =BeautifulSoup(ctf_entry[1], features="html.parser").get_text()[:-17].split(":",1)[-1].strip()
            ctf.format =BeautifulSoup(ctf_entry[2], features="html.parser").get_text().split(":",1)[-1].strip()
            for i in ctf_entry[3:]:
                if "On-line" in i:
                    ctf.online = True
                if "Offical URL" in i:
                    ctf.url = BeautifulSoup(i, features="html.parser").get_text().split(":",1)[-1].strip()
                if "Location" in i:
                    ctf.location = BeautifulSoup(i, features="html.parser").get_text().split(":",1)[-1].strip()
                if "Event organizers" in i:
                    ctf.organizer = BeautifulSoup(i, features="html.parser").get_text().split(":",1)[-1].strip()
            self.ctflist.append(ctf)
        return self.ctflist
