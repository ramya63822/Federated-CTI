# Federated Machine Learning Framework for Real-Time Cyber Threat Intelligence Detection and Multi-Class Threat Response

> Final-year B.Tech project (AI & Data Science) — Team 13
> **Status: In Progress (~25% complete — data collection and preprocessing done; detection, alerting/response, and dashboard modules in development. Expected completion in ~2 months.)**

## Overview

Traditional, signature-based intrusion detection systems struggle to keep up with evolving cyber threats such as DDoS attacks, malware, phishing, and network intrusions, and often produce high false-alarm rates that require manual analysis. This project builds an intelligent, ML-based cybersecurity framework that:

- Captures live network packets and traffic in real time
- Extracts relevant network traffic features
- Uses a trained Logistic Regression model to classify traffic as **Normal**, **Neptune Attack**, or **Satan Attack**
- Generates real-time alerts on detected threats
- Logs attack details (timestamp, source IP, protocol, attack type)
- Supports automated response actions such as suspicious IP identification and blocking
- Surfaces all of this through an interactive monitoring dashboard

The goal is to bring network traffic monitoring, intrusion detection, ML-based prediction, and automated response together into a single, real-time cybersecurity framework — reducing reliance on manual incident response and static, signature-based defenses.

## Problem Statement

Static, signature-based security solutions are ineffective against unknown and evolving attack patterns. As network traffic volume grows, identifying malicious activity in real time while keeping detection accuracy high becomes harder, and delayed detection can lead to unauthorized access, data breaches, service disruption, and financial loss. This project addresses that gap with a machine learning-based detection and response framework capable of continuous monitoring, accurate classification, real-time alerting, and automated response.

## System Architecture

The system is organized into the following modules:

| Module | Responsibility |
|---|---|
| **Network Packet Capture** | Captures live packets and network traffic using Scapy |
| **Data Preprocessing & Feature Extraction** | Cleans captured data and extracts traffic features for prediction |
| **Machine Learning Detection** | Applies a trained Logistic Regression model to classify network traffic |
| **Threat Detection & Alert** | Identifies attacks and generates real-time security alerts |
| **Response & IP Blocking** | Detects suspicious IPs and supports automated response actions |
| **Logging & Reporting** | Stores attack logs, prediction results, and monitoring reports |
| **Dashboard & Visualization** | Flask/Streamlit interface for real-time monitoring and analysis |

## Tech Stack

- **Language:** Python
- **Traffic Capture:** Scapy
- **ML / Data:** Scikit-learn (Logistic Regression), Pandas, NumPy
- **Dashboard:** Flask / Streamlit
- **Model Artifact:** `model.pkl`

## Dataset & Preprocessing

The model is trained on a network intrusion dataset with traffic labeled across Normal, Neptune Attack, and Satan Attack classes. Preprocessing included:

- Missing-value analysis and imputation
- Removing constant/zero-variance columns
- Label encoding of categorical features (e.g. `last_flag`)
- Feature scaling with `StandardScaler` on key numeric traffic features (`count`, `dst_host_diff_srv_rate`, `dst_host_same_src_port_rate`, `dst_host_srv_count`, `same_srv_rate`)
- Correlation analysis to guide feature selection

## Repository Structure

```
├── notebooks/
│   └── 01_eda_preprocessing.ipynb   # Dataset loading, EDA, cleaning, encoding, scaling
├── README.md
```

> More modules (packet capture, detection pipeline, alerting/response, dashboard) will be added here as they're completed.

## My Contribution

- Built core system modules in Python — including the network packet capture logic (Scapy), feature extraction, and the Logistic Regression-based traffic classification pipeline
- Implemented data preprocessing and exploratory data analysis on the network intrusion dataset (missing values, encoding, feature scaling)
- Worked on system integration and the Flask/Streamlit dashboard, connecting detection, alerting, and the automated IP-blocking response into a single interface

## Team

| Name | Roll No. |
|---|---|
| Jesinth Kaghan | 23CU0320042 |
| Kamil M | 23CU0320044 |
| Ramya Sree S V | 23CU0320076 |
| Deepak P | 23CU032112 |

**Guide:** Ms. Abisheka Pon

## Roadmap

- [x] Dataset collection and exploratory data analysis
- [x] Data preprocessing and feature engineering
- [ ] Finalize and evaluate the Logistic Regression classification model
- [ ] Complete real-time packet capture → detection pipeline integration
- [ ] Automated alerting, logging, and IP-blocking response
- [ ] Flask/Streamlit dashboard for live monitoring
- [ ] Final testing and documentation

## Getting Started

> Setup instructions will be finalized as the build is completed. Typical flow:

```bash
git clone <repo-url>
cd <repo-name>
pip install -r requirements.txt
python app.py
```

## License

Academic project — Hindustan Institute of Science and Technology, Chennai (2023–2027).
