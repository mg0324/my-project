ssh root@hw 'rm -rf /opt/kiftd/docker-compose.yml'
scp docker-compose.yml root@hw:/opt/kiftd/
ssh root@hw 'cd /opt/kiftd && docker-compose up -d'