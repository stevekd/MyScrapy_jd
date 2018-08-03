# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random


class RandomUserAgentMiddleWare(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self,crawler):
        super(RandomUserAgentMiddleWare,self).__init__()
        self.user_agent_list=crawler.settings.get('USER_AGENT_LIST',[])

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(crawler)

    def process_request(self, request, spider):

        request.headers.setdefault(b"User-Agent",random.choice(self.user_agent_list))






