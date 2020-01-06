from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch import Elasticsearch, helpers

from logs.elasticsearch_logs.api.serializers import LogsSerializer
from logs.elasticsearch_logs.models import Logs


class Query(APIView):
    '''Query elasticsearch service, save query-response and return response'''
    '''{   
        "client_id":"atomberg",
        "question":"What are store timings?",
        "category":"general_queries"
    }'''
    def post(self, request, format=None):
        data = request.data

        es = Elasticsearch([settings.ELASTICSEARCH_BASE_URL])
        body = { 
            "_source": ["Category","Answer","Question","Action","Action-Param"],
            "query": {
                "bool": {
                    "must": [{
                            "match_phrase": {
                                "Category": data["category"]
                            }
                        },
                        {
                            "match": {
                                "Question": data["question"]
                            }
                        }]
                }
            }
        }
        response = es.search(index=data["client_id"], body=body)
        response_data = response.get("hits")["hits"][0]

        db_data = {
            "client_id":data["client_id"],
            "query_id":response_data["_id"],
            "question":data["question"],
            "question_matched":response_data["_source"]["Question"],
            "answer":response_data["_source"]["Answer"],
            "action":response_data["_source"]["Action"],
            "action_param":response_data["_source"]["Action-Param"],
            "score":response_data["_score"],
        }

        serializer = LogsSerializer(data=db_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        all_logs = Logs.objects.all()
        serializer = LogsSerializer(all_logs, many=True)
        return Response(serializer.data)