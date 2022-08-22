import argparse
import os


def parse_arguments() -> argparse.Namespace:
    """Parse the arguments provided to the operator job, according to the arguments set specified

    :return: Arguments object with the parsed arguments
    """
    parser = argparse.ArgumentParser(description='s3fs test')
    parser.add_argument('--bucket-name', required=True, help='Name of s3 bucket')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    print('Checking mount status')
    if os.path.ismount(f"{args.bucket_name}/"):
        print(f"bucket {args.bucket_name} mounted successfully :)")
    else:
        print(f"bucket {args.bucket_name} not mounted :(")
    print("list s3 directories")
    print(os.listdir(f"{args.bucket_name}/"))
