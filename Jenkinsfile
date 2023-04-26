pipeline {
    agent any
    environment {
        SONAR_URL = "http://localhost:9000"
        SONAR_LOGIN = credentials('sonarqube-token')
    }
    stages {
        stage('Build') {
            steps {
                bat 'docker-compose build'
                bat 'docker-compose up -d'
            }
        }
    
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarserver') {
                    bat 'dotnet build'
                    bat "sonar-scanner \
                        -Dsonar.projectKey=DevOps \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${env.SONAR_URL} \
                        -Dsonar.login=${env.SONAR_LOGIN}'
                }
            }
		}
	}
}