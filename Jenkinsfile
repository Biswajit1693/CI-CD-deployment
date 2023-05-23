pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Biswajit1693/CI-CD-deployment'
      }
    }

    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python setup.py build'
      }
    }

    stage('Test') {
      steps {
        sh 'python -m unittest discover'
      }
    }

    stage('Docker Build') {
      steps {
        script {
          def dockerImage = docker.build('pythonapp:latest')
          docker.withRegistry('https://hub.docker.com/', 'docker-hub') {
            dockerImage.push()
          }
        }
      }
    }

    stage('Minikube Deploy') {
      steps {
        kubernetesDeploy(
          configs: 'deployment.yaml',
          kubeconfigId: 'minikube-cluster',
          kubeconfigFile: ''
        )
      }
    }
  }
}
