ssh root@hw 'rm -rf /opt/flask-todolist/docker-compose.yml'
scp docker-compose.yml root@hw:/opt/flask-todolist/
ssh root@hw 'cd /opt/flask-todolist && docker-compose up -d'