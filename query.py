#coding: utf-8
import urllib2

url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=DlQjR63uLL6EgrgaNa25tLFCK0WbWmyHJgFK2w7hX2ikzwRFIU9jLNyGan2EW4ofYTZFRpnneaNK4BXenX-KHQ9B4MKCbVR6jb23MU6N9w0'

r = urllib2.urlopen(url).read()
print r
