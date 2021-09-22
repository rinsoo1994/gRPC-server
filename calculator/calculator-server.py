from concurrent import futures
import logging
import grpc


import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculateServicer):
    def GetPlus(self, request, context):
        response = int(request.x) + int(request.y)
        return calculator_pb2.CalculateReply(result=str(response))

    def GetMinus(self, request, context):
        response = int(request.x) - int(request.y)
        return calculator_pb2.CalculateReply(result=str(response))

    def GetMultiply(self, request, context):
        response = int(request.x) * int(request.y)
        return calculator_pb2.CalculateReply(result=str(response))

    def GetDivision(self, request, context):
        response = int(request.x) / int(request.y)
        return calculator_pb2.CalculateReply(result=str(response))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculateServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
