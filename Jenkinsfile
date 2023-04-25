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
    	def scannerHome = tool 'SonarScanner';
   		 withSonarQubeEnv() {
      	bat "${scannerHome}/bin/sonar-scanner"
				}
			}
		}
	}
}

