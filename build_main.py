import jenkins
import argparse

# NB: Don't use SSL. You will get an error like: SSL: WRONG_VERSION_NUMBER
JENKINS_SERVER_IP = "http://218.147.131.59:8080/"
USER_NAME = "tfsmaster"
PASSWORD = "testworks"
# token is required to schedule jobs through build_job API
TOKEN = "1128e6c8467c7088f58c130916ca0eabeb"
TARGET_JOB = "2_AUTOMATION_TEST"


if __name__ == "__main__":
    # Create the parser
    arg_parser = argparse.ArgumentParser()

    # Add arguments
    arg_parser.add_argument('--file_path', help='file path')

    # Execute the parse_args() method
    args = arg_parser.parse_args()

    server = jenkins.Jenkins(JENKINS_SERVER_IP, username=USER_NAME, password=PASSWORD)

    # Get all builds
    jobs = server.get_all_jobs(folder_depth=None)
    for job in jobs:
        print(job)
        job_name = job['fullname']
        job_info = server.get_job_info(job_name)

        # print all job info
        for key, val in job_info.items():
            print("\t{}\t{}".format(key, val))

        if TARGET_JOB == job_name:
            print("Target job {} found".format(TARGET_JOB))
            break

    # queue up a build
    job_id = server.build_job(TARGET_JOB, None, TOKEN)

    # TODO: doesn't work
    # Parameters: id – Jenkins job id number for the build, int
    res = server.cancel_queue(job_id)
    print(job_id)

    # res = server.cancel_queue("110")
    print(res)
