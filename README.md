# Software Project Management

...

## Create Minikube instance of the mysql server


1. **Start from root directory**:

```bash
cd mysql
```

2. **Start/create persistent volume**

```bash
kubectl apply -f mysql-pv.yaml
```

3. **Start/create persistent volume claim**
```bash
kubectl apply -f mysql-pvc.yaml
```

4. **Start/create deployment**
```bash
kubectl apply -f mysql-deployment.yaml
```

5. **Start/create service**
```bash
kubectl apply -f mysql-service.yaml
```

**access mysql database through commandline**
```bash
kubectl run -it --rm --image=mysql:8.0 --restart=Never mysql-client -- mysql -h mysql --password="password"
```

## Create Minikube instance of the nextJS server

1. set up docker correctly
```bash
docker context use default
```

2. from root directory of project
```bash
cd nextjs/frontend
```

3. create docker image
```bash
docker build -t frontend .
```

4. make docker image accessible to minikube
```bash
minikube image load frontend
```

5. create deployment
```bash
kubectl apply -f nextjs-deployment.yaml
```

6. create service
```bash
kubectl apply -f nextjs-service.yaml
```

7. run the following to be able to access the pod instance
```bash
minikube service nextjs-app-service --url
```

