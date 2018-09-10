#!/bin/bash
cd thrift

thrift -out ../nodejs --gen js:node test.thrift
thrift -out ../python --gen py test.thrift