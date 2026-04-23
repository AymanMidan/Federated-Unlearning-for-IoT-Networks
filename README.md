# Federated Unlearning for IoT Networks
📌 Overview
This repository implements Federated Unlearning (Désapprentissage Fédéré) specifically tailored for resource-constrained IoT (Internet of Things) environments.

Federated Unlearning: The process of removing a specific client's data influence from a global trained model in a federated setting without retraining from scratch.
Français : Le processus de suppression de l'influence des données d'un client spécifique d'un modèle global entraîné, sans tout réentraîner.

In decentralized networks, the "right to be forgotten" is a critical privacy requirement. This project evaluates model performance, Fairness (Équité), and privacy resilience against Membership Inference Attacks (MIA).

✨ Key Features
Efficient Unlearning: Implementation of algorithms optimized for IoT devices with limited compute/battery.

Privacy Auditing: Integrated Membership Inference Attack (MIA) to verify if the client's data has been effectively forgotten.

MIA: A security threat where an attacker determines if a specific record was part of the training set. (Français : Une menace où un attaquant détermine si un enregistrement spécifique faisait partie de l'ensemble d'entraînement.)

Fairness Metrics: Ensures that the removal of one client does not negatively impact the model's performance for other minority groups.

Fairness: The practice of ensuring that AI model predictions are unbiased and do not discriminate. (Français : La pratique consistant à s'assurer que les prédictions ne sont pas biaisées.)

Scalable Architecture: Based on a central server managing FedAvg and local clients using PyTorch.

🏗️ Architecture
The project follows a client-server architecture:

Federated Learning: Initial training phase using FedAvg.

Unlearning Request: A specific IoT node requests data removal.

Correction Phase: The server applies unlearning (e.g., via gradient subtraction or fine-tuning on remaining data).

Verification: Running MIA benchmarks and accuracy checks.
