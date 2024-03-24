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
