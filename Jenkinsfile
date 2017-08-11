node('master') {
    stage('Build') {
        sh "echo Build"
    }
    stage('Test'){
      parallel (
        "JUnit": {
            sh "echo JUnit"
        },
        "DBUnit": {
            sh "echo DBUnit"
        },
        "Jasmine": {
            sh "echo Jasmine"
        },
      )
    }
 }
