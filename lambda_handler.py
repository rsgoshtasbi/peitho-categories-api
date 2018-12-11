from __future__ import print_function

import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(body):
    return {
        'categories': body,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    categories = [
        "Food/Drink",
        "Fashion",
        "Beauty & Personal Care",
        "Social Media",
        "Photography, Art, Design",
        "Health, Fitness, Sport",
        "Travel",
        "Hotel & Leisure",
        "Auto",
        "Children and Family",
        "Home and Garden",
        "Animals",
        "Education and Books",
        "Business, Finance, Insurance",
        "Foundations and NFP"
    ]
    
    return respond(categories)