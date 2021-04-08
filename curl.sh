#!/bin/bash
curl -d '{"value": "a"}' -H 'Content-Type: application/json' http://localhost:8080
curl -d '{"value": "a"}' -H 'Content-Type: application/json' http://localhost:8080/post