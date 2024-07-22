import re
text = """
Hello, my email is example@example.com. You can also reach me at test.email@domain.co.uk.
My website is https://www.example.com.
Call me at (123) 456-7890 or +1-800-555-5555.
Today's date is 2024-07-18.
"""
def find_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails
def find_urls(text):
    url_pattern = r'https?://[a-zA-Z0-9./-]+'
    urls = re.findall(url_pattern, text)
    return urls
def find_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\+\d{1,2}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers
def find_dates(text):
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    dates = re.findall(date_pattern, text)
    return dates
if __name__ == "__main__":
    print("Emails found:", find_emails(text))
    print("URLs found:", find_urls(text))
    print("Phone numbers found:", find_phone_numbers(text))
    print("Dates found:", find_dates(text))
