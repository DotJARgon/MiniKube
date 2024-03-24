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

## Starting FastAPI Server

1. **Before execution, ensure credentials for your database environment are correct in "Minikube/apiRest/databaseConfig.py"**

2. **Execute from root directory**:

```bash
python -m uvicorn apiRest.main:app --reload
```

3. **This will launch server at http://127.0.0.1:8000**
4. **Go to http://127.0.0.1:8000/docs for all GET calls for testing**
=======
## Create Minikube instance of the nextJS server

1. **set up docker correctly**
```bash
docker context use default
```

2. **from root directory of project**
```bash
cd nextjs/frontend
```

3. **create docker image**
```bash
docker build -t frontend .
```

4. **make docker image accessible to minikube**
```bash
minikube image load frontend
```

5. **create deployment**
```bash
kubectl apply -f nextjs-deployment.yaml
```

6. **create service**
```bash
kubectl apply -f nextjs-service.yaml
```

7. **run the following to be able to access the pod instance**
```bash
minikube service nextjs-app-service --url
```

