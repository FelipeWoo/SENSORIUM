# ====================
# Sensorium Project Makefile
# ====================

# ---------- Docker ----------
server-up:
	@echo "🚀 Levantando servicios..."
	@docker compose up -d

server-down:
	@echo "🛑 Apagando servicios..."
	@docker compose down

server-logs:
	@echo "📜 Logs de todos los servicios..."
	@docker compose logs -f

mqtt-logs:
	@echo "📡 Logs de Mosquitto..."
	@docker compose logs -f mqtt

db-logs:
	@echo "🗃️ Logs de PostgreSQL..."
	@docker compose logs -f postgres

# ---------- Utilidades ----------
mqtt-shell:
	@docker exec -it sensorium_mqtt sh

db-shell:
	@docker exec -it sensorium_db bash

# ---------- MQTT Tools ----------
mqtt-sub:
	@mosquitto_sub -h localhost -p 1883 -u $$MQTT_USERNAME -P $$MQTT_PASSWORD -t "#" -v

mqtt-pub:
	@mosquitto_pub -h localhost -p 1883 -u $$MQTT_USERNAME -P $$MQTT_PASSWORD -t "test/topic" -m "Hello from Makefile"

# ---------- Inicialización ----------
init-mqtt-user:
	@bash scripts/init_mqtt_user.sh

# ---------- Atajo para todo ----------
reset:
	@docker compose down -v
	@docker compose up -d --build

