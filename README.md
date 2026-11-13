# 🛡️ Federated Quantum-Classical Framework for Real-Time Cyber Threat Detection and Multi-Class Threat Response

An intelligent cybersecurity framework integrating **Federated Learning, Quantum Machine Learning, Classical Machine Learning, and Blockchain** to detect, classify, and record network security threats.

## 📌 Overview

Cyberattacks are becoming increasingly sophisticated, making traditional intrusion detection approaches challenging to scale and adapt.

This project explores a hybrid AI-based cybersecurity framework that combines Federated Learning and Quantum Machine Learning with classical classification models to identify malicious network traffic while supporting distributed learning and secure threat logging.

The system processes network traffic datasets, applies quantum-inspired feature enhancement, performs hierarchical threat classification, and records detected intrusions on an Ethereum blockchain. It also provides email notifications to alert users about potential security threats.

## 🎯 Objectives

- Develop an intelligent network intrusion detection framework.
- Explore Federated Learning for collaborative model training across distributed clients.
- Integrate Quantum Machine Learning techniques for feature representation.
- Implement binary and multi-class threat classification.
- Identify specific attack categories from network traffic.
- Maintain tamper-evident intrusion records using blockchain.
- Generate automated email alerts for detected threats.

## 🏗️ System Architecture

The framework combines distributed learning, quantum-classical machine learning, and blockchain-based security logging.

### Overall Workflow

1. **Network Traffic Input:** Upload or stream network traffic CSV files containing CICIoT2023 network flow features.
2. **Data Preprocessing:** Apply StandardScaler and Principal Component Analysis (PCA) to transform 46 input features into four principal components.
3. **Quantum Feature Enhancement:** Use a four-qubit ZZFeatureMap and kernel-based feature processing, incorporating Nyström approximation.
4. **Threat Classification:** Apply two XGBoost classifiers for binary and multi-class threat identification.
5. **Blockchain Logging:** Generate SHA-256 hashes of detected intrusion records and submit them to an Ethereum smart contract through Web3.py.
6. **Email Notifications:** Trigger SMTP-based email alerts containing detected attack information.

### Federated Learning Component

The project also incorporates Federated Learning as part of its distributed learning approach.

Federated Learning enables participating clients to collaboratively improve a model while keeping their local training data within their respective environments.

The federated component is intended to support distributed cybersecurity intelligence without requiring direct centralization of raw network traffic.

## 🧠 Machine Learning Components

### 1. Quantum Machine Learning

The quantum feature processing pipeline includes:

- Four-qubit quantum feature mapping.
- ZZFeatureMap for quantum data encoding.
- Fidelity-based quantum kernel experimentation.
- Nyström approximation for kernel computation.

### 2. Classical Machine Learning

**XGBoost** is used for hierarchical threat classification.

| Model | Function |
|---|---|
| Binary XGBoost Classifier | Distinguishes normal traffic from malicious traffic. |
| Multi-Class XGBoost Classifier | Identifies the specific attack category among 12 classes. |

### 3. Federated Learning

The federated learning component supports collaborative learning across distributed environments while keeping raw network traffic data local.

## 🔗 Blockchain Integration

The framework incorporates Ethereum-based blockchain logging to maintain tamper-evident intrusion records.

**Implementation components:**
- SHA-256 hashing
- Ethereum smart contracts
- Web3.py
- Ganache (development environment, where configured)

Detected intrusion information is hashed and submitted to the smart contract, providing a verifiable record of logged security events.

## 📊 Experimental Results

The available project presentation records the following result:

| Metric | Result |
|---|---:|
| Binary Classification Test Accuracy | 98.4775% |
| Input Network Features | 46 |
| PCA Components | 4 |
| Quantum Feature Map | 4 Qubits |
| Multi-Class Attack Categories | 12 |

**Note:** The reported accuracy refers to the recorded binary classification experiment. It should not be interpreted as the independently verified performance of the complete federated quantum-classical pipeline.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | XGBoost, Scikit-learn |
| Quantum Computing | Qiskit / Quantum Computing Framework |
| Quantum Feature Mapping | ZZFeatureMap |
| Kernel Methods | Fidelity Kernel, Nyström Approximation |
| Data Processing | Pandas, NumPy |
| Dimensionality Reduction | PCA |
| Blockchain | Ethereum, Solidity |
| Blockchain Integration | Web3.py |
| Smart Contract Testing | Ganache |
| Notifications | SMTP |
| Dataset | CICIoT2023 |
| Development | Jupyter Notebook |

## 📂 Project Structure

```text
Federated-Cyber-Threat-Detection/
│
├── backend/
│   ├── preprocessing/
│   ├── quantum/
│   ├── federated/
│   ├── models/
│   └── blockchain/
│
├── frontend/
│
├── datasets/
│
├── notebooks/
│
├── smart_contracts/
│
├── models/
│
├── requirements.txt
│
└── README.md
```

*The directory structure above is a suggested organizational layout. Adapt it to match the actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Federated-Cyber-Threat-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configure the required application settings, including:

- Blockchain RPC endpoint.
- Smart contract address.
- Contract ABI.
- SMTP server credentials.

Never commit API keys, private keys, passwords, or other sensitive credentials to GitHub.

### 5. Run the Application

Use the entry-point command corresponding to the actual backend and frontend implementation.

## 🔬 Research Significance

This project explores the intersection of:

- Privacy-aware distributed machine learning.
- Quantum-enhanced feature representation.
- Hybrid quantum-classical classification.
- Multi-class cybersecurity threat detection.
- Blockchain-based security auditing.

The integration aims to investigate how these technologies can contribute to intelligent and distributed cybersecurity monitoring systems.

## 🚀 Future Enhancements

- Evaluate federated aggregation strategies across heterogeneous clients.
- Compare centralized and federated model performance.
- Investigate quantum and classical feature representations under identical experimental conditions.
- Improve performance on imbalanced network traffic datasets.
- Evaluate detection latency and computational overhead.
- Expand real-time threat monitoring and automated response capabilities.
- Explore deployment on distributed edge environments.

## 👩‍💻 Project Information

**Domain:** Artificial Intelligence | Quantum Machine Learning | Federated Learning | Cybersecurity | Blockchain

**Dataset:** CICIoT2023

**Project Type:** Hybrid AI-Based Cybersecurity Research and Implementation

---

*Developed as an exploration of Federated Learning and Quantum-Classical Machine Learning for intelligent cyber threat detection and response.*
