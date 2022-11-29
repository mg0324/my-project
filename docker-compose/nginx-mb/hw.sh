ssh root@hw 'rm -rf /opt/mb/docker-compose.yml'
scp docker-compose.yml root@hw:/opt/mb/
ssh root@hw 'cd /opt/mb && docker-compose up -d'