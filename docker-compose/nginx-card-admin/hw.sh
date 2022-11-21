ssh root@hw 'rm -rf /opt/docker-compose.yml'
scp docker-compose.yml root@hw:/opt
ssh root@hw 'cd /opt && docker-compose up -d'