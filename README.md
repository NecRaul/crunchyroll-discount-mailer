# crunchyroll-discount-mailer

Mails you if anything on your public wishlist(s) is on discount.

## Requirements

`requests` is used to get the website content.

`BeautifulSoup` is used to parse the content with specified values and get the important information.

You can install these packages by running

```Python
pip install -r requirements.txt
```

Python's native `email`, `smtplib` and `ssl` packages are used to send mail once all the important information has been acquired. `re` is used to validate the urls and mails.

## How it works

You need to have public wishlists with at least one item in them. When you run the script, it checks all items on your wishlists and compares their prices to the specified threshold. If an item's price falls below the threshold, you'll receive an email notification with the details of the discounted items.

## Variables

There is a `variables.py` file with information you have to fill. I have tested the script with gmail and can't give any useful information about how to use it with other mail providers.

## App password

By default, Gmail doesn't allow you to log in with your email and password directly. You'll need to create an "app password" for this purpose. Instructions on how to do this can be found [here](https://help.warmupinbox.com/en/articles/4934806-configure-for-google-workplace-with-two-factor-authentication-2fa).

## Automation

You can automate the script by using system-specific scheduling tools:

- For UNIX-based operating systems, use `cron`. You can learn more about [cron](https://opensource.com/article/17/11/how-use-cron-linux).
- For Windows, create a .bat or .ps1 file containing the command python main.py and schedule it using Task Scheduler.

## If you couldn't get it to work

If you encounter issues getting the script to work, the most likely culprit is the wishlists dictionary in variables.py. Ensure it is correctly formatted, like this:

```Python
wishlists = {
    # wishlist id: price to compare to
    "id1": 10.99,
    "id2": 11.19,
    "id3": 23.49,
}
```

## How to find out my wishlist ID?

Wishlist ID is located in the URL as a query parameter, following `id=`.
Example url

```Python
https://store.crunchyroll.com/on/demandware.store/Sites-CrunchyrollUS-Site/en_US/Wishlist-ShowOthers?id=abc123
```

In this case your wishlist ID would be abc123.

### Note

This repository is built upon [rightstufanime-discount-mailer](https://github.com/NecRaul/rightstufanime-discount-mailer), which was archived because of Right Stuf Anime's acquisition by Sony/Crunchyroll.
