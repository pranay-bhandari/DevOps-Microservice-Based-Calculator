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
			steps {
				withSonarQubeEnv('sonarserver') {
					bat "msbuild.exe /p:Configuration=Release /t:Build MyProject.csproj"
					bat 'msbuild /t:Rebuild'
					sonarqube analysis
				}
			}
		}
	}
}

