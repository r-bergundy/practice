node('master') {
    stage('Build') {
        sh "echo Build"
        sh "ls ${WORKSPACE}"
        sh "python -m unittest tests.test_unit_account.TestAccount"
    }
 }
