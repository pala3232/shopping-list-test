pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/pala3232/testtodo.git', branch: 'main'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh './venv/bin/python -m unittest discover'
            }
        }
        stage('Build and Run Docker Image') {
            steps {
                sh 'docker build -t testtodo-app -f Dockerfile .'
                sh 'docker rm -f mytodo || true'
                sh 'docker run -d --name mytodo -p 5000:5000 testtodo-app:latest'
                sh 'sleep 5'
                sh 'docker stop mytodo'
                sh 'docker rm mytodo'
            }
        }
    }
}
