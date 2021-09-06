"""
https://leetcode.com/problems/unique-email-addresses/
"""

def num_unique_emails(emails):

    email_set = set()

    for email in emails:
        unique_email = ''
        name, domain = email.split('@')

        for e in name:
            if e == '.':
                continue
            elif e == '+':
                break
            unique_email += e
        unique_email = unique_email + '@' + domain

        if unique_email not in email_set:
            email_set.add(unique_email)

    # print(email_set)
    return len(email_set)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(num_unique_emails(emails))
