# python-openshift-mongo
Python + Flask + Mongo for OpenShift

#Clone

git@github.com:alairjt/python-openshift-mongo.git

#Install dependencies

./bootstrap

#Check MongoDB config in app/__init__.py

mongodb://localhost:27017

#Run after install MongoDB

/installpath/MongoDB/Server/3.0/bin/mongod.exe --dbpath "/path/mongodata/"

#Run local

./run

#Add to OpenShift

Sign in to OpenShift

Create new app

Python 3.3

Configure app
    - If you provide a Git URL:
        - Ex.: https://github.com/alairjt/python-openshift-mongo.git (Don't use git@github.com)
        - It's necessary add public key. (Settings -> Add new key)
        - Your application will start with an exact copy of the code and configuration provided in this Git repository.


Create application

########
Making code changes
Install the Git client for your operating system, and from your command line run

git clone ssh://xxxxx@appname-domain.rhcloud.com/~/git/appname.git/
cd appname/
This will create a folder with the source code of your application. After making a change, add, commit, and push your changes.

git add .
git commit -m 'My changes'
git push

When you push changes the OpenShift server will report back its status on deploying your code. The server will run any of your configured deploy hooks and then restart the application.
########


#### ADD MONGODB

Applications

Edit app

## Databases

Add MongoDB X.X

Add Cartidgre

########
MongoDB 2.4 database added.  Please make note of these credentials:

   Root User:     admin
   Root Password: XXXXXXXXXX
   Database Name: appname

Connection URL: mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT/
########

## Connect to ssh (ssh XXXXXXXXXXXXXXX@appname-domain.rhcloud.com)

echo $OPENSHIFT_MONGODB_DB_HOST
> 127.6.16.XXX

echo $OPENSHIFT_MONGODB_DB_PORT
> 27017


## Change in app/__init__py

From: uri = "mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT"
To: uri = "mongodb://127.6.16.XXX:27017"

Check database name and authenticate params.




