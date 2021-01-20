from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import BoardSerializer, TaskSerializer
from rest_framework.generics import get_object_or_404


# Create your views here.

class BoardView(APIView):
    def get(self, request, pk=None):
        if pk:
            boards = get_object_or_404(Board.objects.all(), pk = pk)
            serializer = BoardSerializer(boards)
        else:
            boards = Board.objects.all()
            serializer = BoardSerializer(boards, many=True)
        return Response({"boards": serializer.data})

    def post(self, request):
        board = request.data.get('board')
        serializer = BoardSerializer(data=board)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
        return Response({"success": f"Board {board_saved.name} created successful"})

    def put(self, request, pk):
        saved_board = get_object_or_404(Board.objects.all(), pk=pk)
        data = request.data.get('board')
        serializer = BoardSerializer(instance=saved_board, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            board_saved = serializer.save()
        return Response({"success": f"Board {board_saved.name} updated successful"})

    def delete(self, request, pk):
        board = get_object_or_404(Board.objects.all(), pk=pk)
        board.delete()
        return Response({"message": f"Board {pk} has been deleted"}, status=204)


class TaskView(APIView):
    def get(self, request, pk):
        tasks = get_object_or_404(Task.objects.all(), board_id=pk)
        print(tasks)
        serializer = TaskSerializer(tasks)
        return Response({"boards": serializer.data})
