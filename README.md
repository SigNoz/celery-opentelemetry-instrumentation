make sure you have docker desktop
to avoid conflict...
containers > delete all
images > delete all
volumes > delete all
terminal >> docker system prune

---

RUN

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

docker-compose up --build
or
docker-compose up --build -d

---

[browser]
http://localhost:15672
guest, guest

---

[new terminal]
docker-compose logs -f otel-collector

---

[new terminal]
(you will find container id from docker app)
docker exec -it <celery_worker_container_id> python

just copy these lines, and keep pressing cmd+v multiple times in opened python shell

from app.tasks import add
add.delay(4, 6)
