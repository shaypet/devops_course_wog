pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/shaypet/devops_course_wog.git'
            }
        }
        stage('Build') {
            steps {
                bat 'docker compose build'
            }
        }
        stage('Run') {
            steps {
                bat 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'py tests/e2e.py 8777'
            }
        }
        stage('Finalize') {
            steps {
               echo 'push'
            }
        }
    }
    post{
        always{
            bat 'docker compose down'
        }
    }
}
