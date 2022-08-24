import os

if __name__ == "__main__":
    print('Checking mount status')
    if os.path.ismount(f"s3_bucket/"):
        print(f"bucket mounted successfully :)")
    else:
        print(f"bucket not mounted :(")
    print("list s3 directories")
    print(os.listdir(f"s3_bucket/"))
