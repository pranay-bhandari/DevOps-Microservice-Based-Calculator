pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'docker-compose build'
                bat 'docker-compose up -d'
            }
        }
        stage('SonarQube Analysis') {
            environment {
                scannerHome = tool 'SonarQube Scanner'
            }
            steps {
                withSonarQubeEnv('sonarserver') {
					dir ("\"${workspace}\"") {
                    script {
                        def scannerCmd = "${scannerHome}/bin/sonar-scanner"
                        bat "${scannerCmd} -Dsonar.login=${env.SONAR_LOGIN}"
                    }
                }
            }
        }
    }
}