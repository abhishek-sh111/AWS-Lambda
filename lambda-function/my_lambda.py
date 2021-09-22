def my_lambda(event,context):
    #fetching bucket name
    bucket=event['Records'][0]['s3']['bucket']['name']
    #fetching object key
    key=urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8')

    try:
        response=s3.get_object(Bucket=bucket,Key=key)
        text=response["Body"].read().decode()
        data=json.loads(text)
        print(data)
        books=data["books"]
        for book in books:
            print(record['bookType'])
        return 'Success'
    except Exception as e:
        print(e)
        raise e