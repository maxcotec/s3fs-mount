# s3fs mount from Docker container

<img alt="alt text" height="300" src="s3fs docker mount.png" width="600"/>

This repository contains a singleton Dockerfile that is capable of mounting s3 bucket 
as file system using s3fs fuse. 

Watch video tutorial on [YouTube](https://www.youtube.com/watch?v=de4uZ2yCGlg);

## Prerequisite

* Make sure you already have an s3 bucket in your AWS account. 
* create an IAM user with following policy;
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::<s3_bucket>"
        },
        {
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::<s3_bucket>/*"
        }
    ]
}
```
* create security credentials (ACCESS_KEY_ID and SECRET_ACCESS_KEY) for your IAM user.

## Usage

Build the image

```dockerfile
docker build . -t <your_tag_here> --build-arg BUCKET_NAME=<your_s3_bucket_name>
```

run container
```dockerfile
docker run -it -e ACCESS_KEY_ID=<access_key_id> -e SECRET_ACCESS_KEY=<secret_access_key> --privileged <image_tag>
```

### Using different base image

This Dockerfile uses `python:3.8-slim` as base image, which is Debian. if 
the base image you choose has different OS, then make sure to change the 
installation procedure in Dockerfile (@ line 45) `apt install s3fs -y`. To install 
s3fs for desired OS, follow the official [installation guide](https://github.com/s3fs-fuse/s3fs-fuse#installation) 

