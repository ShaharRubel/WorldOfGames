pipeline {
agent any
    stages {
        stage("Clone Repo") {
            steps {
                git([url: 'git@github.com:ShaharRubel/WorldOfGames.git', branch: 'main', credentialsId: 'github_repo'])
            }
        }
        stage("Building docker image"){
            steps {
                bat 'docker build -t worldofgames .'
            }
        }
        stage("Run dockerized application"){
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage("Test application"){
            steps {
                bat 'python e2e.py'
            }
        }
        stage("finalize and push image"){
            steps {
                bat 'echo pass'
            }
        }
    }
}