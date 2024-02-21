# rightstufanime-discount-mailer

Mails you if anything on your public wishlist(s) is on discount.

This repository is archived due to rightstufanime shutting down their services.

## Public Archive

As October 10, 2023 rightstufanime shut down their services.

## Requirements

`requests` is used to get the website content.

`BeautifulSoup` is used to parse the content with specified values and get the important information.

You can install these packages by running

```Python
pip install -r requirements.txt
```

Python's native `email`, `smtplib` and `ssl` packages are used to send mail once all the important information has been acquired. `re` is used to validate the urls and mails.

## How it works

You have to have a public wishlist(s) with more than 1 item in it. Each time you run the script, it will check all the items on your wishlist, compare it to the price you have specified, if any of them have gone below the specified price, you'll recieve an email with all the discounted items listed, along with their link and price.

## Variables

There is a `variables.py` file with information you have to fill. I have tested the script with gmail and can't give any useful information about how to use it with other mail providers.

## App password

By default gmail doesn't allow you to log in to your mail account with email and password. You will have to create an app password for that.

How you would go about doing that is in this [link](https://help.warmupinbox.com/en/articles/4934806-configure-for-google-workplace-with-two-factor-authentication-2fa).

## Automation

You can use [cron](https://opensource.com/article/17/11/how-use-cron-linux) on Linux or Task Scheduler on Windows to automate the script running process.

For Windows, you'd have to put `python main.py` inside a `.bat` or `.ps1` file and use Task Scheduler.

I haven't used any MacOS devices but cron should be available on there as well since it's a UNIX based distro. I have even less information about BSD but I would assume it has cron or a close equivalent.

## If you couldn't get it to work

It's probably because of the urls list in `variables.py`. Here's an example of how it should look like:

```Python
urls = ["https://www.rightstufanime.com/pl/1",
        "https://www.rightstufanime.com/pl/2",
        "https://www.rightstufanime.com/pl/3"]
```
