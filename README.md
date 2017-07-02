# Wotizdis ?

Just a very simple and basic flask based, Amazon S3 file uploader.
It uses boto3 to connect and interact with the AWS low level API.

# Why ?

Why is the sky blue ? (is it ?)

# Installation instructions

1. clone the repo (or fork it)

```bash
git clone https://github.com/Zabanaa/flask-s3-uploads.git
```

2. Create a virtualenv and activate it

```bash
virtualenv -p python3 ENV_flask_s3_uploads

source /path/to/project/ENV_flask_s3_uploads
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Export your AWS credentials

```bash
export S3_BUCKET_NAME="name of your bucket"
export S3_ACCESS_KEY="your aws access key"
export S3_SECRET_ACCESS_KEY="your aws secret access key"
```

5. Run the app

```bash
python wsgi.py
```

6. Navigate to `localhost:5000` or whichever port you chose to use, and enjoy
   life.

# License

Do what the fuck you want license

_Note: this is really just a learning project that I aim to use as a reference
for when I need to actually use AWS in real world client/work projects. It will
certainly evolve as a learn more about the AWS and S3
