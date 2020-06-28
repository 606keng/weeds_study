pipeline{
    agent any
    stages{
        stage("get code"){
           steps{
                echo "get code"
           }
        }
        stage("unit test"){
           steps{
                echo "unit test"
           }
        }
        stage("package"){
            steps{
                sh 'tar zcf /opt/web-${BUILD_ID}.tar.gz ./* --exclude=./git --exclude=Jenkinsfile'
            }
        }
        stage("deploy"){
            steps{
                sh 'ssh 10.0.0.7 "cd /html && mkdir web-${BUILD_ID}"'
                sh 'scp /opt/web-${BUILD_ID}.tar.gz 10.0.0.7:/html/web-${BUILD_ID}'
                sh 'ssh 10.0.0.7 "cd /html/web-${BUILD_ID} && tar xf web-${BUILD_ID}.tar.gz && rm -rf web-${BUILD_ID}.tar.gz"'
                sh 'ssh 10.0.0.7 "cd /html && rm -rf test && ln -s web-${BUILD_ID} /html/test"'
            }
        }
    }
}