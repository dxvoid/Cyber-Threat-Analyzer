import csv

def correlate_threats(log_file, threat_db_file, output_file):
    malicious_ips = set()
    with open(threat_db_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            malicious_ips.add(row['ip_address'])
    
    with open(log_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['threat_detected']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if row['src_ip'] in malicious_ips:
                row['threat_detected'] = 'Yes'
            else:
                row['threat_detected'] = 'No'
            writer.writerow(row)

if __name__ == "__main__":
    correlate_threats("../processed/parsed_logs.csv", "../threat_db/malicious_ips.csv", "../processed/correlated_logs.csv")
