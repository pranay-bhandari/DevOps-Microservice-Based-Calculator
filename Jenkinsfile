pipeline {
  	agent any
	stages {
    	stage('Build') {
      		steps {
        		bat 'docker-compose build'
				bat 'docker-compose up -d'
			}
		}
	}
}

stage('SonarQube Analysis') {
			steps {
				withSonarQubeEnv('SonarQube Server') {
					bat 'msbuild /t:Rebuild'
					sonarqube analysis
				}
			}
		}
	}
}
