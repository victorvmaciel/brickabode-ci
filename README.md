### Features: Continuous Integration

- Update all python libraries for the application.;
- Build a docker image with the application;
- CI job running CVE scans on the python libraries using snyk to scan the docker image;
- CI job that only runs on master branch
- CI job building a docker image using a dockerfile and pushing to dockerhub docker register.;

### Features: Continuous Deployment

- Repository continuous deployment implemented;
- Every time a new image is built it also deploy on the production environment;
- Every time that new code is merged on master, the CD pipeline is trigged.
- The application is deployed on a EC2 AWS instance that is connected to a nginx reverse proxy;
- The application has a DNS record and answer on the following address: [DNS](http://brickabode-ci-test.cloudns.ph "DNS");

# Brick Abode CI / CD test

![](https://media-exp1.licdn.com/dms/image/C4E0BAQFhRHi0tefe1g/company-logo_200_200/0/1616162207405?e=2159024400&v=beta&t=-TM6rxWwtyTPSmsjlRpU4t5ctGTZpoaB3BEQWe9dhyU)



## Gitlab CI .yml file
### stages
Each stage is part of a pipeline and do a specifical task. They are **build**, **test** and **deploy**. If some new code is commited and pulled to the main branch, it will automatically activate all steps bellow.

#### Build ``build-docker``
Build is the first stage on pipeline, it is responsible for build the docker image based on the repository's Dockerfile. It uses a service called docker:dind or "docker in docker" that uses a gilab's docker engine to login on docker hub, build the app image (using the python image as base). it will build a image doing these steps:
 - Pull the docker with the python 3.8 image from dockerhub;
 - Copy all application code from the current repository to the image;
 - Update the python libraries;
 - Build all the dependency files with pip install;
 - Expose the app on 5000 http port;
 - Finally, the Dockerfile is pulled to https://hub.docker.com/repository/docker/victorvmaciel/a-simple-note-taking-web-app;

![](https://i.ibb.co/wN07Mzs/build-docker-hub.png)

	ubuntu@ip-172-31-21-29:~$ docker images
	REPOSITORY 					TAG                             IMAGE ID  						CREATED       SIZE
	victorvmaciel/a-simple-note-taking-web-app   latest    b85a78b7a6b0   7 hours ago   957MB

#### Test ``test-project``

After build the image and pull to dockerhub, the next stage is to test the docker image integrity  with Snyk, a developer security platform for securing code, dependencies, containers, and infrastructure as code. Snyk it is executed through a shell script using the gitlab-runner.


![](https://i.ibb.co/pdZhfkx/Dockerhub-Snyk-Feature.jpg)

##### Synk results example:


```
Project name:      docker-image|victorvmaciel/a-simple-note-taking-web-app
Docker image:      victorvmaciel/a-simple-note-taking-web-app:latest
Platform:          linux/amd64
Base image:        python:3.8.12-bullseye
Licenses:          enabled
Tested 427 dependencies for known issues, found 171 issues.
Base Image              Vulnerabilities  Severity
python:3.8.12-bullseye  171              6 critical, 6 high, 27 medium, 132 low
Recommendations for base image upgrade:
Alternative image types
Base Image                   Vulnerabilities  Severity
python:3.10-slim             37               1 critical, 0 high, 1 medium, 35 low
python:3.11-rc-slim          37               1 critical, 0 high, 1 medium, 35 low
python:3.8.12-slim-bullseye  37               1 critical, 0 high, 1 medium, 35 low
python:3.8-slim-buster       70               2 critical, 9 high, 9 medium, 50 low
```

#### Deploy ``deploy-project``

The final step will deploy the application on a AWS EC2 Instance using a gilab-runner to execute shell commands to:
- Certify if there is a good environment for pull a new image, by cleaning the dangling images;
- Stop any container to avoid erros on running a new one;
- Pull the image build on CI build-step;
- Run a container to publish the app on the **5000** http port;

```
      $ ubuntu@ip-172-31-21-29:~$ docker ps --format "{{.Names}}\t{{.Ports}}"
      a-simple-note-taking-web-app	0.0.0.0:5000->5000/tcp, :::5000->5000/tcp
```

## Cloud environment
### AWS EC2

It was created two EC2 Amazon Web Services instances to:
- Provide de application;
- Provide Nginx;

![](https://i.ibb.co/FXdtKBR/aws-instances.png)
The instance named **app**, it will serve the application on 5000 por but this one it is exclusively exposed to the another instance named **nginx** trhough the VPC internal network on Amazon Web Services Cloud.
```
root@ip-172-31-26-36:/etc/nginx/sites-available# cat brickabode-ci-test.cloudns.ph | grep proxy_redirect
proxy_redirect		 http://172.31.21.29:5000 http://3.80.71.22;
```
The another instance, named nginx, expose the 80 http port to the public, as example below.

![](https://i.ibb.co/fYBNn7D/ngix-result.png)

## DNS

### ClouDNS

The DNS server name chosen was the [ClouDNS](https://www.cloudns.net/ "ClouDNS") . It provides a free DNS to use a Type A and point it name to a external IP provided from AWS.

The Domain Name	 was: named brickabode-ci-test.cloudns.ph witch is availbe [here](http://brickabode-ci-test.cloudns.ph/ "here")

![](https://i.ibb.co/DGDZRps/dns-brickabode-app.png)
