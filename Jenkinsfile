pipeline {
    agent any
    stages {
        stage('Maven Build') {
            steps {
                bat 'docker-compose build'
                bat 'docker-compose up -d'
                bat 'mvn clean install'
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

        stage('Start Prometheus') {
            steps {
                bat 'docker run -d -p 9092:9092 --name prometheus prom/prometheus'
            }
        }

        stage('Create Grafana Dashboard') {
            environment {
                PROMETHEUS_PORT = 9090
                API_KEY = 'eyJrIjoiMmdQUkFWNDVzUWVFSVpuNkZXdGpIWTMxNHExWEExSmIiLCJuIjoiRGV2T3BzIiwiaWQiOjF9'
            }
            steps {
                bat 'docker run -d -p 3001:3000 --name grafana grafana/grafana'
//                 bat 'timeout /t 10 /nobreak'
                bat "curl -X POST -H \"Content-Type: application/json\" \
                    -d '{\"name\":\"db\",\"type\":\"prometheus\",\"url\":\"http://192.168.85.1:9090\",\"access\":\"proxy\",\"isDefault\":true}' \
                    http://admin:${API_KEY}@192.168.85.1:3000/api/datasources"
                bat "curl -X POST -H \"Content-Type: application/json\" \
                    -d '{\"dashboard\":{\"id\":null,\"title\":\"${JOB_NAME}-${BUILD_NUMBER}\",\"tags\":[\"devops\"],\"timezone\":\"browser\",\"schemaVersion\":21,\"panels\":[{\"id\":1,\"gridPos\":{\"x\":0,\"y\":0,\"w\":12,\"h\":8},\"type\":\"graph\",\"title\":\"Panel Title\",\"datasource\":\"db\",\"targets\":[{\"expr\":\"up\",\"legendFormat\":\"\",\"refId\":\"A\"}],\"xaxis\":{\"mode\":\"time\",\"show\":true},\"yaxes\":[{\"format\":\"short\",\"show\":true},{\"format\":\"short\",\"show\":true}]},{\"collapsed\":false,\"gridPos\":{\"h\":2,\"w\":24,\"x\":0,\"y\":8},\"id\":2,\"panels\":[],\"title\":\"\",\"type\":\"row\"}],\"version\":0,\"links\":[]},\"overwrite\":false}' \
                    http://admin:${API_KEY}@192.168.85.1:3000/api/dashboards/db"
            }
        }
    }

//     post {
//         always {
//             bat 'docker-compose down'
//             bat 'docker stop prometheus'
//             bat 'docker rm prometheus'
//             bat 'docker stop grafana'
//             bat 'docker rm grafana'
//         }
//     }
// }

}
