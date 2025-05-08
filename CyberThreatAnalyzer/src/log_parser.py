import json
import csv
import os

def parse_logs(log_dir, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'src_ip', 'dst_port', 'event']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for filename in os.listdir(log_dir):
            if filename.endswith('.json'):
                with open(os.path.join(log_dir, filename), 'r') as f:
                    data = json.load(f)
                    writer.writerow(data)

if __name__ == "__main__":
    parse_logs("../logs", "../processed/parsed_logs.csv")
