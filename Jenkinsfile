pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/your-username/your-repository.git'
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
          def dockerImage = docker.build('your-image-name')
          docker.withRegistry('https://your-docker-registry', 'docker-credentials-id') {
            dockerImage.push()
          }
        }
      }
    }

    stage('Minikube Deploy') {
      steps {
        kubernetesDeploy(
          configs: 'your-deployment-file.yaml',
          kubeconfigId: 'minikube-kubeconfig',
          kubeconfigFile: ''
        )
      }
    }
  }
}
