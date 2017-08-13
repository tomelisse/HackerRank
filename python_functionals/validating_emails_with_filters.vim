def is_valid(mail):
    at  = mail.find('@')
    dot = mail.find('.')
    if at == -1 or dot == -1 or at > dot:
	return False
    username    = mail[:at]
    websitename = mail[at+1:dot]
    extension   = mail[dot+1:]
    username = username.replace('-','a')
    username = username.replace('_','a')
    if username.isalnum() and websitename.isalnum() and len(extension) <= 3:
	return True
    return False

def filter_mail(emails):
    return list(filter(is_valid, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
	emails.append(input())

				filtered_emails = filter_mail(emails)
				filtered_emails.sort()
				print(filtered_emails)
