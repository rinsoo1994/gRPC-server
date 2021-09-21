import logging
import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = calculator_pb2_grpc.CalculateStub(channel)
        response = stub.GetPlus(calculator_pb2.CalculateRequest(x=1, y=2, input_num_values=[1,2,3,4,5], input_nums=[1,2,3,4,5]))
        print("GetPlus client received: " + response.result, response)
        response = stub.GetMinus(calculator_pb2.CalculateRequest(x=1, y=2, input_num_values=[1,2,3,4,5], input_nums=[1,2,3,4,5]))
        print("GetMinus client received: " + response.result)
        response = stub.GetMultiply(calculator_pb2.CalculateRequest(x=1, y=2, input_num_values=[1,2,3,4,5], input_nums=[1,2,3,4,5]))
        print("GetMultiply client received: " + response.result)
        response = stub.GetDivision(calculator_pb2.CalculateRequest(x=1, y=2, input_num_values=[1,2,3,4,5], input_nums=[1,2,3,4,5]))
        print("GetDivision client received: " + response.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()


