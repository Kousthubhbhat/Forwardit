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
    SESSION = os.environ.get("SESSION" "BQCQGTJ-hFLv62J6QMgq5Ybe5o8CP-j6qs50PRwkAkD23uft7STryKe7a9bgxNolAIx1M-mBfR7cxpcxY2ZXSl6dmsTPoTWPwWh9m_VQ6NIhtERHj_nmZaWfgwBlif3NQTQMzazxMJMnbdkcrF2IBf2UgHOU2EvRnZ0UW5nx7MoBi_A6Q9NRb_N0e6L4Ar-xElTxDdTuUum5I3wf7YJXthpYPwKCpfvDDuRqNi9FORv5k626ZNwQzbPpQOtm64CtgPVBnjFNaWiCXbVqVmIU-SSc2LZaU1DsWtHdRT2lDBkto8Yhyac2b-cJ6I5gPp_8g2cTbUe9A4aUFLpncxBLvs3uTr70rAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001796986025"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
