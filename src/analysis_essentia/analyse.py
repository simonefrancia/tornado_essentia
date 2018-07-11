import os,json

EXTRACTORS_FOLDER = "/essentia/essentia/build/src/examples/"


def analysisFromLocal(filepath="", output="output.json", profile="analysis_essentia/profile.yaml"):

    DOWNLOADED = False

    if filepath=="":
        print("Downloading Song..............")
        DOWNLOADED=True

        filepath = "sample.mp3"
        os.system("wget -c https://www.freesounds.info/global/wav.php?fileid=101 -o {0} ".format(filepath))

    os.system(EXTRACTORS_FOLDER + "streaming_extractor_music {0} {1} {2}".format(filepath, output, profile))

    if DOWNLOADED:
        os.system('rm {0}'.format(filepath))

    data = []

    if os.path.exists(output):
        with open(output) as f:
            data = json.load(f)
        os.system('rm {0}'.format(output))

    return data



def analysisFromAWS(filepath):
    output = self.get_argument("o", "output", True)

    print(output)

    details = self.get_argument("details", None, True)

    BUCKET_NAME = 'my-bucket'  # replace with your bucket name
    KEY = 'my_image_in_s3.jpg'  # replace with your object key

    s3 = boto3.resource('s3')

    """try:
        s3.Bucket(BUCKET_NAME).download_file(url, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    """

    print("ffmpeg -url {0} -i {1} -o {2}".format(url, input, output))
    # os.system("ffmpeg -url {0} -i {1} -o {2}")

    pass

