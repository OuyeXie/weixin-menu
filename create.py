#coding: utf-8
import urllib2
import json
import ssl 

ssl._create_default_https_context = ssl._create_unverified_context

#data = ‘’’{
#    “button”:[
#    {
#        “name”: “PK 神股票”,
#        “sub_button”:[
#        { 
#            “type”:”view”,
#            “name”:”我的排行”,
#            “url”:”https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxd34fed2afc9f960e&redirect_uri=http%3A%2F%2Fshengupiao.com%2Fmygame&response_type=code&scope=snsapi_base&state=service#wechat_redirect”
#        },
#        { 
#            “type”:”click”,
#            “name”:”如何玩”,
#            “key”:”HOW_TO_PLAY”
#        }]
#    },
#    {
#        “type”:”click”,
#        “name”:”新三板”,
#        “key”:”NEEQ”
#    }]
#}’’’


data = ‘’’{
    “button”:[
    {
            “type”:”view”,
            “name”:”摇一摇”,
            “url”:”http://shengupiao.com/shake”
    }]
}’’’

url = ‘https://api.weixin.qq.com/cgi-bin/menu/create?access_token=DlQjR63uLL6EgrgaNa25tLFCK0WbWmyHJgFK2w7hX2ikzwRFIU9jLNyGan2EW4ofYTZFRpnneaNK4BXenX-KHQ9B4MKCbVR6jb23MU6N9w0'

r = urllib2.urlopen(url, data).read()
print r
