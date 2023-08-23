#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "20574097"))
    API_HASH = os.environ.get("API_HASH" , "278d1014e386425e05d2d67cc62a5ac7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2108427614:AAFgNBxwh8kOAAWu8Jyaqy1Puv3O5XCT7K8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001539983068")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "2109516065")
    LIMIT = int(os.environ.get("LIMIT", "25000000000000000000000000000000000000000000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION" "BQAKhYPH1j5sgnYjq_Kus6I2rj70yd3QgIfkAsqLr2Ka_URaJy_69fFUYqWxc5yi_z8toVQZOSfM6jS1hyQ8VevVwSpBJipCUZtlbkZCimSKtRtPKK1IZc7SrXJaxWgc8EWdjnrMI7BNpVX5R8-3POtdauUoXRW2bpAy5KzP_XKrVu-4p2FWPe9w7djvb_buYeSrlLUhhHRjQ6Zyx2lY-AKxqqsnfGfDNst1RSVzXz18I_RW22iAkeFRGtb4k074j6Jb6xrkQ_PyzJ84GzmBUoBArurIw9I1fk8zbd34R0Hq3tJNg51Sxltcr7Wu84eIhSImsrKnJDQIDFogZbmgRfu9Tr70rAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001796986025"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
