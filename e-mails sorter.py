def csv_importer(input_file):
	output_list = []
	f = open(input_file, 'r')
	for line in f:
		output_list.append(line.rstrip())
	f.close()
	return output_list
	
emails_list = csv_importer('emails_list.csv')
domains_list = csv_importer('domains_list.csv')

emails_list = [email for email in emails_list if not any(email.endswith(domain) for domain in domains_list)]
print(len(emails_list), emails_list)