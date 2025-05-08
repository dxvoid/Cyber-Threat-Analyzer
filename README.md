# CyberThreat Analyzer Pro (Offline Edition)

## Overview
An offline SIEM dashboard solution that simulates log collection and integrates static threat intelligence to visualize and report security events using Power BI.

## Components
- Simulated logs (Windows & Linux)
- Static threat intelligence (CSV)
- Python scripts for parsing and correlation
- Power BI dashboard placeholder
- Ready for offline demo without any API calls

## How to Run
1. Run `log_parser.py` to parse JSON logs into CSV.
2. Run `threat_correlator.py` to enrich logs with threat intel.
3. Import the resulting `correlated_logs.csv` into Power BI for visualization.

