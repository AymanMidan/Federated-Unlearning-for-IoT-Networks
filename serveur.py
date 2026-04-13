import paho.mqtt.client as mqtt
import torch
import torch.nn as nn
import pickle

# ====== CONFIG ======
NOMBRE_MAX_CLIENTS = 3

# ====== MODELE GLOBAL ======
model_global = nn.Linear(30, 1)

clients_poids_recus = []
clients_counts_recus = []

# ====== FEDAVG ======
def fed_avg(weights_list, samples_count_list):
    n_total = sum(samples_count_list)
    global_weights = {}

    ref = weights_list[0]
    for k in ref.keys():
        global_weights[k] = torch.zeros_like(ref[k])

    for i in range(len(weights_list)):
        importance = samples_count_list[i] / n_total
        for k in weights_list[i].keys():
            global_weights[k] += weights_list[i][k] * importance

    return global_weights


# ====== RECEPTION ======
def on_message(client, userdata, msg):
    global model_global

    print("Message reçu !")

    packet = pickle.loads(msg.payload)
    poids = packet["weights"]
    n = packet["n_samples"]

    clients_poids_recus.append(poids)
    clients_counts_recus.append(n)

    print(f"Progression : {len(clients_poids_recus)}/{NOMBRE_MAX_CLIENTS}")

    if len(clients_poids_recus) == NOMBRE_MAX_CLIENTS:
        print("FedAvg en cours...")

        new_weights = fed_avg(clients_poids_recus, clients_counts_recus)

        # update modèle global
        model_global.load_state_dict(new_weights)

        print("Modèle global mis à jour !")

        # renvoyer aux clients
        message = pickle.dumps({
            "weights": model_global.state_dict()
        })

        serveur.publish("fl/model/down", message)
        print("Modèle envoyé aux clients !")

        clients_poids_recus.clear()
        clients_counts_recus.clear()


# ====== MQTT ======
serveur = mqtt.Client()
serveur.on_message = on_message

serveur.connect("localhost", 1883, 60)
serveur.subscribe("fl/model/up")

print("Serveur en écoute...")

# envoyer modèle initial
init_message = pickle.dumps({
    "weights": model_global.state_dict()
})
serveur.publish("fl/model/down", init_message)
print("Modèle initial envoyé !")

serveur.loop_forever()
