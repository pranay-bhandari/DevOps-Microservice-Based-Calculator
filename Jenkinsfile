pipeline {
	agent any
	stages {
		stage('Maven Build') {
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
						     -Dsonar.host.url=http://192.168.85.1:9000/ \
						     -Dsonar.login=squ_971d22c4c6eeadec4d6ca3bf2959ff05aedeb356'
					}
				}
			}
		}
	}
}
