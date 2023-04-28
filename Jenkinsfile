pipeline {
    agent any
    environment {
        PROMETHEUS_PORT = 9090
        SCANNER_HOME = tool 'SonarQube_Scanner'
    }
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
                    def jobName = env.JOB_NAME.replace('/', '_')
                    def buildName = env.BUILD_NUMBER
                    sh "echo 'jenkins_job_build_info{job_name=\"${jobName}\",build_name=\"${buildName}\"} 1' | curl --data-binary @- http://192.168.85.1:${PROMETHEUS_PORT}/metrics/job/${jobName}/build/${buildName}"
                }
            }
        }
    }
    post {
        always {
            script {
                def jobName = env.JOB_NAME.replace('/', '_')
                def buildName = env.BUILD_NUMBER
                def buildUrl = env.BUILD_URL.replace(env.JENKINS_URL, "")

                sh "curl -X POST -H 'Content-Type: application/json' -d '{\"dashboard\": {\"title\": \"${jobName}-${buildName}\"}, \"folderId\": 0, \"overwrite\": true}' http://admin:pranay@1234@192.168.85.1:3000/api/dashboards/db"

                sh "curl -X POST -H 'Content-Type: application/json' -d '{\"title\": \"Build Metrics\", \"targets\": [{\"expr\": \"jenkins_job_build_info{job_name=\\\"${jobName}\\\", build_name=\\\"${buildName}\\\"}\"}], \"panels\": [{\"title\": \"Build Info\", \"type\": \"stat\", \"targets\": [{\"expr\": \"jenkins_job_build_info{job_name=\\\"${jobName}\\\", build_name=\\\"${buildName}\\\"}\"}]}]}' http://admin:pranay@1234@192.168.85.1:3000/api/dashboards/db/${jobName}-${buildName}/panel"
            }
        }
    }
}
