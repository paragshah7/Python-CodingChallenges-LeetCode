"""
Input - ['3 bbs.vmware.com', '4 work.google.com']

Output - list of domains and visit times

3 bbs.vmware.com
3 vmware.com
7 com
4 work.google.com
4 google.com

"""

def count_domain(domains):
    output = []
    seen_domains = {}

    for domain in domains:
        # print(domain)
        count_each = domain.split()
        number = int(count_each[0])

        each_domain = count_each[1].split('.')
        len_domain = len(each_domain)
        individual_domain = None

        for d in range(len_domain-1,-1,-1):
            if individual_domain is None:
                individual_domain = each_domain[d]
            else:
                individual_domain = '{}.{}'.format(each_domain[d],individual_domain)

            if individual_domain not in seen_domains:
                seen_domains[individual_domain] = number
            else:
                number_all_domain = number + seen_domains[individual_domain]
                seen_domains[individual_domain] = number_all_domain

    for domain, number in seen_domains.items():
        output.append('{} {}'.format(number, domain))

    return output


domain_list = ['3 bbs.vmware.com', '4 work.google.com', '5 work.facebook.com', '10 apple.com']
print(count_domain(domain_list))
