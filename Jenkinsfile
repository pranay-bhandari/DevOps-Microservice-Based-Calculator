pipeline {
  	agent any
	stages {
    	stage('Build') {
      		steps {
        		sh 'docker-compose build'
				sh 'docker-compose up -d'
			}
		}
	}
}
