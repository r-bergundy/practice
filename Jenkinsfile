node('master') {
    stage('Build') {
        sh "echo Build"
        sh "python -m unittest tests.test_unit_account.TestAccount"
    }
 }
