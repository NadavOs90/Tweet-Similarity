import boto3
import sys


def main(*args):
    access_key = "AKIAJX7SJ3BXPEGL2YQQ"
    secret_key = "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"
    client = boto3.client('emr', aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key, region_name='us-east-1')
    N = args[0]
    print 'N = {}'.format(N)
    S3_BUCKET = 'dsp2gnfinal'
    S3_KEY = 'spark/main.py'
    S3_URI = 's3://{bucket}/{key}'.format(bucket=S3_BUCKET, key=S3_KEY)
    CORPUS = "TinyCorpus.txt"
    print 'Corpus = {}'.format(CORPUS)


    client.run_job_flow(
        Name="DS2",
        ReleaseLabel='emr-4.8.0',
        Instances={
            'MasterInstanceType': 'm1.medium',
            'SlaveInstanceType': 'm1.medium',
            'InstanceCount': 2,
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
        },
        Applications=[],
        LogUri="s3://{}/logs/".format(S3_BUCKET),
        BootstrapActions=[],
        Configurations=[
                         {
                             "Classification": "spark-defaults",
                             "Properties": {}
                         }
                     ],
        Steps=[
            {
                'Name': 'Setup Debugging',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['state-pusher-script']
                }
            },
            {
                'Name': 'Record Reader and index',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/record_reader.py,s3://{bucket}/index_reducer.py".format(bucket=S3_BUCKET),
                             '-mapper', "record_reader.py",
                             '-reducer', "index_reducer.py",
                             '-input', "s3://{}/{}".format(S3_BUCKET, CORPUS),
                             '-output', "s3://{}/output/record_reader".format(S3_BUCKET)
                             ]
                }
            },
            {
                'Name': 'Step 1 - words',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/first_mapper.py,s3://{bucket}/first_reducer.py".format(bucket=S3_BUCKET),
                             '-mapper', "first_mapper.py",
                             '-reducer', "first_reducer.py",
                             '-input', "s3://{}/output/record_reader/part-000*".format(S3_BUCKET),
                             '-output', "s3://{}/output/step1".format(S3_BUCKET)
                             ]
                }
            },
            {
                'Name': 'Step 2 - tfidf',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/second_mapper.py,s3://{bucket}/second_reducer.py".format(bucket=S3_BUCKET),
                             '-mapper', "second_mapper.py",
                             '-reducer', "second_reducer.py",
                             '-input', "s3://{}/output/step1/part-000*".format(S3_BUCKET),
                             '-output', "s3://{}/output/step2".format(S3_BUCKET)
                             ]
                }
            },
            {
                'Name': 'Step 3 - cos',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/third_mapper.py,s3://{bucket}/third_reducer.py".format(
                                 bucket=S3_BUCKET),
                             '-mapper', "third_mapper.py",
                             '-reducer', "third_reducer.py",
                             '-input', "s3://{}/output/step2/part-000*".format(S3_BUCKET),
                             '-output', "s3://{}/output/step3".format(S3_BUCKET)
                             ]
                }
            },
            {
                'Name': 'Step 4 - tweet pairs',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/fouth_mapper.py,s3://{bucket}/fourth_reducer.py".format(
                                 bucket=S3_BUCKET),
                             '-mapper', "fouth_mapper.py",
                             '-reducer', "fourth_reducer.py",
                             '-input', "s3://{}/output/step3/part-000*".format(S3_BUCKET),
                             '-output', "s3://{}/output/step4".format(S3_BUCKET)
                             ]
                }
            },
            {
                'Name': 'Step 5 - topN',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['hadoop-streaming',
                             '-files',
                             "s3://{bucket}/fifth_mapper.py,s3://{bucket}/fifth_reducer.py".format(
                                 bucket=S3_BUCKET),
                             '-mapper', "fifth_mapper.py",
                             '-reducer', "fifth_reducer.py",
                             '-input', "s3://{}/output/step4/part-000*".format(S3_BUCKET),
                             '-output', "s3://{}/output/step5".format(S3_BUCKET)
                             ]
                }
            }
        ],
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole'
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main(10)