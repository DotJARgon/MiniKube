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

**how access mysql database through minikube pod**
```bash
kubectl run -it --rm --image=mysql:8.0 --restart=Never mysql-client -- mysql -h mysql --password="password"
```

## Upload sakila data

1. **access mysql database through minikube pod!!!**
```bash
kubectl run -it --rm --image=mysql:8.0 --restart=Never mysql-client -- mysql -h mysql --password="password"
```

2. **in minikube mysql, add localhost user**
```mysql
GRANT ALL PRIVILEGES ON *. * TO 'root'@'127.0.0.1' WITH GRANT OPTION;
```

3. **on local machine, log into mysql**
```bash
mysql -uroot -p
```

4. **upload schema on local mysql**
```mysql
SOURCE PATH/TO/sakila-schema.sql
```

5. **upload data on local mysql**
```mysql
SOURCE PATH/TO/sakila-data.sql
```

6. **port forward mysql**
```bash
kubectl port-forward mysql-pod-name 3306:3306
```

