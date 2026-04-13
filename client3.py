import paho.mqtt.client as mqtt
import torch
import torch.nn as nn
import torch.optim as optim
import pickle

# ====== CHARGER DATA ======
X, y = pickle.load(open("client3.pkl", "rb"))

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).view(-1, 1)

# ====== MODELE ======
model = nn.Linear(30, 1)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# ====== RECEPTION MODELE ======
def on_message(client, userdata, msg):
    print("Modèle reçu du serveur !")

    packet = pickle.loads(msg.payload)
    model.load_state_dict(packet["weights"])

    # ====== TRAIN LOCAL ======
    for epoch in range(5):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

    print("Training terminé !")

    # ====== ENVOI AU SERVEUR ======
    message = pickle.dumps({
        "weights": model.state_dict(),
        "n_samples": len(X)
    })

    client.publish("fl/model/up", message)
    print("Poids envoyés !")


# ====== MQTT ======
client = mqtt.Client()
client.on_message = on_message

client.connect("192.168.1.10", 1883, 60)  # IP serveur
client.subscribe("fl/model/down")

print("Client en attente du modèle...")

client.loop_forever()
