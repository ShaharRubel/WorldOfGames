pipeline {
agent any
environment {
   registryCredential = 'dockerhub_id'
   imagename = "darkerlighter/worldofgames"
    }
    stages {
        stage("Clone Repo") {
            steps {
                git([url: 'git@github.com:ShaharRubel/WorldOfGames.git', branch: 'main', credentialsId: 'github_repo'])
            }
        }
        stage("Building docker image"){
            steps {
                bat 'docker build -t worldofgames .'
                bat "docker tag worldofgames ${imagename}:latest"
            }
        }
        stage("Run dockerized application"){
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage("Test application"){
            steps {
                bat 'python ./tests/e2e.py'
            }
        }
        stage("Finalize and push image"){
            steps {
            script {
                   withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                       // Login with credentials
                       bat "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                       // Push the image
                       bat "docker push ${imagename}:latest"

                       bat 'docker-compose down'
                       bat "docker image rmi ${imagename}:latest"
                   }
                }
            }
        }
    }
}