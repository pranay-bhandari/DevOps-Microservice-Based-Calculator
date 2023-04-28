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

			stage('Prometheus Metrics Collection') {
    steps {
        prometheus([
            prometheusGlobalConfig: [
                prometheusJobBuildTimestamp: true,
                prometheusJobUrl: true,
                prometheusMetricsPath: '/prometheus',
                prometheusPushGatewayUrl: 'http://192.168.85.1:9090'
            ],
            prometheusJobConfig: [
                jobName: 'project-pipeline',
                scrapeInterval: 1
            ]
        ])}
    
				}
			}
		}
	}
}

post {
    always {
        grafana(
            url: 'http://192.168.85.1:3000',
            grafanaUrl: 'http://192.168.85.1:9090',
            dataSourceName: 'Prometheus',
            grafanaFolderId: 1,
            dashboard: """
                {
                    "title": "db",
                    "rows": [
                        {
                            "title": "My Metric",
                            "panels": [
                                {
                                    "title": "My Panel",
                                    "targets": [
                                        {
                                            "query": "my_metric",
                                            "refId": "A"
                                        }
                                    ],
                                    "type": "graph",
                                    "span": 12
                                }
                            ]
                        }
                    ]
                }
            """
        )
    }
}
}
