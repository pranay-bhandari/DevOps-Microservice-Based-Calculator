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
				SCANNER_HOME = tool 'SonarQube_Scanner'
			}
			steps {
				script {
					def scannerHome = tool 'SonarQube_Scanner'
					withEnv(["PATH+SCANNER=${scannerHome}\\bin"]) {
						bat 'sonar-scanner.bat \
						     -Dsonar.projectKey=DevOps \
						     -Dsonar.sources=. \
						     -Dsonar.host.url=http://sonarqube-server:9000 \
						     -Dsonar.login='sqp_ed97c0184cad643ae982d46a518ee9ed4892df5e' \
					}
				}
			}
		}
	}
}
