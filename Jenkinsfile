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
				SCANNER_HOME = tool 'SonarQube Scanner'
			}
			steps {
				script {
					def scannerHome = tool 'SonarQube Scanner'
					withEnv(["PATH+SCANNER=${scannerHome}\\bin"]) {
						bat 'dotnet tool install --global dotnet-sonarscanner'
						bat 'dotnet sonarscanner begin /k:"DevOps" /d:sonar.host.url="http://sonarqube-server:9000" /d:sonar.login="${env.SONAR_TOKEN}"'
						bat 'dotnet build'
						bat 'dotnet sonarscanner end /d:sonar.login="${env.SONAR_TOKEN}"'
					}
				}
			}
		}
	}
}