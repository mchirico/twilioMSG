import boto3
#  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html
# java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

class DYN:
    def load_movies(self, movies, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

        table = dynamodb.Table('Movies')
        for movie in movies:
            year = int(movie['year'])
            title = movie['title']
            print("Adding movie:", year, title)
            table.put_item(Item=movie)


    def create_movie_table(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

        table = dynamodb.create_table(
            TableName='Movies',
            KeySchema=[
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table



    
