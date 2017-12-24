# Currency-notifier
Desktop notification of exchange rates for Indian rupees vis-a`-vis other currencies like Dollar, Swiss Franks, Euro etc.

## Use of desktop notifications
There are many instances where-in you wish that computer notify you about the issues that may not need immediate response. You just need to aware of the events -  currency fluatations, latest software updates available, minutes of battery charging left and so on. Such events should be presented in an alert box or some other window. Desktop notification is the most appropriate way to handle such events.

## How to run
### Behind proxy
```sh
$ python currency-notifier.py --exchange-url http://www.floatrates.com/daily/inr.json --proxy-host=10.1.1.2 --proxy-port=8080 --proxy-user=xxx --proxy-password=xxxx
```
### Without proxy
```sh
$ python currency-notifier.py --exchange-url http://www.floatrates.com/daily/inr.json
```
## Thanks
Thanks to site - http://www.floatrates.com/daily/inr.json for providing currency related JSON feed

I wrote this script after reading the article:
https://www.codementor.io/dushyantbgs/building-a-desktop-notification-tool-using-python-bcpya9cwh
