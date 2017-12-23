#!/usr/bin/env python
'''
This script can be used for setting up exchange rate notifications on desktop PCs.

If you encounter error:
 No module named dbus

Then, install - sudo apt install python-dbus

Also, don't forget to install notify2 python package: 
sudo pip install notify2

'''


import sys
import logging
import requests
import argparse
import json
import notify2
import os
from time import sleep

# setup logging
logging.basicConfig(stream=sys.stdout,level = logging.ERROR)
logger = logging.getLogger(__name__)

def exchange_rates(exchange_url,proxy_dict=None):
    json_response = None

    try:
        response = requests.get(exchange_url, proxies=proxy_dict,verify=False)
        json_response = response.json()

    except Exception,exc:
        logger.error("Error while getting exchange-rate information - {}".format(exc.message),exc_info=True)
    return json_response

def setup_notification(icon_path):
    try:
        notify_instance = None
        # initialise the d-bus connection
        notify2.init("Exchange rates notifie")

        # create Notification object
        notify_instance = notify2.Notification("Exchange rate Notifier", icon = icon_path)
        
        # Set the urgency level
        notify_instance.set_urgency(notify2.URGENCY_NORMAL)
        
        # Set the timeout
        notify_instance.set_timeout(200)

    except Exception,exc:
        logger.error("Error while setting up notifications - {}".format(exc.message),exc_info=True)
 
    return notify_instance 

def show_notification(notification_instance,summary,message,icon_path):
    try:
        notification_instance.update(summary,message,icon_path)
        notification_instance.show()
    except Exception,exc:
        logger.error("Error while showing notifications - {}".format(exc.message),exc_info=True)

def cmd_arguments():

    try:
        parser = argparse.ArgumentParser("This script can be used for setting up exchange rate notifications on desktop PCs.")

        parser.add_argument('--exchange-url', required=True, help='Please specify exchange rate JSON feed url.',dest='exchange_url')
        parser.add_argument('--proxy-host', required=False, help='Please specify proxy host',dest='proxy_host')
        parser.add_argument('--proxy-port', required=False, help='Please specify proxy port',dest='proxy_port')
        parser.add_argument('--proxy-user', required=False, help='Please specify proxy user',dest='proxy_user')
        parser.add_argument('--proxy-password', required=False, help='Please specify proxy password',dest='proxy_password')
        args = parser.parse_args()
        return args

    except Exception as exc:
        logger.error("Error while getting command line arguments - %s" %exc.message,exc_info=True)


if __name__ == "__main__":
    try:
        cmd_args = cmd_arguments()

        dirname, filename = os.path.split(os.path.abspath(__file__))
        logger.debug("Directory - %s File- %s"%(dirname,filename))

        icon_file = os.path.join(os.path.sep, dirname,'currency.png')

        if not os.path.isfile(icon_file):
            logger.warning("Icon file - {} does not exists".format(icon_file))
            icon_file = None

        if cmd_args.exchange_url:
            if cmd_args.proxy_user and cmd_args.proxy_password and cmd_args.proxy_host and cmd_args.proxy_port:
                proxy_dict = {
                      'http':'http://{}:{}@{}:{}'.format(cmd_args.proxy_user,cmd_args.proxy_password,cmd_args.proxy_host,cmd_args.proxy_port),
                      'https':'http://{}:{}@{}:{}'.format(cmd_args.proxy_user,cmd_args.proxy_password,cmd_args.proxy_host,cmd_args.proxy_port),
                     }
            else:
                proxy_dict = None   
            logger.info("Proxies - {}".format(proxy_dict))
            logger.info("Getting exchange rates information")
            json_response = exchange_rates(cmd_args.exchange_url,proxy_dict)
            logger.info("Exchange rates information is retrieved successfully.")

            exchange_rates = ''

            if json_response.has_key('usd'):
                exchange_rates = exchange_rates + "1 dollar - Rs. {}".format(float(1/json_response['usd']['rate'])) + '\n'       
            if json_response.has_key('chf'):
                exchange_rates = exchange_rates + "1 CHF - Rs. {}".format(float(1/json_response['chf']['rate'])) + '\n'       
            if json_response.has_key('eur'):
                exchange_rates = exchange_rates + "1 Euro - Rs. {}".format(float(1/json_response['eur']['rate'])) + '\n'       
            if json_response.has_key('gbp'):
                exchange_rates = exchange_rates + "1 Pound - Rs. {}".format(float(1/json_response['gbp']['rate'])) + '\n'       

            logger.info("Exchange rates:\n{}".format(exchange_rates))

            notify_instance = setup_notification(icon_file)
            sleep(1) 
            #show_notification(notify_instance, "Exchange rates", "1 dollar=54 rupees", icon_file)
            
            show_notification(notify_instance, "Exchange rates", exchange_rates, icon_file)

    except Exception as exc:
        logger.error("Error while setting up exchange rate notifier - %s" %exc.message,exc_info=True)
