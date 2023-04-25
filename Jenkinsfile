pipeline {
  	agent any
	stages {
    	stage('Build') {
      		steps {
				bat 'mvn clean package'
        		bat 'docker-compose build'
				bat 'docker-compose up -d'
			}
		}
	
		stage('SonarQube Analysis') {
			steps {
				withSonarQubeEnv('sonarserver') {
					bat 'msbuild /t:Rebuild'
					sonarqube analysis
				}
			}
		}
	}
}

