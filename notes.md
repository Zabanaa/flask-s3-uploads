```python

# import boto3, botocore

# s3 = boto3.client(
#    "s3",
#    aws_access_key_id=S3_KEY,
#    aws_secret_access_key=S3_SECRET
#)

# Upload a file (a binary object)
# just copy the function below and add comments

# Generate a presigned url for a file
# url = s3.generate_presigned_url(
#     ClientMethod="get_object",
#     Params={
#         "Bucket": S3_BUCKET,
#         "Key": "psql_todo.md"
#     },
#     ExpiresIn=10000
#

# If you don't want to restrict access based on time, just split the url on ? and return the first part
# url = url.split("?")[0]

# buckets         = s3.list_buckets()
# objects         = s3.list_objects(Bucket=S3_BUCKET)
# objects         = s3.list_objects_v2(Bucket=S3_BUCKET)

# # Access the files in a bucket
# all_files       = objects["Contents"]

# Get the total number of files in the bucket
# number_of_files = objects["KeyCount"]

# ! If not using client.list_objects (not v2) !
# number_of_files = len(all_files)

# # Get each file's name
# file_names      = [file["Key"] for file in objects["Contents"]]
```

This is what the final function looks like

```python
def upload_file_to_s3(file, bucket_name, acl="public-read"):

    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={"ACL": acl}
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e


    file_url = s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": S3_BUCKET,
            "Key": "psql_todo.md"
        },
        ExpiresIn=10000
    )

    return file_url

```

