pipeline {
    agent any
    
    stages {
        stage("Checkout from repo and build docker image") {
            steps {
                // Source repo url
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'd299d134-829d-4813-b09d-7dbba5908def', url: 'https://github.com/Biswajit1693/CI-CD-deployment']])
                
                // Build docker image
                sh 'sudo docker build -t hello:latest .'
            }
        }
        
        stage("Push to dockerhub") {
            steps {
                // Login to Dockerhub
                withCredentials([string(credentialsId: 'docker-passwd', variable: 'dockerpssd')]) {
                sh 'sudo docker login -u jeetlinux -p ${dockerpssd}'
                    
                }
                
                // push the image to dockerhub
                sh 'sudo docker tag hello:latest jeetlinux/demo-docker:v2'
                sh 'sudo docker push jeetlinux/demo-docker:v2'
                
            }
        }
        
    }

}
