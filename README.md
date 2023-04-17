TOKA TEST

Please follow this steps in order to run this.

1. you need to clone this repo
2. add secret to your k8s named kube-config that contain the kubectl config file:

   for example: kubectl.exe create secret generic kube-config --from-file=$HOME/.kube/config_out
3. apply the helm/templates/deployment.yaml:

    for examply: kubectl apply -f helm/templates/deployment.yaml

TBD: 
1. finish ansi playbook
2. convert to helm chart


