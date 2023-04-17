TOKA TEST

Please follow this steps in order to run this.

1. you need to clone this repo
2. add secret to your k8s named kube-config that contain the kubectl config file:

   for example: kubectl.exe create secret generic kube-config --from-file=$HOME/.kube/config_out
3. apply the helm/templates/deployment.yaml:

    for examply: kubectl apply -f helm/templates/deployment.yaml
4. after that the resti app is up and running. Now you need to do POST req like this:
    
    curl -X POST http://<EXTERNAL_IP>/connect \
     -H 'Content-Type: application/json' \
     -d '{
           "IP": "<REMOTE_HOST_IP>",
           "PORT": "<REMOTE_HOST_PORT>",
           "USERNAME": "<REMOTE_HOST_USERNAME>",
           "PASSWORD": "<REMOTE_HOST_PASSWORD>"
         }'

TBD: 
1. finish ansi playbook
2. convert to helm chart
3. Add Jenkinsfile


