from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mail
import variables
import item_class


# custom sort key for books
def custom_sort_key(book):
    parts = book.name.split()
    return (parts[0], int(parts[-1]))


def create_email_message(discounted_item_list):
    plain = ""
    html = "<html>\n\t<body>"
    for item in discounted_item_list:
        plain += f"{item.name} - ${item.price}:{item.link}\n"
        html += f'\n\t\t<p><a href="{item.link}">{item.name}</a> - ${item.price}</p>'
    html += "\n\t</body>\n</html>"
    mail.send_check = True
    return [plain, html]  # plain-text and HTML version of your message


def main():
    if mail.email_check and mail.password_check:
        # setting up mail attributes for later
        message = MIMEMultipart("alternative")
        message["Subject"] = variables.email_subject
        message["From"] = variables.sender_email
        message["To"] = variables.receiver_email

        for key, value in variables.wishlists.items():
            url = f"https://store.crunchyroll.com/on/demandware.store/Sites-CrunchyrollUS-Site/en_US/Wishlist-ShowOthers?id={key}"
            if url:
                discounted_item_list = item_class.find_discounted_item(url, value)

                # if any item in any url is on sale, it will send you mail
                if len(discounted_item_list) != 0:
                    # use this if your wishlist consists of something other than books
                    sorted_items = sorted(discounted_item_list, key=lambda x: x.name)
                    # use this if your wishlist consists of books
                    # sorted_items = sorted(discounted_item_list, key=custom_sort_key)

                    message_parts = create_email_message(sorted_items)

                    # turn these into plain/html MIMEText objects
                    part1 = MIMEText(message_parts[0], "plain")
                    part2 = MIMEText(message_parts[1], "html")

                    # add HTML/plain-text parts to MIMEMultipart message
                    # the email client will try to render the last part first
                    message.attach(part1)
                    message.attach(part2)

        if mail.send_check:
            mail.send_mail(message.as_string())


if __name__ == "__main__":
    main()
