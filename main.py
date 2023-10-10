import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import variables
import item_class
import mail

def url_check(url):
    pattern = r"^https?://(www\.)?store\.crunchyroll\.com/on/demandware\.store/Sites-CrunchyrollUS-Site/en_US/Wishlist-ShowOthers\?id=[a-zA-Z0-9]+$"
    return re.match(pattern, url) is not False
    
def process_url(url):
    # checking if the url is valid
    is_valid_url = url_check(url)
    
    # adding https:// to the start of the string if url is not valid
    url = f"https://{url}" if not is_valid_url else url
    
    # checking if the url is valid again
    is_valid_url = url_check(url)
    
    if (not is_valid_url):
        print("URL", url, "is not a Crunchyroll public wishlist.")
        return None
    else:
        return url

# custom sort key for books
def custom_sort_key(book):
    parts = book.name.split()
    return (parts[0], int(parts[-1]))
        
def create_email_message(item_array):
    plain = ""
    html = "<html>\n\t<body>"
    for item in item_array:
        plain += f"{item.name} - ${item.price}:{item.link}\n"
        html += f"\n\t\t<p><a href=\"{item.link}\">{item.name}</a> - ${item.price}</p>"
    html += "\n\t</body>\n</html>"
    mail.send_check = True
    return [plain, html] # plain-text and HTML version of your message

def main():
    if (mail.email_check and mail.password_check):
        # setting up mail attributes for later
        message = MIMEMultipart("alternative")
        message["Subject"] = variables.email_subject
        message["From"] = variables.sender_email
        message["To"] = variables.receiver_email
        
        for key, value in variables.dict.items():
            url = process_url(key) if process_url(key) else None
            if (url):
                item_array = item_class.find_discounted_item(url, value)
                    
                if len(item_array) != 0: # if any item in any url is on sale, it will send you mail
                    
                    # uncomment/use this if your wishlist consists of something other than books
                    sorted_items = sorted(item_array, key=lambda x: x.name)
                    
                    # uncomment/use this if your wishlist consists of books
                    # sorted_items = sorted(item_array, key=custom_sort_key)
                    
                    message_parts = create_email_message(sorted_items)

                    # turn these into plain/html MIMEText objects
                    part1 = MIMEText(message_parts[0], "plain")
                    part2 = MIMEText(message_parts[1], "html")

                    # add HTML/plain-text parts to MIMEMultipart message
                    # the email client will try to render the last part first
                    message.attach(part1)
                    message.attach(part2)

        if (mail.send_check):
            mail.send_mail(message.as_string())

if __name__ == "__main__":
    main()