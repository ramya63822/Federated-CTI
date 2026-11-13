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
- Ethereum smart contracts (`Intrusion.sol`)
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
| Web Framework & Database | Flask, SQLite |
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
Federated-CTI/
│
├── blockchain/
│   ├── blockchain.py                   # Web3.py smart contract interaction
│   └── contract/
│       └── Intrusion.sol               # Solidity smart contract for intrusion logging
│
├── datasets/
│   ├── simulation/                     # Real-time traffic simulation CSVs (sim_1 - sim_5)
│   └── upload/                         # Sample traffic upload CSVs (sample_1 - sample_5)
│
├── notebooks/
│   └── 01_eda_preprocessing.ipynb      # Exploratory data analysis & preprocessing
│
├── routes/
│   ├── auth.py                         # User authentication routes
│   ├── blocked_ips.py                  # Automated IP blocking management
│   ├── ledger.py                       # Blockchain audit ledger views
│   ├── monitor.py                      # Real-time traffic monitoring routes
│   ├── reports.py                      # CSV security report generation
│   ├── settings.py                     # System configuration routes
│   └── upload.py                       # Traffic CSV upload endpoints
│
├── services/
│   ├── alert_service.py                # SMTP email alerting service
│   ├── ip_service.py                   # Threat IP tracking & blocking logic
│   └── ml_service.py                   # Quantum-classical inference pipeline
│
├── static/
│   ├── reports/                        # Generated threat reports
│   └── uploads/                        # Uploaded traffic files
│
├── templates/
│   ├── components/                     # Navbar, sidebar, and alert popups
│   ├── partials/                       # Dashboard sub-views (ledger, monitoring, stats, etc.)
│   ├── dashboard.html                  # Main security monitoring dashboard
│   ├── index.html                      # Landing page
│   ├── login.html                      # Login page
│   └── signup.html                     # Registration page
│
├── utils/
│   └── database.py                     # SQLite database helpers
│
├── app.py                              # Flask application entry point
├── config.py                           # Application configuration
├── dataset.py                          # Dataset handling utilities
├── deploy.py                           # Smart contract deployment script
├── verify.py                           # Verification utilities
├── QML.ipynb                           # Quantum Machine Learning experiments
├── binary_model.pkl                    # Trained binary XGBoost classifier
├── multi_model.pkl                     # Trained multi-class XGBoost classifier
├── label_encoder.pkl                   # Target label encoder
├── model_metrics.pkl                   # Saved evaluation metrics
├── pca_quantum_reducer.pkl             # PCA dimensionality reducer
├── quantum_feature_transformer.pkl     # Quantum feature map transformer
├── scaler_standard.pkl                 # StandardScaler artifact
├── requirements.txt                    # Python dependencies
├── setup.bat                           # Windows setup script
├── setup_instructions.md               # Detailed setup guide
├── How_to_run.txt                      # Quick run instructions
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com
cd Federated-CTI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell)**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**
```cmd
venv\Scripts\activate.bat
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables & Blockchain

Update your settings in `config.py` (or environment variables) with:

- Ethereum / Ganache RPC endpoint.
- Deployed smart contract address (`Intrusion.sol`) and ABI.
- SMTP server credentials for automated email alerts.

*(Note: Never commit private keys, passwords, or sensitive credentials to GitHub.)*

### 5. Deploy Smart Contract & Run the Application

1. Deploy the smart contract (if running locally with Ganache):
   ```bash
   python deploy.py
   ```
2. Start the Flask dashboard:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to http://127.0.0.1:5000.

🔬 Research Significance

This project explores the intersection of:
• Privacy-aware distributed machine learning.
• Quantum-enhanced feature representation.
• Hybrid quantum-classical classification.
• Multi-class cybersecurity threat detection.
• Blockchain-based security auditing.
The integration aims to investigate how these technologies can contribute to intelligent and distributed cybersecurity monitoring systems.

🚀 Future Enhancements

• Evaluate federated aggregation strategies across heterogeneous clients.
• Compare centralized and federated model performance.
• Investigate quantum and classical feature representations under identical experimental conditions.
• Improve performance on imbalanced network traffic datasets.
• Evaluate detection latency and computational overhead.
• Expand real-time threat monitoring and automated response capabilities.
• Explore deployment on distributed edge environments.

👩‍💻 Project Information

Domain: Artificial Intelligence | Quantum Machine Learning | Federated Learning | Cybersecurity | Blockchain
Dataset: CICIoT2023
Project Type: Hybrid AI-Based Cybersecurity Research and Implementation