pipeline {
  	agent any
	stages {
    	stage('Build') {
      		steps {
        		bat 'docker-compose build'
				bat 'docker-compose up -d'
			}
		}
	
		stage('SonarQube analysis') {
      		steps {
        // Add SonarQube scanner step
        withSonarQubeEnv('My SonarQube Server') {
          bat 'mvn clean package sonar:sonar'
				}
			}
		}
	}
}

