# Federated Unlearning for IoT Networks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)

## 📌 Overview

This repository implements **Federated Unlearning (Désapprentissage Fédéré)** specifically tailored for resource-constrained **IoT (Internet of Things)** environments. 

> **Federated Unlearning**: The process of removing a specific client's data influence from a global trained model in a federated setting without retraining from scratch.  
> *Français : Le processus de suppression de l'influence des données d'un client spécifique d'un modèle global entraîné, sans tout réentraîner.*

In decentralized networks, the "right to be forgotten" is a critical privacy requirement. This project evaluates model performance, **Fairness (Équité)**, and privacy resilience against **Membership Inference Attacks (MIA)**.

## ✨ Key Features

* **Efficient Unlearning**: Implementation of algorithms optimized for IoT devices with limited compute/battery.
* **Privacy Auditing**: Integrated **Membership Inference Attack (MIA)** to verify if the client's data has been effectively forgotten.
    * **MIA**: A security threat where an attacker determines if a specific record was part of the training set.  
    * *Français : Une menace où un attaquant détermine si un enregistrement spécifique faisait partie de l'ensemble d'entraînement.*
* **Fairness Metrics**: Ensures that the removal of one client does not negatively impact the model's performance for other minority groups.
    * **Fairness**: The practice of ensuring that AI model predictions are unbiased and do not discriminate.  
    * *Français : La pratique consistant à s'assurer que les prédictions du modèle ne sont pas biaisées.*
* **Scalable Architecture**: Based on a central server managing `FedAvg` and local clients using `PyTorch`.

## 🏗️ Architecture

The project follows a client-server architecture:
1.  **Federated Learning**: Initial training phase using `FedAvg`.
2.  **Unlearning Request**: A specific IoT node requests data removal.
3.  **Correction Phase**: The server applies unlearning (e.g., via gradient subtraction or fine-tuning on remaining data).
4.  **Verification**: Running MIA benchmarks and accuracy checks.

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* PyTorch / Torchvision
* Scikit-learn

### Installation
```bash
git clone [https://github.com/votre-username/Federated-Unlearning-for-IoT-Networks.git](https://github.com/votre-username/Federated-Unlearning-for-IoT-Networks.git)
cd Federated-Unlearning-for-IoT-Networks
pip install -r requirements.txt
