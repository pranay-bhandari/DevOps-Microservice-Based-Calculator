pipeline {
  agent any
  tools {
    // define SonarQube Scanner
    sonarqubeScanner 'SonarQube'
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
        withSonarQubeEnv('sonarsever') {
          dir("\"${workspace}\"") {
            bat 'dotnet build'
            bat "sonar-scanner -Dsonar.login=${env.SONAR_LOGIN}"
          }
        }
      }
    }
  }
}