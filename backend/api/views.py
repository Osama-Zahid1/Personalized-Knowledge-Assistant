from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from django.core.cache import cache
import os

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize LlamaIndex with some documents
class ChatView(APIView):
    index = None

    @classmethod
    def initialize_index(cls):
        if not cls.index:
            # Load documents from a directory named 'documents' (should contain your text files)
            documents = SimpleDirectoryReader('documents').load_data()
            cls.index = VectorStoreIndex.from_documents(documents)

    def post(self, request):
        query = request.data.get('query')
        if query:
            # Check if the response for the query is already cached
            cached_response = cache.get(query)
            if cached_response:
                return Response({'response': cached_response}, status=status.HTTP_200_OK)

            # Ensure the index is initialized with documents
            self.initialize_index()
            
            try:
                # Retrieve the response from LlamaIndex
                response = self.index.query(query)

                # Cache the response for future use (e.g., cache for 24 hours)
                cache.set(query, response, timeout=86400)

                return Response({'response': response}, status=status.HTTP_200_OK)
            except openai.error.RateLimitError as e:
                return Response(
                    {'error': 'Rate limit exceeded. Please try again later.'},
                    status=status.HTTP_429_TOO_MANY_REQUESTS,
                )
            except Exception as e:
                return Response(
                    {'error': f'An unexpected error occurred: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response({'error': 'Query not provided'}, status=status.HTTP_400_BAD_REQUEST)
