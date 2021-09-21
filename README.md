# gRPC-server
> gRPC server example code

### Install required python library
```bash
$ python -m pip install --upgrade pip
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```

### Start proto buffer compiler 
```bash
$ cd calculator
$ python3 -m grpc_tools.protoc -I ../proto --python_out=. --grpc_python_out=. ../proto/calculator.proto
```

